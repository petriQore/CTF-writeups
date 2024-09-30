# import os


# def xnor_bit(a_bit, b_bit):
#     if a_bit == "1" and b_bit == "1":
#         return "1"
#     elif a_bit == "1" and b_bit == "0":
#         return "0"
#     elif a_bit == "0" and b_bit == "1":
#         return "0"
#     elif a_bit == "0" and b_bit == "0":
#         return "1"


# def xnor_byte(a_byte, b_byte):
#     a_bits = get_bits_from_byte(a_byte)
#     b_bits = get_bits_from_byte(b_byte)

#     result_bits = [xnor_bit(a_bits[i], b_bits[i]) for i in range(8)]
#     result_byte = get_byte_from_bits(result_bits)
#     return result_byte


# def xnor_bytes(a_bytes, b_bytes):
#     assert len(a_bytes) == len(b_bytes)

#     return bytes([xnor_byte(a_bytes[i], b_bytes[i]) for i in range(len(a_bytes))])


# def get_bits_from_byte(byte):
#     return list("{:08b}".format(byte))


# def get_byte_from_bits(bits):
#     return int("".join(bits), 2)


message = b"Blue is greener than purple for sure!"
# key = os.urandom(37)

# flag = b"bctf{???????????????????????????????}"


# def main():
#     print(f"Key: {key.hex()}")
#     print(f"\nMessage: {message}")

#     encrypted = xnor_bytes(message, key)
#     print(f"Enrypted message: {encrypted.hex()}")

#     print(f"\nFlag: {flag}")
#     encrypted_flag = xnor_bytes(flag, key)
#     print(f"Encrypted flag: {encrypted_flag.hex()}")


# if __name__ == "__main__":
#     main()


xored = 0b00000001011000100111011100001100001010011000101000101111001101101111001001101010101110010111110111101101010010000110000101101101011000010000000000000011000011010111111000101111101100001111001100000101100100101111100010001111101111101110011101101011110000100101110101010000110010010100011000000111
flag= 0b00100001011011010111011000001111011100101001010000110100011011111100101001100000101100100010100011110001011100100110101001111101011000000011011100000000010100000110111100110001101000101101111000000110100100011100001010011100101000001110101101110101100101110001101100010100110011010001000001011011
ascii_string = ''.join(chr((xored >> (8 * i)) & 0xFF) for i in range((xored.bit_length() + 7) // 8))
xored = ascii_string[::-1]
from pwn import xor
key = xor(xored, message)
# print(xor_with_message)
ascii_flag = ''.join(chr((flag >> (8 * i)) & 0xFF) for i in range((flag.bit_length() + 7) // 8))
flag = ascii_flag[::-1]
print(xor( flag, key))