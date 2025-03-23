
class Parser():
    def __init__(self, RAM, addr=0):
        self.RAM = RAM
        self.addr = addr

        self.memory_ref = {"AND": 0, "ADD": 1, "LDA": 2, "STA": 3, "BUN": 4, "BSA": 5, "ISZ": 6}
        self.register_ref = {"CLA": "7800", "CMA": "7200", "INC": "7020"}
        self.io_ref = {"INP": "F800", "OUT": "F400"}

    def strip_comments(self, line):
        """Strip comments from the line"""
        return line.strip().split("#")[0]

    def parse_content(self, content):
        """Parsing the content"""
        count = 0
        for line in content:
            line = self.strip_comments(line)
            print(count, end=": ")
            print(line)
            count+=1
            if line == "":
                continue
            elif line[0] == ".":
                command = self.parse_directive(line.split())
            else:
                command = self.parse_instruction(line.split())

            if command != None:
                self.RAM[self.addr] = command
                self.addr += 1
        
        return self.RAM

    def parse_directive(self, args):
        """Parse the directive"""
        cmd = args[0]
        addr = args[1]
        if cmd == ".org":
            self.addr = int(addr, 16)
        elif cmd == ".data":
            self.RAM[self.addr] = addr[2:]
            self.addr+=1

    def parse_instruction(self, args):
        """Parse the instruction"""

        # Don't forget to update the lists in __init__ when adding a new command

        instruction = args[0]
        if instruction in self.memory_ref:
            command = self.parse_memory_ref(args)
        elif instruction in self.register_ref:
            command = self.parse_register_ref(args)
        elif instruction in self.io_ref:
            command = self.parse_io_ref(args)

        return command

    def parse_memory_ref(self, args):
        """Parse memory reference instructions"""
        cmd = args[0]
        command = "" # Final command

        if "@" in args[1]:
            command += str( hex(self.memory_ref[cmd] + 8 )[2:] )
            addr = args[1].split("@")[1][2:]
        else:
            command += str( self.memory_ref[cmd] )
            addr = args[1][2:]

        command += addr
        return command

    def parse_register_ref(self, args):
        """Parse register reference instructions"""
        cmd = args[0]
        command = self.register_ref[cmd]
        return command

    def parse_io_ref(self, args):
        """Parse IO reference instructions"""
        cmd = args[0]
        command = self.io_ref[cmd]
        return command

