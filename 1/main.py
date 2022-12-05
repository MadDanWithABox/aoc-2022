lists=[]

with open("input.txt") as f:
    lines=f.readlines()

dummy_elves = [[1,2,3], [4,5,6], [7,8],[1000]]

def calc_total(snacks):
    total = 0
    for calories in snacks:
        total += snacks
    return total

calorie_laden_elf_index = None
most_calories = 0

def find_fattest_elf(elves):
    for i, elf in enumerate(elves):
        calories = calc_total(snacks)
        if calories > most_calories:
            calorie_laden_elf_index = i
            most_calories = calories
        
    solution = f"The elf with most calories is {calorie_laden_elf_index} with {most_calories} calories of snacks"
    
    return solution 

ans = find_fattest_elf(dummy_elves)
print(ans)