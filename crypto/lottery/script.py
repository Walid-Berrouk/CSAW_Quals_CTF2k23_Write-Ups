from pwn import * 
import random
target = remote("crypto.csaw.io", 5000)

print(target.recv())
#6, 19, 52, 21, 59, 30
target.sendline(b"35")
print(target.recv())
seed = 1
for i in range(35):
    # target.sendline(b'6')
    # target.sendline(b'19')
    # target.sendline(str(random.randint(1,70)).encode())
    # target.sendline(str(random.randint(1,70)).encode())
    # target.sendline(str(random.randint(1,70)).encode())
    # target.sendline(str(random.randint(1,70)).encode())
    target.sendline(str(seed).encode())
    target.sendline(str(seed + 1).encode())
    target.sendline(str(seed + 2).encode())
    target.sendline(str(seed + 3).encode())
    target.sendline(str(seed + 4).encode())
    target.sendline(str(seed + 5).encode())

    seed = (seed + 2) % 66

    target.recv()

print(target.recv())
print(target.recv())