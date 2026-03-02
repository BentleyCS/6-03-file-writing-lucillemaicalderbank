import random


def writeFile(inputList, fileName):
    with open(fileName, 'w') as f:
        for item in inputList:
            f.write(str(item) + "\n")


def sortNames(fileName, targetFile):
    with open(fileName, 'r') as f:
        names = f.read().splitlines()

    names.sort()

    writeFile(names, targetFile)


def highScore(newScore: int):
    with open("scores.txt", "a") as f:
        f.write(str(newScore) + "\n")

    all_scores = []
    with open("scores.txt", "r") as f:
        for line in f:
            clean_line = line.strip()
            if clean_line:
                all_scores.append(int(clean_line))

    if not all_scores:
        return 0.0

    return sum(all_scores) / len(all_scores)