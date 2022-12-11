def solve(calories):
    maxElf = []
    currTotal = 0
    for i in calories:
        if i != '':
            currTotal += int(i)
        else:
            maxElf.append(currTotal)
            currTotal = 0
    return sum(sorted(maxElf)[-3:])

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        calories = f.read().split("\n")
    print(solve(calories))