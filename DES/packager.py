from DES.ConvAlphaBin import conv_bin, nib_vnoc


class Packager:
    def __init__(self, packet_size):
        self.packet_size = packet_size

    def __call__(self, message):
        packets = [message[i:i + self.packet_size] for i in range(0, len(message), self.packet_size)]
        packets[-1] = packets[-1] + '0' * (self.packet_size - len(packets[-1]))
        return packets
