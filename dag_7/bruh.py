from collections import defaultdict

# Læs indputfilen og gem den som en streng
data = open("input.txt").read().strip()

# Initialiser et ordbog med standardværdier på 0
størrelser = defaultdict(int)

# Opret en tom liste til at gemme den aktuelle sti
sti = []

# Del inputstrengen op ved nye linjeskift
for linje in data.split("\n"):
    # Hvis linjen starter med "$ cd", er det et kommando for at skifte mappe
    if linje.startswith("$ cd"):
        # Udtræk mappenavnet fra linjen
        d = linje.split()[2]
        
        # Hvis mappenavnet er "/", tilføj det til stien
        if d == "/":
            sti.append("/")
        # Hvis mappenavnet er "..", fjern det sidste element fra stien
        elif d == "..":
            sidste = sti.pop()
        # Ellers, tilføj mappenavnet til stien
        else:
            sti.append(f"{sti[-1]}{'/' if sti[-1] != '/' else ''}{d}")
    # Hvis det første tegn i linjen er numerisk, er det en filstørrelse
    if linje[0].isnumeric():
        # For hver mappe i stien, tilføj filstørrelsen til ordbogen størrelser
        for p in sti:
            størrelser[p] += int(linje.split()[0])

# Beregn og udskriv resultatet for Del 1
print(f"Del 1: {sum(s for s in størrelser.values() if s <= 100_000)}")

# Beregn og udskriv resultatet for Del 2
print(f"Del 2: {min(s for s in størrelser.values() if s >= 30_000_000 - (70_000_000 - størrelser['/']))}")
