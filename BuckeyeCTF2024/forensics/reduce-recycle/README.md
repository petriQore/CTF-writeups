wow good task  
ok so we have 1 zip and 1 7z each containing 4 pngs and 1 flag.txt respectively  

examining the zip file closely, we can see the encryption method used is ZipCrypto Store which is known to be broken  

the only condition is that we know at least 12 bytes of the original archived files (the equivalent of a plaintext in a plaintext attack), 8 of those being contiguous.  

fortunately we know that the archived files are PNGs, we can use that to our advantage, because PNG files always include a header (89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49) that is fortunately bigger than 12 bytes  

note that we could have managed even with only 11 bytes, because there is an extra "check" byte or whatever its called... just google it idk  

so now we can get to cracking the zip, first let's make a file containing the header:  
```
echo "89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49" | xxd -r -p > plain.bin

```
we also have to use a tool called bkcrack  
```
./bkcrack -C ../dogs_wearing_tools.zip -c 1.png -p test.bin
```
this gives us a key back:  
```
bkcrack 1.7.0 - 2024-05-26
[20:05:59] Z reduction using 5 bytes of known plaintext
100.0 % (5 / 5)
[20:05:59] Attack on 1190986 Z values at index 6
Keys: adf73413 6f6130e7 0cfbc537
7.7 % (91746 / 1190986)
Found a solution. Stopping.
You may resume the attack with the option: --continue-attack 91746
[20:07:00] Keys
adf73413 6f6130e7 0cfbc537
```
we can now use that key to make a new zip file that is unprotected:  
``` 
./bkcrack -C ../dogs_wearing_tools.zip -k adf73413 6f6130e7 0cfbc537 -D dogs_clean.zip
bkcrack 1.7.0 - 2024-05-26
[20:08:37] Writing decrypted archive dogs_clean.zip
100.0 % (4 / 4)
```
the files didn't have anything interesting inside, then i remembered that the goal was to get the password so we can unlock the 7z file  
so our next move is bruteforcing, thankfully we know the password length is 12:
``` 
./bkcrack -k adf73413 6f6130e7 0cfbc537 --bruteforce ?a --length 12
bkcrack 1.7.0 - 2024-05-26
[20:09:43] Recovering password
length 12...
Password: 2n3Ad3&ZxDvV (as bytes: 32 6e 33 41 64 33 26 5a 78 44 76 56)
Some characters are not in the expected charset. Continuing.
100.0 % (3844 / 3844)
[20:09:47] Could not recover password
```
it says Could not recover password but the password is right there lol "2n3Ad3&ZxDvV"  

that's it now you can go ahead and unlock the 7z