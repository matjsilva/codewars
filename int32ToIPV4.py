# int32_to_ip(2154959208), "128.114.17.104"
# int32_to_ip(2149583361), "128.32.10.1"

# o que eu penso que pode ser: int32 => bin -> bin separado em 4 bytes -> byte pra int (*4)
import socket, struct

def int32_to_ip(int32):
    return socket.inet_ntoa(struct.pack('!L', int32))

# ipList = []

# if len(str(int32)) >= 9:
#     splitBin = textwrap.wrap(str(bin(int32)[2:]), 8)
# else:
#     return f"{str(int32)}.{str(int32)}.{str(int32)}.{str(int32)}"
# for byte in splitBin:
#     byte = int(byte, 2)
#     ipList.append(str(byte))

# return ".".join(ipList) 

print(int32_to_ip(2154959208))

