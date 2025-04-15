from part1 import (
    fillListswithPuzzleInput,
    sortLists,
    computeTotalDistance
)

def main():
    leftList, rightList = fillListswithPuzzleInput("./day1/puzzle.txt")
    sortedLeftList, sortedRightList = sortLists(leftList, rightList)
    distance = computeTotalDistance(sortedLeftList, sortedRightList) 
    print(f"Distance between two lists: {distance}")

if __name__ == "__main__":
    main()
