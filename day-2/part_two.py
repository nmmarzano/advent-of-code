input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,19,
         5,23,2,6,23,27,1,6,27,31,2,31,9,35,1,35,6,39,1,
         10,39,43,2,9,43,47,1,5,47,51,2,51,6,55,1,5,55,
         59,2,13,59,63,1,63,5,67,2,67,13,71,1,71,9,75,1,
         75,6,79,2,79,6,83,1,83,5,87,2,87,9,91,2,9,91,95,
         1,5,95,99,2,99,13,103,1,103,5,107,1,2,107,111,1,
         111,5,0,99,2,14,0,0]
wanted_output = 19690720


def process_code(code, paramA, paramB):
    output = code[:]
    ip = 0
    acc = 0
    output[1] = paramA
    output[2] = paramB
    while ip < len(output):
        if output[ip] == 1:
            acc = output[output[ip + 1]] + output[output[ip + 2]]
            output[output[ip + 3]] = acc
            ip = ip + 4
        elif output[ip] == 2:
            acc = output[output[ip + 1]] * output[output[ip + 2]]
            output[output[ip + 3]] = acc
            ip = ip + 4
        elif output[ip] == 99:
            break
    return output


def find_inputs(code, output):
    found = False
    for x in range(min(len(code), 100)):
        for y in range(min(len(code), 100)):
            test = process_code(code, paramA=x, paramB=y)
            if test[0] == output:
                found = True
                break
        if found:
            break
    return (found, x, y)


def main():
    (found, noun, verb) = find_inputs(input, wanted_output)
    if found:
        print(100 * noun + verb)
    else:
        print("inputs not found")


if __name__ == "__main__":
    main()
