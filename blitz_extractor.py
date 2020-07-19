#Key extractor for game based on Blitz3D engine like Turtle, Maluch Racer v2, Czeski Rajd etc...

#pip install lief
import lief
import re
import struct
import sys

if len(sys.argv) != 2:
    print("Usage: python extractor.py <file>")
    exit()

print("Opening file...")
binary = lief.parse(sys.argv[1])

if not binary:
    print("Couldnt find or parse the binary", sys.argv[1], "aborted...")
    exit()

if not binary.has_resources:
    print("No resources found in this binary. Couldn't extract the key. Aborted")
    exit()
    
print("Browsing resources...")
content = None
for child in binary.resources.childs:
    for child_next in child.childs:
        if child_next.id == 1111:
            content = bytes(child_next.childs[0].content)
            print("Found resource with id 1111...")
            
if not content:
    print("Couldn't find resource with id 1111... Aborted")
    exit()
    
print("Looking for pattern...")
"""
MOV        dword ptr [ESP + 0x8],EAX
MOV        dword ptr [ESP + 0xc],HEADER_KEY
MOV        dword ptr [ESP + 0x4],MAIN_KEY
SUB        ESP,0x4
"""
p = re.compile(b"\\x89\\x44\\x24\\x08\\xC7\\x44\\x24\\x0C(.{4})\\xC7\\x44\\x24\\x04(.{4})\\x81")
results = p.search(content)
if len(results.groups()) < 2:
    print("Couldn't find the pattern in resource... Aborted")
    exit()
    
elif len(results.groups()) != 2:
    print("WARNING: Found more then two matches, key might be invalid")
    
print("OK! Extracted keys:\n\n")
header_key, main_key = struct.unpack("<II", results.groups()[0] + results.groups()[1])

print("Header key:\t", hex(header_key))
print("Main key:\t",  hex(main_key)) 