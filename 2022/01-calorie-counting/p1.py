def solve(calories):
    maxElf = 0
    currTotal = 0
    for i in calories:
        if i != '':
            currTotal += int(i)
        else:
            maxElf = max(maxElf, currTotal)
            currTotal = 0
    return maxElf

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        calories = f.read().split("\n")
    print(solve(calories))