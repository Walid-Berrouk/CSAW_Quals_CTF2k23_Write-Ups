#! /usr/bin/python3


from pwn import *

HOST = 'misc.csaw.io'
PORT = 3000

lst = []

# Extract from a0 to a29
for i in range(26, 30):
    p = remote(HOST, PORT)

    for j in range(30):
        if j == i:
            p.sendlineafter(b'Enter your input: \r\n', b'1')
        else:
            p.sendlineafter(b'Enter your input: \r\n', b'0')
    print(f"Sent {i}!")

    p.recvline()
    lst.append(p.recvline())
    print(lst)
    p.close()


# Extract b
p = remote(HOST, PORT)

for j in range(30):
    p.sendlineafter(b'Enter your input: \r\n', b'0')
print(f"Sent 30!")

p.recvline()
lst.append(p.recvline())
print(lst)
p.close()

# Construct Flag
# lst = [b'224\r\n', b'240\r\n', b'222\r\n', b'244\r\n', b'224\r\n', b'241\r\n', b'227\r\n', b'248\r\n', b'234\r\n', b'173\r\n', b'225\r\n', b'176\r\n', b'174\r\n', b'220\r\n', b'178\r\n', b'241\r\n', b'176\r\n', b'177\r\n', b'174\r\n', b'230\r\n', b'235\r\n', b'228\r\n', b'220\r\n', b'230\r\n', b'178\r\n', b'220\r\n', b'223\r\n', b'177\r\n', b'225\r\n', b'250\r\n', b'125\r\n']

newlst = [int(l.strip()) for l in lst]
flag_chars = [chr(c - newlst[-1]) for c in newlst]

flag = ''.join(flag_chars)

print(flag)