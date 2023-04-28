class BrainFuckInterpreter:
    def __init__(self, filename: str = None, print_end: str = ''):
        self.__cells_number: int = 30_000
        self.__memory: list[int] = [0 for _ in range(self.__cells_number)]
        self.__pointer: int = 0
        self.__printEnd: str = print_end

        self.version = 0.1

        if filename is not None:
            self.readfile(filename)

    def __check_pointer(self, new_pointer: int):
        if new_pointer > self.__cells_number-1:
            return False
        elif new_pointer < 0:
            return False
        else:
            return True

    def __process_cmd(self, cmd: str):
        match cmd:
            case '>':
                if self.__check_pointer(self.__pointer + 1):
                    self.__pointer += 1
                else:
                    print(f'the pointer went beyond the memory limit ({self.__pointer + 1} > {self.__cells_number})')
                    return False
            case '<':
                if self.__check_pointer(self.__pointer - 1):
                    self.__pointer -= 1
                else:
                    print(f'the pointer went beyond the memory limit ({self.__pointer - 1}) < 0)')
                    return False
            case '+': self.__memory[self.__pointer] += 1
            case '-': self.__memory[self.__pointer] -= 1
            case '.': print(self.__memory[self.__pointer], end=self.__printEnd)
            case '*': print(chr(self.__memory[self.__pointer]), end=self.__printEnd)
            case ',':
                try:
                    self.__memory[self.__pointer] = int(input())
                except ValueError:
                    print('no int was entered')
                    return False

            case _:
                print(f'{cmd} not brainfuck instruction')
                return False

        return True

    def __start_loop(self, instructions: str, pointer_to_check: int = -1):
        while self.__memory[pointer_to_check] != 0 or pointer_to_check == -1:
            instr_pointer: int = 0
            while instr_pointer < len(instructions):
                instruction: str = instructions[instr_pointer]
                if instruction == '[':
                    loop: str = instructions[instr_pointer+1:instructions.find(']', instr_pointer+1)]
                    self.__start_loop(loop, pointer_to_check=self.__pointer)
                    instr_pointer: int = instr_pointer + len(loop)
                else:
                    success: bool = self.__process_cmd(instruction)
                    if not success:
                        break

                instr_pointer += 1

            if pointer_to_check == -1:
                break

    def readfile(self, filename: str):
        instructions: str = ''
        with open(filename, 'rt') as file:
            for line in file:
                for char in line.strip():
                    instructions += char

        self.__start_loop(instructions)

    def readline(self, line: str):
        self.__start_loop(line)


class BFShell:
    def __init__(self):
        self.__bfi: BrainFuckInterpreter = BrainFuckInterpreter()
        self.__instr_stack: str = str()
        self.__version = 0.1

        self.main_loop()

    def main_loop(self):
        running: bool = True
        print(f"BFShell version {self.__version}\n"
              f"Brainfuck interpreter version {self.__bfi.version}\n"
              "Type '/' for commands list\n"
              "Made by Silebox")
        while running:
            ent_values: str = input('>>> ')
            for cmd in ent_values:
                match cmd:
                    case '/':
                        print(" / - commands list\n",
                              "| - execute code from instruction stack\n",
                              "~ - run another interpreter and execute code from file\n",
                              "` - clear instruction stack\n",
                              "% - get instruction stack\n",
                              "all branfuck commands - add commands to instruction stack\n",
                              "= - quit\n")
                    case '|':
                        self.__bfi.readline(self.__instr_stack)
                        self.__instr_stack: str = str()
                    case '~':
                        fname: str = input('Input filename: ')
                        BrainFuckInterpreter(fname)
                    case '`': self.__instr_stack: str = str()
                    case '=': running = False
                    case '%': print(self.__instr_stack)
                    case _: self.__instr_stack += cmd
