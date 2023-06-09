#!/bin/python3
import sys
import os
import binascii
import struct

path = sys.argv[2]
if os.path.exists(path):
    os.remove(path)
else:
    print('no such file')

filepath= sys.argv[1]

f = open(path, "w")
fb = open(filepath, "rb")
databuffer = ["0","0","0","0","0","0","0","0"]

f.write("MEMORY_INITIALIZATION_RADIX=16;\n")
f.write("MEMORY_INITIALIZATION_VECTOR=\n")

size = os.path.getsize(filepath)
for i in range(int(size/4)):

  for j in range(4):
    datab = fb.read(1)
    datah = str(binascii.b2a_hex(datab))[2]
    databuffer[(3-j)*2] = datah
    datah =  str(binascii.b2a_hex(datab))[3]
    databuffer[(3-j)*2+1] = datah

  for n in range(8):
    f.write(databuffer[n])

  if i < int(size/4)-1:
    f.write(",\n")
  else :
    f.write(";\n")

fb.close()
f.close()

