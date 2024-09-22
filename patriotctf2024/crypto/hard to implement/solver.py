from pwn import *
p = remote('chal.competitivecyber.club', 6001)

line = p.recvline()
print(line.decode().strip())line = p.recvline()
print(line.decode().strip())line = p.recvline()
print(line.decode().strip())

fck this sh im not fixing this

i=11
#aes ecb orcale padding attack ok gg
p.sendline(b'a'*(i-1))
response = p.recvline()
print("SPECIAL",response)

alphanumeric = b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
for c in alphanumeric:
    print(c)
    p.sendline(b'a'*(i-1)+b"pctf{"+bytes([c]))
    response = p.recvline()
    print(response)
ffffffffffffffffffffk
p.interactive()
