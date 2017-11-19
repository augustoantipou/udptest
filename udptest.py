# X-Plane 10 data transfer via UDP protocol
# 2017/11/18 - Augusto Antipou

# Imports the socket library.
from socket import *

import struct

# X-Plane IP address and port
address = ('127.0.0.1', 49001) # ('IP of the machine running XP', default comm port)

# We have a socket, we need an address family.
# In this case we will use IPv4 with the AF_INET parameter.
# We define our protocol:
# TCP = SOCK_STREAM
# UDP = SOCK_DGRAM
server_socket = socket(AF_INET, SOCK_DGRAM)

# We finish it binding the socket with the X-Plane address.
server_socket.bind(address)

# This will execute forever. (Ctrl+C to stop it).

# If we receive anything:
while True:
	# We read and send the data to recv_data.
	recv_data, address = server_socket.recvfrom(512)

	# We extract the pitch value from byte no. 9 to 13.
	pitch_degrees = struct.unpack('f', recv_data[9:13])

	# Print the pitch value.
	print 'Pitch degrees: %.2f' % pitch_degrees

# How it works:
#
# X-Plane data packet:
#
# 68 65 84 65 64 | 17 0 0 0 | 187 207 141 65 | 8 104 41 62 | 143 124 220 66 | 38 196 5 67 | 0 192 121 196 | 0 192 121 196 | 0 192 121 196 | 0 192 121 196
#
# Each value corresponds to a byte, the first 5 bytes define the heading of the data, the values 68:65:84:65 are equal to the text "DATA",
# we have other headings such as DREF, CHAR, MOUS, etc.
# The heading we are looking for is "DATA", after that we need an index, in this case the '17'. Remember we choose the parameter 17 at "Data Input & Output".
# Following we have three zeros, they will always be zeros.
# After that we have 32 bytes, divided into groups of 4 bytes. This equals to 8 values in floating point (simple precision).
# If we look at the order the data is sent we can see we have the sequence of pitch, roll, heading (true) and heading (mag).
# We have four more empty spaces, that is, in parameter 17 we have only 4 datas.
# In our byte sequence, after the heading, those 4 bytes correspond to pitch, that's why we send them to the struct.unpack method, which returns the byte values
# as simple precision floating point (32 bits).