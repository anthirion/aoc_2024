import re

def fillListswithPuzzleInput(filepath: str) -> tuple[list[int], list[int]]:
    leftList = []
    rightList = []
    try:
        with open(filepath, "r", encoding="utf8") as file:
            for line in file:
                if line: 
                    leftInt, rightInt = extractIntegersInLine(line)
                    leftList.append(leftInt)
                    rightList.append(rightInt)
        if len(leftList) == 0 and len(rightList) == 0:
            print("WARNING: the two lists are empty; the file is probably empty.")
        assert len(leftList) == len(rightList)
        return leftList, rightList
    except FileNotFoundError:
        print(f"File not found; please check file path {filepath}")
        exit(1)

def extractIntegersInLine(line: str) -> tuple[int, int]:
    # the line is not empty (checked in caller function)
    integerPattern = r"\d+"
    foundIntegers: list[str] = re.findall(integerPattern, line)
    assert len(foundIntegers) == 2
    return int(foundIntegers[0]), int(foundIntegers[1])

def sortLists(leftList: list[int], rightList:list[int]) -> tuple[list[int], list[int]]:
    return sorted(leftList), sorted(rightList)

def computeTotalDistance(leftList: list[int], rightList:list[int]) -> int:
    totalDistance = 0
    for leftInt, rightInt in zip(leftList, rightList):
        totalDistance += abs(leftInt - rightInt)
    return totalDistance
