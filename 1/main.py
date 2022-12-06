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

dummy_elves = [[1000, 2000, 3000], [4000], [5000, 6000], [7000,8000,9000], [10000]]


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

def find_3_fattest(elves):
    top3 = [1,1,1]
    for elf in elves:
        calories = calc_total(elf)
        if calories > min(top3):
            print(f"FAT ELF! {calories}")
            top3= sorted(top3)
            top3[0] = calories
            print(top3)
    print(f"total cals for pt.2: {sum(top3)}")


print(find_fattest_elf(all_elves))

find_3_fattest(all_elves)


