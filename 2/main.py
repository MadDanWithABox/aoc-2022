p1_win_mappings = {
    "A X\n":"draw",
    "A Y\n":"win",
    "A Z\n":"loss",
    "B X\n":"loss",
    "B Y\n":"draw",
    "B Z\n":"win",
    "C X\n":"win",
    "C Y\n":"loss",
    "C Z\n":"draw"
}

p2_win_mappings = {
    ("A","win"):"Y",
    ("A","draw"):"X",
    ("A","loss"):"Z",
    ("B","win"):"Z",
    ("B","draw"):"Y",
    ("B","loss"):"X",
    ("C","win"):"X",
    ("C","draw"):"Z",
    ("C","loss"):"Y"
}

point_mappings= {"win":6, "draw":3, "loss":0}
p1_selection_point_mappings = {"X":1, "Y":2, "Z":3}

dummy_data = ["A Y\n", "B X\n", "C Z\n"]
p2_res_mapping = {"X":"loss", "Y":"draw", "Z":"win"}

with open("input.txt") as f:
    real_data=f.readlines()


total = 0
for example in real_data:
    play1 = example[0]
    needed_res = p2_res_mapping[example[-2:-1]]
    key = (play1, needed_res)
    total += point_mappings[p2_res_mapping[example[-2:-1]]]
    total += p1_selection_point_mappings[p2_win_mappings[key]]
    print(total)

wdl_points = sum([point_mappings[p1_win_mappings[key]] for key in real_data])
played_points = sum([p1_selection_point_mappings[datum[-2:-1]] for datum in real_data])

print("Part1: ",wdl_points+played_points)
