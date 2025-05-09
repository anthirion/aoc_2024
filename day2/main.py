import argparse

from data import Data

def getArgumentsFromCommandLine():
  parser = argparse.ArgumentParser()
  parser.add_argument("--part", type=int, choices=[1, 2], default=1)
  return parser.parse_args()

def main():
  args = getArgumentsFromCommandLine()
  
  inputPuzzlePath = "puzzle.txt"
  data: Data = Data(inputPuzzlePath)
  
  if args.part == 1:
    print(f"Number of safe reports: {data.countSafeReports()}")
  elif args.part == 2:
    print(f"Number of safe reports using Dampener problem: {data.countSafeReportsAfterCorrection()}")

if __name__ == "__main__":
    main()