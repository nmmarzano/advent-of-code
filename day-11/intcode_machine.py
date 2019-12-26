import math
from enum import Enum


class ParamMode(Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


class OpCode(Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JIT = 5
    JIF = 6
    LT = 7
    EQ = 8
    ADDOFFSET = 9
    HALT = 99


class IntcodeMachine:

    cant_params = {1: 3,
                   2: 3,
                   3: 1,
                   4: 1,
                   5: 2,
                   6: 2,
                   7: 3,
                   8: 3,
                   9: 1,
                   99: 0}

    need_input = 'NEED_INPUT'


    def __init__(self, in_queue=None, out_queue=None, code=None):
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.memory = {}
        self.__load_to_memory(code)


    def set_in_queue(self, q):
        self.in_queue = q


    def set_out_queue(self, q):
        self.out_queue = q


    def __load_to_memory(self, code):
        if code is not None:
            self.memory = {i:code[i] for i in range(len(code))}


    def __opcode(self, intcode):
        return intcode % 100


    def __mode(self, intcode):
        if intcode > 100:
            return math.floor(intcode/100)
        else:
            return 0


    def __memread(self, direction):
        value = 0
        try:
            value = self.memory[direction]
        except KeyError:
            value = 0
        return value


    def __memwrite(self, direction, value):
        self.memory[direction] = value


    def __memwrite_mode(self, mode, direction, relative_base, value):
        if mode == ParamMode.POSITION.value:
            self.__memwrite(self.__memread(direction), value)
        elif mode == ParamMode.IMMEDIATE.value:
            params.append(self.__memread(ip + offset))
            self.__memwrite(direction, value)
        elif mode == ParamMode.RELATIVE.value:
            self.__memwrite(self.__memread(direction) + relative_base, value)


    def __memread_mode(self, mode, direction, relative_base):
        if mode == ParamMode.POSITION.value:
            return self.__memread(self.__memread(direction))
        elif mode == ParamMode.IMMEDIATE.value:
            return self.__memread(direction)
        elif mode == ParamMode.RELATIVE.value:
            return self.__memread(self.__memread(direction) + relative_base)


    def __get_params(self, ip, relative_base):
        instruction = self.__memread(ip)
        intmode = self.__mode(instruction)
        params = []
        for offset in range(1, self.__class__.cant_params[self.__opcode(instruction)]+1):
            params.append(
                self.__memread_mode(
                    intmode % 10,
                    ip + offset,
                    relative_base))
            intmode = math.floor(intmode / 10)
        return params


    def __get_writemode(self, instruction):
        return math.floor(self.__mode(instruction)
                          / 10**(self.__class__.cant_params[self.__opcode(instruction)]-1))


    def compute(self):
        ip = 0
        instruction = 0
        params = ()
        relative_base = 0
        while ip < len(self.memory):
            instruction = self.__memread(ip)
            operation = self.__opcode(instruction)
            params = self.__get_params(ip, relative_base)
            writemode = self.__get_writemode(instruction)
            if operation == OpCode.ADD.value:
                self.__memwrite_mode(writemode, ip + 3, relative_base, params[0] + params[1])
            elif operation == OpCode.MULTIPLY.value:
                self.__memwrite_mode(writemode, ip + 3, relative_base, params[0] * params[1])
            elif operation == OpCode.INPUT.value:
                self.out_queue.put(self.__class__.need_input)
                self.__memwrite_mode(writemode, ip + 1, relative_base, self.in_queue.get())
            elif operation == OpCode.OUTPUT.value:
                self.out_queue.put(params[0])
            elif operation == OpCode.JIT.value:
                if params[0] != 0:
                    ip = params[1]
                    continue
            elif operation == OpCode.JIF.value:
                if params[0] == 0:
                    ip = params[1]
                    continue
            elif operation == OpCode.LT.value:
                if params[0] < params[1]:
                    self.__memwrite_mode(writemode, ip + 3, relative_base, 1)
                else:
                    self.__memwrite_mode(writemode, ip + 3, relative_base, 0)
            elif operation == OpCode.EQ.value:
                if params[0] == params[1]:
                    self.__memwrite_mode(writemode, ip + 3, relative_base, 1)
                else:
                    self.__memwrite_mode(writemode, ip + 3, relative_base, 0)
            elif operation == OpCode.ADDOFFSET.value:
                relative_base += params[0]
            elif operation == OpCode.HALT.value:
                break
            ip += self.__class__.cant_params[self.__opcode(instruction)] + 1


if __name__ == '__main__':
    print('This is a module, import it into your code.\n')
