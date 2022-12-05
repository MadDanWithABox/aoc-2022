lists=[]

with open("input.txt") as f:
    lines=f.readlines()
    all_elves=[]
    current_elf=[]
    for line in lines:
        curr=line.strip("\n\r")
        if curr != "":
            val = int(curr)
            current_elf.append(val)
        else:
            all_elves.append(current_elf)
            current_elf=[]

print(all_elves)

dummy_elves = [[1,2,3],[4,5,6],[7,8],[1000], [900,10000, -29]]


def calc_total(snacks):
    total = 0
    for calories in snacks:
        total = total+calories
    return total

def find_fattest_elf(elves):
    calorie_laden_elf_index = None
    most_calories = 0
    for i, elf in enumerate(elves):
        calories = calc_total(elf)
        if calories > most_calories:
            calorie_laden_elf_index = i
            most_calories = calories
        
    solution = f"The elf with most calories is {calorie_laden_elf_index} with {most_calories} calories of snacks"
    
    return solution 

ans = find_fattest_elf(all_elves)
print(ans)