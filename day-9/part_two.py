import math, threading, queue
from enum import Enum


input_code = [1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1102,3,1,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1102,1,38,1003,1102,24,1,1008,1102,1,29,1009,1102,873,1,1026,1102,1,32,1015,1102,1,1,1021,1101,0,852,1023,1102,1,21,1006,1101,35,0,1018,1102,1,22,1019,1102,839,1,1028,1102,1,834,1029,1101,0,36,1012,1101,0,31,1011,1102,23,1,1000,1101,405,0,1024,1101,33,0,1013,1101,870,0,1027,1101,0,26,1005,1101,30,0,1004,1102,1,39,1007,1101,0,28,1017,1101,34,0,1001,1102,37,1,1014,1101,20,0,1002,1102,1,0,1020,1101,0,859,1022,1102,1,27,1016,1101,400,0,1025,1102,1,25,1010,109,-6,1207,10,29,63,1005,63,201,1001,64,1,64,1105,1,203,4,187,1002,64,2,64,109,3,2107,25,8,63,1005,63,221,4,209,1106,0,225,1001,64,1,64,1002,64,2,64,109,-4,2101,0,9,63,1008,63,18,63,1005,63,245,1106,0,251,4,231,1001,64,1,64,1002,64,2,64,109,3,2108,38,7,63,1005,63,273,4,257,1001,64,1,64,1106,0,273,1002,64,2,64,109,22,21102,40,1,0,1008,1018,40,63,1005,63,299,4,279,1001,64,1,64,1106,0,299,1002,64,2,64,109,-16,21108,41,41,10,1005,1012,321,4,305,1001,64,1,64,1105,1,321,1002,64,2,64,109,6,2102,1,-2,63,1008,63,22,63,1005,63,341,1105,1,347,4,327,1001,64,1,64,1002,64,2,64,109,21,1206,-8,359,1106,0,365,4,353,1001,64,1,64,1002,64,2,64,109,-7,21101,42,0,-6,1008,1016,44,63,1005,63,389,1001,64,1,64,1105,1,391,4,371,1002,64,2,64,109,2,2105,1,0,4,397,1106,0,409,1001,64,1,64,1002,64,2,64,109,-3,1205,0,427,4,415,1001,64,1,64,1105,1,427,1002,64,2,64,109,-13,2102,1,-1,63,1008,63,39,63,1005,63,449,4,433,1106,0,453,1001,64,1,64,1002,64,2,64,109,-10,1202,4,1,63,1008,63,20,63,1005,63,479,4,459,1001,64,1,64,1106,0,479,1002,64,2,64,109,7,2108,37,-2,63,1005,63,495,1105,1,501,4,485,1001,64,1,64,1002,64,2,64,109,4,21101,43,0,1,1008,1010,43,63,1005,63,523,4,507,1106,0,527,1001,64,1,64,1002,64,2,64,109,-4,1208,-5,23,63,1005,63,549,4,533,1001,64,1,64,1106,0,549,1002,64,2,64,109,-4,1208,7,27,63,1005,63,565,1106,0,571,4,555,1001,64,1,64,1002,64,2,64,109,15,1205,4,587,1001,64,1,64,1106,0,589,4,577,1002,64,2,64,109,-7,1202,-7,1,63,1008,63,18,63,1005,63,613,1001,64,1,64,1106,0,615,4,595,1002,64,2,64,109,5,21107,44,43,1,1005,1015,635,1001,64,1,64,1105,1,637,4,621,1002,64,2,64,109,-2,21102,45,1,6,1008,1018,44,63,1005,63,661,1001,64,1,64,1105,1,663,4,643,1002,64,2,64,109,-18,1207,6,24,63,1005,63,685,4,669,1001,64,1,64,1105,1,685,1002,64,2,64,109,4,2101,0,8,63,1008,63,21,63,1005,63,707,4,691,1105,1,711,1001,64,1,64,1002,64,2,64,109,17,1206,5,725,4,717,1105,1,729,1001,64,1,64,1002,64,2,64,109,9,21107,46,47,-9,1005,1015,751,4,735,1001,64,1,64,1106,0,751,1002,64,2,64,109,-9,1201,-6,0,63,1008,63,26,63,1005,63,775,1001,64,1,64,1106,0,777,4,757,1002,64,2,64,109,-15,1201,0,0,63,1008,63,23,63,1005,63,803,4,783,1001,64,1,64,1105,1,803,1002,64,2,64,109,-1,2107,30,10,63,1005,63,819,1106,0,825,4,809,1001,64,1,64,1002,64,2,64,109,24,2106,0,5,4,831,1105,1,843,1001,64,1,64,1002,64,2,64,109,-5,2105,1,5,1001,64,1,64,1105,1,861,4,849,1002,64,2,64,109,14,2106,0,-5,1105,1,879,4,867,1001,64,1,64,1002,64,2,64,109,-17,21108,47,44,4,1005,1019,899,1001,64,1,64,1105,1,901,4,885,4,64,99,21101,0,27,1,21102,915,1,0,1106,0,922,21201,1,58969,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21101,0,942,0,1105,1,922,22102,1,1,-1,21201,-2,-3,1,21101,957,0,0,1106,0,922,22201,1,-1,-2,1106,0,968,21201,-2,0,-2,109,-3,2105,1,0]

input_queue = queue.Queue()

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


def opcode(intcode):
    return intcode % 100


def mode(intcode):
    if intcode > 100:
        return math.floor(intcode/100)
    else:
        return 0


def memread(memory, direction):
    value = 0
    try:
        value = memory[direction]
    except KeyError:
        value = 0
    return value


def memwrite(memory, direction, value):
    memory[direction] = value


def memwrite_mode(memory, mode, direction, relative_base, value):
    if mode == ParamMode.POSITION.value:
        memwrite(memory, memread(memory, direction), value)
    elif mode == ParamMode.IMMEDIATE.value:
        params.append(memread(memory, ip + offset))
        memwrite(memory, direction, value)
    elif mode == ParamMode.RELATIVE.value:
        memwrite(memory, memread(memory, direction) + relative_base, value)


def memread_mode(memory, mode, direction, relative_base):
    if mode == ParamMode.POSITION.value:
        return memread(memory, memread(memory, direction))
    elif mode == ParamMode.IMMEDIATE.value:
        return memread(memory, direction)
    elif mode == ParamMode.RELATIVE.value:
        return memread(memory, memread(memory, direction) + relative_base)


def get_params(memory, ip, relative_base):
    instruction = memread(memory, ip)
    intmode = mode(instruction)
    params = []
    for offset in range(1, cant_params[opcode(instruction)]+1):
        params.append(
            memread_mode(
                memory,
                intmode % 10,
                ip + offset,
                relative_base))
        intmode = math.floor(intmode / 10)
    return params


def get_writemode(instruction):
    return math.floor(mode(instruction)
                      / 10**(cant_params[opcode(instruction)]-1))


def threaded_compute(memory, in_queue, out_queue):
    ip = 0
    instruction = 0
    params = ()
    relative_base = 0
    while ip < len(memory):
        instruction = memread(memory, ip)
        operation = opcode(instruction)
        params = get_params(memory, ip, relative_base)
        writemode = get_writemode(instruction)
        if operation == OpCode.ADD.value:
            memwrite_mode(memory, writemode, ip + 3, relative_base, params[0] + params[1])
        elif operation == OpCode.MULTIPLY.value:
            memwrite_mode(memory, writemode, ip + 3, relative_base, params[0] * params[1])
        elif operation == OpCode.INPUT.value:
            memwrite_mode(memory, writemode, ip + 1, relative_base, in_queue.get())
        elif operation == OpCode.OUTPUT.value:
            out_queue.put(params[0])
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
                memwrite_mode(memory, writemode, ip + 3, relative_base, 1)
            else:
                memwrite_mode(memory, writemode, ip + 3, relative_base, 0)
        elif operation == OpCode.EQ.value:
            if params[0] == params[1]:
                memwrite_mode(memory, writemode, ip + 3, relative_base, 1)
            else:
                memwrite_mode(memory, writemode, ip + 3, relative_base, 0)
        elif operation == OpCode.ADDOFFSET.value:
            relative_base += params[0]
        elif operation == OpCode.HALT.value:
            break
        ip += cant_params[opcode(instruction)] + 1


def load_to_memory(code):
    memory = {i:code[i] for i in range(len(code))}
    return memory


def process_code(code, inputs):
    outputs = []
    memory = load_to_memory(code)
    output_queue = queue.Queue()
    processor = threading.Thread(
                target = threaded_compute,
                args = (memory, input_queue, output_queue),
                daemon = True)
    processor.start()
    for value in inputs:
        input_queue.put(value)
    processor.join()
    while not output_queue.empty():
        outputs.append(output_queue.get())
    return outputs


def main():
    print(process_code(input_code, [1]))


if __name__ == '__main__':
    main()
