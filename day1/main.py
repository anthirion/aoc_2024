from part1 import (
    fillListswithPuzzleInput,
    sortLists,
    computeTotalDistance,
)
from part2 import (
    computeSimilarityScore,
)

import argparse

def main():
    leftList, rightList = fillListswithPuzzleInput("./day1/puzzle.txt")
    parser = argparse.ArgumentParser()
    parser.add_argument("--part", type=int, choices=[1, 2], default=1)
    args = parser.parse_args()
    
    if args.part == 1:
        sortedLeftList, sortedRightList = sortLists(leftList, rightList)
        distance = computeTotalDistance(sortedLeftList, sortedRightList) 
        print(f"Distance between two lists: {distance}")
    elif args.part == 2:
        similarityScore = computeSimilarityScore(leftList, rightList)
        print(f"Similarity score between two lists: {similarityScore}")

if __name__ == "__main__":
    main()
