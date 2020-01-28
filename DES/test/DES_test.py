import unittest

from DES.constants import Constants
from DES.encrypt import Encrypt, Decrypt
from DES.extractor import Extractor
from DES.key import Key
from DES.packager import Packager
from DES.permutator import Permutator
from DES.round import Round


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.constants = Constants()
        self.initial_permutator = Permutator(offset=-1)
        self.packager = Packager(64)
        self.message = "1101110010111011110001001101010111100110111101111100001000110010100111010010101101101011111000110011101011011111"

    def test_key(self):
        key = Key.from_file("./Messages/Clef_de_pdf.txt")
        expected_key = "01011110101101010100101111110101000000110110111101001000"
        self.assertEqual(key.str_without_control(), expected_key)

    def test_first_perm(self):
        key = Key.from_file("./Messages/Clef_de_pdf.txt")

        extractor = Extractor(self.constants.cp1(), self.constants.cp2())
        first_perm = extractor.first_perm(key.key)
        expected_first_perm = "11000000000111110100100011110010111101001001011010111111"
        self.assertEqual(first_perm, expected_first_perm)

    def subkey(self):
        key = Key.from_file("./Messages/Clef_de_pdf.txt")

        extractor = Extractor(self.constants.cp1(), self.constants.cp2())
        sub_keys = key.extract_sub_keys(extractor)

    def test_paquet_message(self):
        key = Key.from_file("./Messages/Clef_de_pdf.txt")

        extractor = Extractor(self.constants.cp1(), self.constants.cp2())
        sub_keys = key.extract_sub_keys(extractor)
        packets = self.packager(self.message)
        expected_packet_one = "1101110010111011110001001101010111100110111101111100001000110010"
        expected_packet_two = "1001110100101011011010111110001100111010110111110000000000000000"
        self.assertEqual(packets[0], expected_packet_one)
        self.assertEqual(packets[1], expected_packet_two)

    def test_initial_permutation(self):
        key = Key.from_file("./Messages/Clef_de_pdf.txt")

        extractor = Extractor(self.constants.cp1(), self.constants.cp2())
        sub_keys = key.extract_sub_keys(extractor)
        packets = self.packager(self.message)

        packet_perm = self.initial_permutator(packets[0], self.constants.pi())
        expected_packet_perm = "0111110110101011001111010010101001111111101100100000001111110010"
        self.assertEqual(packet_perm, expected_packet_perm)

    def test_round_one(self):
        key = Key.from_file("./Messages/Clef_de_pdf.txt")

        extractor = Extractor(self.constants.cp1(), self.constants.cp2())
        sub_keys = key.extract_sub_keys(extractor)
        packets = self.packager(self.message)

        packet = self.initial_permutator(packets[0], self.constants.pi())
        left, right = packet[0:32], packet[32:]
        round = Round(sub_keys[0], self.constants.perm(), self.constants.expansion(), self.constants.substitutions())
        left, right = round(left, right)
        expected_round_one = "0111111110110010000000111111001001111111101100100000001111110010"
        self.assertEqual(left+right, expected_round_one)


    def get_sub_keys(self):
        key = Key.from_file("./Messages/Clef_de_pdf.txt")
        extractor = Extractor(self.constants.cp1(), self.constants.cp2())
        return key.extract_sub_keys(extractor)

    def test_crypt(self):
        sub_keys = self.get_sub_keys()
        packets = self.packager(self.message)

        packet = self.initial_permutator(packets[0], self.constants.pi())
        for i in range(16):
            round = Round(sub_keys[i], self.constants.perm(), self.constants.expansion(), self.constants.substitutions())
            left = packet[0:32]
            right = packet[32:]
            left, right = round(left, right)
            packet = left + right

        expected_all_round = "0011000011001010010000100001110011010101001001100001000100011010"
        self.assertEqual(packet, expected_all_round)
        crypted_message = self.initial_permutator(packet, self.constants.inv_pi())
        expected_crypted_message = "1000100000110110101000010001001111001011011000001001010010010000"
        self.assertEqual(crypted_message, expected_crypted_message)

    def test_des_integration(self):
        key = Key.from_file("./Messages/Clef_de_1.txt")
        original_message = "Hello world my friends"
        encrypt = Encrypt()
        crypted_message = encrypt(original_message, key)
        decrypt = Decrypt()
        decrypted_message = decrypt(crypted_message, key)
        original_len = len(original_message)
        self.assertEqual(decrypted_message[:original_len], original_message)








if __name__ == '__main__':
    unittest.main()
