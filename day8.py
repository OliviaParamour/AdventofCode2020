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
    accumulator = 0
    instructions = []
    while True:
        if step not in instructions and step < len(program):
            instructions.append(step)
            current = program[step]
            if current["opcode"] == "acc":
                accumulator += current["value"]
            if current["opcode"] == "jmp":
                step += current["value"]
            else:
                step += 1
        else:
            instructions.append(step)
            return accumulator, instructions

def find_fault(program: list, executed_instructions: list) -> tuple:
    """iterates through all executed instructions to test and find the fault"""
    switch_opcode = {"jmp":"nop", "nop":"jmp"}
    modified_program = program.copy()
    for i in executed_instructions: 
        opcode = modified_program[i]["opcode"]
        if opcode != "acc":
            modified_program[i].update({"opcode": switch_opcode[opcode]})
            accumulator, instructions = run(modified_program)
            if instructions[-1] >= len(program):
                return accumulator, i
            modified_program[i].update({"opcode": opcode})
    return None, None


def main() -> None:
    """The main function for day 8. Answers Question 1 and 2."""
    program = load("day8.txt")
    accumulator, instructions = run(program)
    fixed_accumulator, instruction = find_fault(program, instructions)
    
    print(f"Total number of inputs: {len(program)}")
    print(f"value in accumulator when looping: {accumulator}")
    print(f"Corrupted instruction: {instruction}")
    print(f"value in accumulator when fixed: {fixed_accumulator}")
    # [print(input) for input in program]

if __name__ == "__main__":
    main()