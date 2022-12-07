import string
import sys

with open("input.txt") as f:
    real_data=f.readlines()

dummy_data = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]

### Part 1 functions ###

def split_in_half(item):
    bonjovi = int(len(item)/2) ### Woooah we're halfway there!
    comp1= item[:bonjovi]
    comp2=item[bonjovi:]

    return comp1, comp2

def compare_compartments(comp1, comp2):
    common_item = set([c for c in comp1]).intersection([c for c in comp2])
    if len(common_item) > 1:
        print("there's more than one common item!")
        sys.exit()
        
    else:
        return next(iter(common_item)) # we want the value in the set returned, not the set

### part 2 functions ###

def get_elf_groups(input_data):
    groups = []
    current_group = []
    for elf in input_data:
        current_group.append(elf)
        if len(current_group) == 3:
            groups.append(current_group)
            current_group = []
    return groups


def compare_rucksacks_in_group(rucksacks):
    common_item = set([item for item in rucksacks[0]]).intersection([item for item in rucksacks[1]], [item for item in rucksacks[2]])
    try: 
        common_item.remove("\n") # need to strip out newline characters
    except:
        KeyError
        pass
    return next(iter(common_item))

### shared functions ###

def get_item_priority(item):
    prioritizer = string.ascii_lowercase+string.ascii_uppercase
    priority = prioritizer.find(item)+1 # because we want to index from 1-52, not 0-51
    if priority == 0:
        print("There's a mistake here. Common item not found in priority list")
        sys.exit()
    return priority


if __name__ == "__main__":
    total_item_priority = 0
    total_badge_priority = 0
    for rucksack in real_data:
        # part 1
        a, b = split_in_half(rucksack)
        common_item = compare_compartments(a,b)
        priority_score = get_item_priority(common_item)
        total_item_priority += priority_score
    print(f"Part 1. Total item priority is: {total_item_priority}")

    
    # part 2
    groups = get_elf_groups(real_data)
    for group in groups:
        badge = compare_rucksacks_in_group([rucksack for rucksack in group])
        badge_priority =get_item_priority(badge)
        total_badge_priority += badge_priority
    print(f"Part 2. Total badge priority is: {total_badge_priority}")


