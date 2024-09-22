import subprocess

binary_path = "./ai_rnd"

def get_encrypted_output(input_string):
    process = subprocess.Popen([binary_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate(input=input_string.encode())
    return stdout.decode().strip()

encrypted_flag = "a5 39 24 90 a8 a5 88 77 26 e4 3c 14 03 1e ba 3c 7d bb dc d6 aa 90 50 c9 0f aa dd 57 33 e1 a4 c7".split(" ")
print(f"Encrypted Flag: {encrypted_flag}")
flag = ["."] * 32
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz}0123456789-_$@!#{+*'
index = 0
for encrypted_char in encrypted_flag:
    for char in alphabet:
        input_string = char * 32
        encrypted_output = get_encrypted_output(input_string).split(" ")
        if encrypted_output[index] == encrypted_char:
            flag[index] = char
            index += 1
            break
print(f"Flag: {''.join(flag)}")
