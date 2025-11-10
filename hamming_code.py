def calc_parity_bits(data):
    m = len(data)
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1
    return r
def insert_parity_bits(data, r):
    j = 0
    k = 0
    res = ''
    m = len(data)
    for i in range(1, m + r + 1):
        if i == 2 ** j:
            res += '0'
            j += 1
        else:
            res += data[k]
            k += 1
    return res
def calc_parity_values(arr, r):
    n = len(arr)
    arr = list(arr)
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2 ** i) == (2 ** i):
                val ^= int(arr[-j])
        arr[-(2 ** i)] = str(val)
    return ''.join(arr)
def detect_error(received, r):
    n = len(received)
    received = list(received)
    res = 0
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2 ** i) == (2 ** i):
                val ^= int(received[-j])
        res += val * (10 ** i)
    return int(str(res)[::-1], 2)
data = input("Enter the data bits: ")[::-1]
r = calc_parity_bits(data)
arr = insert_parity_bits(data, r)
arr = calc_parity_values(arr, r)
print(f"\nGenerated Hamming Code: {arr[::-1]}")
received = list(arr)
pos = int(input("Enter error position (0 for no error): "))
if pos != 0:
    received[-pos] = '1' if received[-pos] == '0' else '0'
print(f"Received code: {''.join(received[::-1])}")
error_pos = detect_error(received, r)
if error_pos == 0:
    print("✅ No error detected.")
else:
    print(f"❌ Error detected at bit position: {error_pos}")
    received[-error_pos] = '1' if received[-error_pos] == '0' else '0'
    print(f"Corrected code: {''.join(received[::-1])}")
