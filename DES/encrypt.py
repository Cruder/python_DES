import sys
from DES.key import Key
from DES.constants import Constants
from DES.extractor import Extractor
from DES.packager import Packager
from DES.permutator import Permutator
from DES.round import Round

from DES.ConvAlphaBin import conv_bin, nib_vnoc


class Encrypt:
    def __init__(self):
        pass

    def __call__(self, message, key):
        # Convert message to binary
        message = conv_bin(message)

        # Fetch constants from file
        constants = Constants()

        # Slice the message into a 64bit data
        packager = Packager(64)

        # Permute data for messages
        initial_permutator = Permutator(offset=-1)

        # Class to extract 16 sub key from the key
        # Initialized from CP1 and CP2
        extractor = Extractor(constants.cp1(), constants.cp2())

        # Extract sub keys
        # sub_keys : Array(16)
        sub_keys = key.extract_sub_keys(extractor)

        print(sub_keys)

        # packets : Array(64)
        packets = packager(message)
        new_packets = []

        for packet in packets:
            # packet : String | Permuted using PI
            packet = initial_permutator(packet, constants.pi())

            for i in range(16):
                round = Round(sub_keys[i], constants.perm(), constants.expansion(), constants.substitutions())
                left = message[0:32]
                right = message[32:]
                left, right = round(left, right)
                packet = left + right

            packet = initial_permutator(packet, constants.inv_pi())
            new_packets.append(packet)
        return ''.join(new_packets)


class Decrypt:
    def __init__(self):
        pass

    def __call__(self, message, key):
        # Fetch constants from file
        constants = Constants()

        # Slice the message into a 64bit data
        packager = Packager(64)

        # Permute data for messages
        initial_permutator = Permutator(offset=-1)

        # Class to extract 16 sub key from the key
        # Initialized from CP1 and CP2
        extractor = Extractor(constants.cp1(), constants.cp2())

        # Extract sub keys
        # sub_keys : Array(16)
        sub_keys = key.extract_sub_keys(extractor)

        # packets : Array(64)
        packets = packager(message)
        new_packets = []

        for packet in packets:
            # packet : String | Permuted using PI
            packet = initial_permutator(packet, constants.pi())

            for i in range(16, 0, -1):
                round = Round(sub_keys[i], constants.perm(), constants.expansion(), constants.substitutions())
                left = message[0:32]
                right = message[32:]
                left, right = round(right, left)
                packet = left + right

            packet = initial_permutator(packet, constants.inv_pi())
            new_packets.append(packet)
        new_packets = ''.join(new_packets)

        nib_vnoc('') # Final
