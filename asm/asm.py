#!/usr/bin/python3
import sys
from parser import Parser
import ipdb


# Expect an arguemnt with the filename
filename = sys.argv[1]

def check_if_file_exists_and_load_content(filename):
    """Trying to open and read the file"""
    try:
        with open(filename, "r") as f:
            content = f.readlines()
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)
    return content

def save_to_ram(RAM, filename):
    """Saving it to a file"""
    output_file = filename.split(".")[0] + ".out"
    with open(output_file, "w") as f:
        f.write("v3.0 hex words addressed\n")
        for addr in range(0, 4096, 16):
            line = [f"{(RAM[addr + i])}" for i in range(16)]
            f.write(f"{addr:03x}: {' '.join(line)}\n")

def main():
    # Check if the file exists and load the content
    content = check_if_file_exists_and_load_content(filename)

    # Initialize the RAM contents
    RAM = ["0000"] * 4096

    # Parsing the file
    parser = Parser(RAM)
    RAM = parser.parse_content(content)
    print(RAM[:105])

    # Save the RAM contents to a file
    save_to_ram(RAM, filename)

if __name__ == "__main__":
    main()
