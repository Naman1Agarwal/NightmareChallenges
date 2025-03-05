import struct
import sys

# canary, 0, 0, -, -

def num2hex(x):
    """
    Convert a double-precision floating-point number to its IEEE-754
    hexadecimal representation.

    Parameters:
      x (float): The floating-point number to convert.

    Returns:
      str: A 16-character hexadecimal string representing the binary form of x.
    """
    # Pack the float as a double ('d') in network (big-endian) order ('!')
    packed = struct.pack('!d', x)
    return packed.hex()


def hex2num(hex_str):
    """
    Convert a 16-character hexadecimal string representing an IEEE-754 double-precision
    floating-point number (in big-endian order) back into a Python float.

    Parameters:
      hex_str (str): A 16-character hexadecimal string.

    Returns:
      float: The corresponding floating-point number.
    """
    # Ensure the hex string is exactly 16 characters (8 bytes)
    if len(hex_str) != 16:
        raise ValueError("Hex string must be exactly 16 hex digits for a double.")

    # Convert the hex string to bytes
    b = bytes.fromhex(hex_str)
    # Unpack the bytes as a big-endian double ('!d') and return the number
    num = struct.unpack('!d', b)[0]
    return num


print(num2hex(-1e300))
print(num2hex(-20))
print(hex2num("c034000000000000"))
print(hex2num("b95bb400ff95a7f8"))
#print(hex2num("cee8b200ffde6718"))
#0xffde6730      0xf7e35e14      0x00000000      0xf7c24d43
#print(hex2num("f7c24d4300000000"))
#print(hex2num("f7e35e14ffde6730"))

# e84e4500ffa56158
#print(hex2num("e84e4500ffa56158"))

#print(hex2num("12c02200ffefa308"))

#print(hex2num("0804900affefa0e8"))

#print(hex2num("0804900a00000000"))

#print(hex2num("0804900affffffff"))
'''
for hexString in ["080498500804c000", "08049841ffefa308"]:
        #hexString = "58dde300ffcfe4d8"
	number = hex2num(hexString)
	hexStr = num2hex(number)
	print("number =", number)
	print("hexStr =", hexStr)
'''
