import math

input_code = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,37,61,225,101,34,121,224,1001,224,-49,224,4,224,102,8,223,223,1001,224,6,224,1,224,223,223,1101,67,29,225,1,14,65,224,101,-124,224,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1102,63,20,225,1102,27,15,225,1102,18,79,224,101,-1422,224,224,4,224,102,8,223,223,1001,224,1,224,1,223,224,223,1102,20,44,225,1001,69,5,224,101,-32,224,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1102,15,10,225,1101,6,70,225,102,86,40,224,101,-2494,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,1102,25,15,225,1101,40,67,224,1001,224,-107,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,2,126,95,224,101,-1400,224,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,1002,151,84,224,101,-2100,224,224,4,224,102,8,223,223,101,6,224,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,677,677,224,1002,223,2,223,1006,224,329,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,344,101,1,223,223,8,677,677,224,1002,223,2,223,1006,224,359,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,374,101,1,223,223,7,226,677,224,1002,223,2,223,1006,224,389,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,404,1001,223,1,223,7,677,677,224,1002,223,2,223,1006,224,419,1001,223,1,223,1008,677,226,224,1002,223,2,223,1005,224,434,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,449,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,464,1001,223,1,223,1108,677,677,224,102,2,223,223,1006,224,479,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,494,1001,223,1,223,107,226,226,224,1002,223,2,223,1006,224,509,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,524,1001,223,1,223,1007,226,226,224,1002,223,2,223,1006,224,539,1001,223,1,223,107,677,677,224,1002,223,2,223,1006,224,554,1001,223,1,223,1107,226,226,224,102,2,223,223,1005,224,569,101,1,223,223,1108,677,226,224,1002,223,2,223,1006,224,584,1001,223,1,223,1007,677,226,224,1002,223,2,223,1005,224,599,101,1,223,223,107,226,677,224,102,2,223,223,1005,224,614,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,629,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,644,101,1,223,223,8,677,226,224,102,2,223,223,1006,224,659,1001,223,1,223,108,677,226,224,102,2,223,223,1005,224,674,1001,223,1,223,4,223,99,226]

parameter_modes = {
    0: 'POSITION',
    1: 'IMMEDIATE'}
opcodes = {1: 'ADD',
           2: 'MULTIPLY',
           3: 'INPUT',
           4: 'OUTPUT',
           99: 'HALT'}
cant_params = {1: 3,
               2: 3,
               3: 1,
               4: 1,
               99: 0}


def opcode(intcode):
    return intcode % 100


def mode(intcode):
    if intcode > 100:
        return math.floor(intcode/100)
    else:
        return 0


def get_params(code, instruction, paramA, paramB):
    intmode = mode(instruction)
    param1 = 0
    param2 = 0
    if intmode % 10 == 0:
        param1 = code[paramA]
    elif intmode % 10 == 1:
        param1 = paramA
    intmode = math.floor(intmode / 10)
    if cant_params[opcode(instruction)] > 1:
        if intmode % 10 == 0:
            param2 = code[paramB]
        elif intmode % 10 == 1:
            param2 = paramB
    return [param1, param2]


def process_code(code, paramA, paramB):
    output = code[:]
    ip = 0
    output[1] = paramA
    output[2] = paramB
    instruction = 0
    params = (0, 0)
    while ip < len(output):
        instruction = output[ip]
        if opcodes[opcode(instruction)] == 'ADD':
            params = get_params(output, instruction, output[ip + 1], output[ip + 2])
            output[output[ip + 3]] = params[0] + params[1]
        elif opcodes[opcode(instruction)] == 'MULTIPLY':
            params = get_params(output, instruction, output[ip + 1], output[ip + 2])
            output[output[ip + 3]] = params[0] * params[1]
        elif opcodes[opcode(instruction)] == 'INPUT':
            output[output[ip + 1]] = int(input('input: \n> '))
        elif opcodes[opcode(instruction)] == 'OUTPUT':
            print(get_params(output, instruction, output[ip + 1], 0)[0])
        elif opcodes[opcode(instruction)] == 'HALT':
            break
        ip = ip + cant_params[opcode(instruction)] + 1
    return output


def main():
    process_code(input_code, paramA=input_code[1], paramB=input_code[2])


if __name__ == '__main__':
    main()
