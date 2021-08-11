header = 0x10
value = 0x20
data = [0xA2, 0x3A, 0x45, 0x6B, 0x46]
crc = 0

for i in range (0, 5):
    crc += data[i]
    

print("{" + hex(header) + "," +  hex(value) + ",")

for i in range(0,5):
     print(hex(data[i]) + ",")
    
print(hex(crc) + ",")
print("}")
