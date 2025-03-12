
# str 1-رشته های معمولی (اسکی و یونیکد) 
#     encoding-decoding-ascii-unicode
x = 'p'
print(ord(x))
print(chr(112))
# bytes 2-داده های باینری
s = b'r'
#or
s = bytes('r','utf-8')
print(type(s))
# byte-array 3-داده های باینری
p = bytearray('m','utf-8')
print(type(p))

c = bytes('rezæ','utf-8')
print(c)
print(c.decode('utf-8'))
print(c[0])     #binary!!!!!!!!!
print(0x72) 
print('\x72\x65\x7a\xc3\xa6')
print(type(c))
# -------------------------------------------------
x = bytes([1,7,9,56,120])
print(chr(x[4]))
print(hex(56))
print(x)
# x[0] = 152          # error because bytes is immutable but bytes-array is mutable
# -------------------------------------------------

x = bytearray('mahdi','utf-8')
x[1] = 126
print(x)
# -------------------------------------------------
x = bytes('mahdi§','ascii','ignore')
print(x)
x = bytes('mahdi§','ascii','replace')
print(x)
x = bytes('mahdi§','ascii','backslashreplace')
print(x)
x = bytes('mahdi§','ascii','namereplace')
print(x)
# x = bytes('mahdi§','ascii','strict')      #cause error
# print(x)
# -------------------------------------------------
print((32).to_bytes(4,'big'))
print('\x20')
