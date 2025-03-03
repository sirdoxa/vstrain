print(divmod(10,3)) # (x//y , x % y)
print(pow(10,3)) # x ** y
print(pow(2,3,5)) # x ** y % z
print(round(3.56564156,3)) # 3.66564156 , x-->4.x
print(abs(-55)) # -x --> +x
x = 0.25
print(dir(x))
print(x.as_integer_ratio())
x = 16
print(x.bit_count())        #0b....-->2
print(bin(x))               #0o....-->8
                            #0x....-->16 
print(x.denominator)
print(x.numerator)

x = 4 + 8j
print(x.conjugate())    # مزدوج

print(x.imag)
print(x.real)


x = 16 
print(x.to_bytes(2 , byteorder='big', signed=False))
print(x.from_bytes(b'\x00\x10' , byteorder='big'))
print(int.from_bytes(b'\x00\x10' , byteorder='big'))  # ^^^^^^^
f = 16.5
print(f.hex()) 
print(f.fromhex('0x1.0800000000000p+4'))
f = 10
print(f.is_integer())
print(bin(f))   # bin = 2
print(hex(f))   # hex = 16
print(oct(f))   # oct = 8

