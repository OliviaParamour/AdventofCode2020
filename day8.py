def load(file_name: str) -> list:
    """Loads and parses the input for use in the challenge."""
    input = []
    with open(file_name) as file:
        for line in file:
            instruction = line.strip().split()

            input.append({
                "opcode":instruction[0],
                "value": int(instruction[1])
                })
    return input

def run(program: list) -> tuple:
    """runs program until it loops or reaches end of file."""
    step = 0
    acc = 0
    instructions = []
    while True:
        if step not in instructions and step < len(program):
            instructions.append(step)
            current = program[step]
            if current["opcode"] == "acc":
                acc += current["value"]
            if current["opcode"] == "jmp":
                step += current["value"]
            else:
                step += 1
        else:
            instructions.append(step)
            return acc, instructions

def find_fault(program: list, executed_instructions: list) -> tuple:
    """iterates through all executed instructions to test and find the fault"""
    program_end = False
    modified_program = program.copy()
    for i in executed_instructions: 
        opcode = modified_program[i]["opcode"]
        if opcode != "acc": 
            opcode = switch_opcode(opcode)
            modified_program[i].update({"opcode": opcode})
            acc, instructions = run(modified_program)
            if instructions[-1] >= len(program):
                return acc, i
            modified_program[i].update({"opcode": switch_opcode(opcode)})
    return None, None

def switch_opcode(opcode: str) -> str:
    if opcode == "jmp":
        return "nop"
    elif opcode == "nop":
        return "jmp"
    else:
        return opcode


def main() -> None:
    """The main function for day 8. Answers Question 1 and 2."""
    program = load("day8.txt")
    acc, instructions = run(program)
    acc2, instruction = find_fault(program, instructions)
    
    print(f"Total number of inputs: {len(program)}")
    print(f"value in accumulator when looping: {acc}")
    print(f"Corrupted instruction: {instruction}")
    print(f"value in accumulator when fixed: {acc2}")
    # [print(input) for input in program]

if __name__ == "__main__":
    main()