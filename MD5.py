import hashlib
import time

message = input("Enter message: ")
key = input("Enter secret key: ")

data = key + message  

start = time.time()

mac = hashlib.md5(data.encode()).hexdigest()

end = time.time()

print("\n=== MD5 MAC ===")
print("MAC:", mac)
print("Time taken:", end - start, "seconds")