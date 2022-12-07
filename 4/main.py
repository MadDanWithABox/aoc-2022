

dummy_data = [
    [2-4,6-8],
    [2-3,4-5],
    [5-7,7-9],
    [2-8,3-7],
    [6-6,4-6],
    [2-6,4-8],
]

class Elf:
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end


    
def elf_start_end(elf):
    elf_start = elf.split("-")[0]
    elf_end = elf.split("-")[1]
    return elf_start, elf_end

def check_ranges(start1, start2, end1, end2):
    if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
        return True
    else:
        return False

def check_ranges_part_2(start1, start2, end1, end2):
    if (start1 <= start2 and end1 >= start2) or (start2 <= start1 and end2 >= start1):
        return True
    else:
        return False

if __name__ == "__main__":
    p1_total = 0
    p2_total=0
    with open("input.txt") as file:
        for line in file:
            contents = line.split(",")
            c1 = contents[0]
            c2 = contents[1]
            e1_start, e1_end = elf_start_end(c1)
            e2_start, e2_end = elf_start_end(c2)

            elf1 = Elf(e1_start, e1_end)
            elf2 = Elf( e2_start, e2_end)

            if check_ranges(int(elf1.start), int(elf2.start), int(elf1.end), int(elf2.end)):
                p1_total+=1
            if check_ranges_part_2(int(elf1.start), int(elf2.start), int(elf1.end), int(elf2.end)):
                p2_total +=1


    print(f"Part 1 result: {p1_total}")
    print(f"Part 2 result: {p2_total}")


