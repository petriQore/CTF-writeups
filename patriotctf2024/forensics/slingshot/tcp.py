from datetime import datetime
import math

# from the pcapcng
with open("./data1") as f:
    lines1 = "".join([line.strip() for line in f.readlines()])
with open("./data2") as f:
    lines2 = "".join([line.strip() for line in f.readlines()])
with open("./data3") as f:
    lines3 = "".join([line.strip() for line in f.readlines()])

total_hex = lines1 + lines2 + lines3
encrypted_bytes = bytes.fromhex(total_hex)

current_time = "2024-09-17 17:56:09"
time_object = datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")
current_time = time_object.timestamp()
current_time = math.floor(current_time)
current_time = 1726595769
print(f"(timestamp): {current_time}")

key_bytes = str(current_time).encode('utf-8')
init_key_len = len(key_bytes)
data_bytes_len = len(encrypted_bytes)
temp1 = data_bytes_len // init_key_len
temp2 = data_bytes_len % init_key_len

key_bytes *= temp1
key_bytes += key_bytes[:temp2]

decrypted_bytes = bytes(a ^ b for a, b in zip(key_bytes, encrypted_bytes))
image_filename = 'decrypted_image.jpg'

with open(image_filename, 'wb') as f:
    f.write(decrypted_bytes)
#print(decrypted_bytes)

print("gg check imagee")
