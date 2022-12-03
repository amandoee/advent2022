point = {
    "A X": 3+1,
    "A Y": 6+2,
    "A Z": 3,
    "B X": 1,
    "B Y": 3+2,
    "B Z": 6+3,
    "C X": 6+1,
    "C Y": 2,
    "C Z": 3+3
}
point_del2 = {
    "A X": 3+0,
    "A Y": 1+3,
    "A Z": 2+6,
    "B X": 1+0,
    "B Y": 2+3,
    "B Z": 3+6,
    "C X": 2+0,
    "C Y": 3+3,
    "C Z": 1+6
}

del1=0
del2=0
with open("input.txt") as input:
    data = [i for i in input.read().strip().split("\n")]
    for item in data:
        del1+=(point[item])
        del2+=(point_del2[item])
    print("Summen til del 1:",del1)
    print("Summen til del 2:",del2)



