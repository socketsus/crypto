import hashlib
import time

message = input("Enter message: ")
key = input("Enter secret key: ")

data = key + message

start = time.time()

mac1 = hashlib.md5(data.encode()).hexdigest()

if len(message) > 0:
    modified_message = message[:-1] + chr((ord(message[-1]) + 1) % 256)
else:
    modified_message = "a"

data2 = key + modified_message
mac2 = hashlib.md5(data2.encode()).hexdigest()

end = time.time()

bin1 = bin(int(mac1, 16))[2:].zfill(128)
bin2 = bin(int(mac2, 16))[2:].zfill(128)

changed_bits = sum(b1 != b2 for b1, b2 in zip(bin1, bin2))
avalanche_percent = (changed_bits / 128) * 100

print("\n=== MD5 MAC ===")
print("Original MAC :", mac1)
print("Modified MAC :", mac2)
print("Time taken:", end - start, "seconds")

print("\n=== Avalanche Effect ===")
print("Changed bits:", changed_bits, "/ 128")
print("Avalanche Effect: {:.2f}%".format(avalanche_percent))
