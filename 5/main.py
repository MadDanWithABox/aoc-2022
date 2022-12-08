import re

#LOG_LEVEL = "info"
LOG_LEVEL = "debug"

# create lists of stacks (along x-axis and not y)
stacks = []
with open("input.txt") as file:
    instructions = file.readlines()
    for col in range(0, len(instructions [0])):
        stacks.append("")
        for line in range(0,8): #3 for toy change to 8 for main data
            if instructions [line][col] not in ["[", "]", " "]:
                stacks[col] += instructions [line][col]

# remove empty lists and list of trailing newlines
stacks = [stack for stack in stacks if stack != ''][:-1]

# remove stack diagram from input, reduce to only integers
# instructions are now [Digit, Digit, Digit]: move n from x1 to x2
instructions = [[int(d) for d in re.findall(r"\d+", line.strip())] for line in instructions[10:]] #5 for toy, change to 10 for full data



class Crane:
    def __init__(self, claw=""):
        self.claw = claw

class Stack:
    def __init__(self, number, crates=[], crane=Crane()):
        self.crates = crates
        self.crane = crane
        self.number = number

    def add_crate(self):
        self.crates.append(self.crane.claw)
        self.crane.claw = None
        return self.crates
        
    def remove_crate(self):
        self.crane.claw = self.crates.pop()
        return self.crates

    def multi_remove(self, number_to_remove):
        self.crane.claw = self.crates[-number_to_remove:]
        del self.crates[-number_to_remove:]
    
    def multi_add(self):
        self.crates.extend(self.crane.claw)
        self.crane.claw = None


    
all_crates = [list(reversed(stack)) for stack in stacks]

def one_stack_to_another(remove_stack: Stack, add_stack: Stack):
    remove_stack.remove_crate()
    add_stack.add_crate()


def follow_p2_instructions(instruction, stacks_of_crates):
    crates_to_move = instruction[0]
    stack_to_remove_from = stacks_of_crates[instruction[1]-1]
    stack_to_add_to = stacks_of_crates[instruction[2]-1]
    if LOG_LEVEL == "debug":
        print(f"Moving {crates_to_move} crates")
        print(f"Moving from {stack_to_remove_from.number} to {stack_to_add_to.number}")
    stack_to_remove_from.multi_remove(crates_to_move)
    stack_to_add_to.multi_add()

def follow_instruction(instruction, stacks_of_crates):
    i=0
    times_to_move = instruction[0]
    stack_to_remove_from = stacks_of_crates[instruction[1]-1]
    stack_to_add_to = stacks_of_crates[instruction[2]-1]
    if LOG_LEVEL == "debug":
        print(f"Performing the following action {times_to_move} times")
        print(f"Moving from {stack_to_remove_from.number} to {stack_to_add_to.number}")
    while i < times_to_move:
        one_stack_to_another(stack_to_remove_from, stack_to_add_to)
        i+=1

def print_out_crates(stacks_of_crates):
    for stack in stacks_of_crates:
        print(stack.crates)
    print("======================================")

def get_top_crates(stacks_of_crates):
    topline = ""
    for stack in stacks_of_crates:
        topline+=stack.crates[-1]
    print(topline)


if __name__ == "__main__":

    crane = Crane()
    # load main data #

    # note: need to re-initialise crate starting positions (or comment out section 1 to get answer for section 2)

    '''
    s1,s2,s3,s4,s5,s6,s7,s8,s9 = [Stack(i, e, crane) for i,e in enumerate(all_crates)]
    stacks_of_crates = [s1,s2,s3,s4,s5,s6,s7,s8,s9]
    print_out_crates(stacks_of_crates)
    for instruction in instructions:
        if LOG_LEVEL == "debug":
            print(f"instruction is:{instruction}")
        follow_instruction(instruction, stacks_of_crates)
        #print_out_crates(stacks_of_crates)
    print("Part 1 solution")
    get_top_crates(stacks_of_crates)
    '''

    s1,s2,s3,s4,s5,s6,s7,s8,s9 = [Stack(i, e, crane) for i,e in enumerate(all_crates)]
    stacks_of_crates = [s1,s2,s3,s4,s5,s6,s7,s8,s9]
    print_out_crates(stacks_of_crates)
    for instruction in instructions:
        if LOG_LEVEL == "debug":
            print(f"instruction is:{instruction}")
        follow_p2_instructions(instruction, stacks_of_crates)
        print_out_crates(stacks_of_crates)
    print("Part 2 solution")
    get_top_crates(stacks_of_crates)
