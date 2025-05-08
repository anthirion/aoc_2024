from collections import defaultdict

def computeSimilarityScore(leftList: list[int], rightList: list[int]) -> int:
  occurrences = computeLeftListOccurrences(rightList)
  similarityScore = 0
  for leftListInteger in leftList:
      similarityScore += leftListInteger * occurrences.get(leftListInteger, 0)
  return similarityScore

# Naive implementation with O(n2) time complexity
# def computeLeftListOccurrences(leftList: list[int], rightList: list[int]) -> list[int]:
#   occurrences = []
#   for integer in leftList:
#       occurrences.append(rightList.count(integer))
#   return occurrences

# Better implementation with O(n) time complexity
def computeLeftListOccurrences(rightList: list[int]) -> dict[int, int]:
  """Returns a dictionary where rightList elements are keys and occurrences are values"""
  # using a default dict removes the need to check if the key exists
  occurrences: dict[int, int] = defaultdict(lambda: 0)
  for integer in rightList:
      occurrences[integer] += 1
  return occurrences
