from PIL import Image
from pyzbar.pyzbar import decode
img = Image.open('./qr_mosaic.bmp')
qr_width, qr_height = 2320 // 40, 1450 // 25

wordlist = []

for row in range(25):
    for col in range(40):
        left = col * qr_width
        upper = row * qr_height
        right = left + qr_width
        lower = upper + qr_height

        qr_code_img = img.crop((left, upper, right, lower))

        decoded_data = decode(qr_code_img)

        if decoded_data:
            wordlist.append(decoded_data[0].data.decode('utf-8'))

with open('./qr_wordlist.txt', 'w') as f:
    for word in wordlist:
        f.write(f"{word}\n")

print("check qr_wordlist.txt")
