# -*- coding: utf-8 -*-
# @Time    : 2017/10/16 10:33
# @Author  : Sean
# @File    : 5_2_BinaryFile.py

import struct
import array

f = open('beat.wav', 'rb')
info = f.read(44)
# NumChannels
print(struct.unpack('h', info[22:24]))
# SampleRate
print(struct.unpack('i', info[24:28]))
# BitPerSample
print(struct.unpack('h', info[34:36]))

# point to end of file
f.seek(0, 2)
n = (f.tell() - 44) / 2
buff = array.array('h', (0 for _ in range(int(n))))
f.seek(44)
f.readinto(buff)
for i in range(int(n)):
    buff[i] = int(buff[i] / 8)
f.close()

f2 = open('beat2.wav', 'wb')
f2.write(info)
buff.tofile(f2)
f2.close()