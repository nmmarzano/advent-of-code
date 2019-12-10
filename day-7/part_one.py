import math


input_code = [3,8,1001,8,10,8,105,1,0,0,21,42,63,76,101,114,195,276,357,438,99999,3,9,101,2,9,9,102,5,9,9,1001,9,3,9,1002,9,5,9,4,9,99,3,9,101,4,9,9,102,5,9,9,1001,9,5,9,102,2,9,9,4,9,99,3,9,1001,9,3,9,1002,9,5,9,4,9,99,3,9,1002,9,2,9,101,5,9,9,102,3,9,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,3,9,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99]


parameter_modes = {
    0: 'POSITION',
    1:'IMMEDIATE'}
opcodes = {1: 'ADD',
           2: 'MULTIPLY',
           3: 'INPUT',
           4: 'OUTPUT',
           5: 'JIT',
           6: 'JIF',
           7: 'LT',
           8: 'EQ',
           99: 'HALT'}
cant_params = {1: 3,
               2: 3,
               3: 1,
               4: 1,
               5: 2,
               6: 2,
               7: 3,
               8: 3,
               99: 0}


def opcode(intcode):
    return intcode % 100


def mode(intcode):
    if intcode > 100:
        return math.floor(intcode/100)
    else:
        return 0


def get_params(code, ip):
    instruction = code[ip]
    intmode = mode(instruction)
    params = []
    for offset in range(1, cant_params[opcode(instruction)]+1):
        if parameter_modes[intmode % 10] == 'POSITION':
            params.append(code[code[ip + offset]])
        elif parameter_modes[intmode % 10] == 'IMMEDIATE':
            params.append(code[ip + offset])
        intmode = math.floor(intmode / 10)
    return params


def process_code(code, inputs):
    output = code[:]
    last_output = -99
    ip = 0
    instruction = 0
    params = (0, 0)
    input_index = 0
    while ip < len(output):
        instruction = output[ip]
        operation = opcodes[opcode(instruction)]
        if operation == 'ADD':
            params = get_params(output, ip)
            output[output[ip + 3]] = params[0] + params[1]
        elif operation == 'MULTIPLY':
            params = get_params(output, ip)
            output[output[ip + 3]] = params[0] * params[1]
        elif operation == 'INPUT':
            output[output[ip + 1]] = inputs[input_index]
            input_index += 1
        elif operation == 'OUTPUT':
            params = get_params(output, ip)
            last_output = params[0]
        elif operation == 'JIT':
            params = get_params(output, ip)
            if params[0] != 0:
                ip = params[1]
                continue
        elif operation == 'JIF':
            params = get_params(output, ip)
            if params[0] == 0:
                ip = params[1]
                continue
        elif operation == 'LT':
            params = get_params(output, ip)
            if params[0] < params[1]:
                output[output[ip + 3]] = 1
            else:
                output[output[ip + 3]] = 0
        elif operation == 'EQ':
            params = get_params(output, ip)
            if params[0] == params[1]:
                output[output[ip + 3]] = 1
            else:
                output[output[ip + 3]] = 0
        elif operation == 'HALT':
            break
        ip += cant_params[opcode(instruction)] + 1
    return last_output


def amplifier_combinations():
    combinations = []
    num_set = set(())
    for i in range(5):
        for j in range(5):
            for k in range(5):
                for l in range(5):
                    for m in range(5):
                        combination = [i,j,k,l,m]
                        num_set.update(combination)
                        if len(num_set) == 5:
                            combinations.append(combination)
                        num_set = set(())
    return combinations


def process_code_multiple(code, multiple_inputs, signal):
    outputs = []
    output = signal
    for inputs in multiple_inputs:
        for value in inputs:
            output = process_code(code, [value, output])
        outputs.append(output)
        output = signal
    return outputs


def main():
    print(max(process_code_multiple(input_code, amplifier_combinations(), 0)))


if __name__ == '__main__':
    main()
