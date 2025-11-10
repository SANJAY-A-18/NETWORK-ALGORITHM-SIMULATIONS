def xor(a, b):
    result = []
    for i in range(1, len(b)):
        result.append('0' if a[i] == b[i] else '1')
    return ''.join(result)
def crc_division(data, key):
    pick = len(key)
    tmp = data[0:pick]
    while pick < len(data):
        if tmp[0] == '1':
            tmp = xor(key, tmp) + data[pick]
        else:
            tmp = xor('0' * pick, tmp) + data[pick]
        pick += 1
    if tmp[0] == '1':
        tmp = xor(key, tmp)
    else:
        tmp = xor('0' * pick, tmp)
    return tmp
data = input("Enter data bits: ")
key = input("Enter generator polynomial: ")
l_key = len(key)
appended_data = data + '0' * (l_key - 1)
remainder = crc_division(appended_data, key)
transmitted = data + remainder
print(f"\nTransmitted Frame: {transmitted}")
received = input("\nEnter received frame: ")
rem = crc_division(received, key)
if '1' not in rem:
    print("✅ No Error Detected (Remainder = 0)")
else:
    print("❌ Error Detected (Remainder != 0)")

