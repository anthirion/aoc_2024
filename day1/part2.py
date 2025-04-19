from collections import defaultdict

def computeSimilarityScore(leftList: list[int], rightlist: list[int]) -> int:
    occurences = computeleftListOccurences(rightlist)
    similarityScore = 0
    for leftListInteger in leftList:
        similarityScore += leftListInteger * occurences.get(leftListInteger, 0)
    return similarityScore

# Naive implementation with O(n2) time complexity
# def computeleftListOccurences(leftList: list[int], rightlist: list[int]) -> list[int]:
#     occurences = []
#     for integer in leftList:
#         occurences.append(rightlist.count(integer))
#     return occurences

# Better implementation with O(n) time complexity
def computeleftListOccurences(rightlist: list[int]) -> dict[int, int]:
    """Returns a dictionnary where rightlist elements are keys and occurences are values"""
    # using a default dict removes the need to check if the key exists
    occurences: dict[int, int] = defaultdict(lambda: 0)
    for integer in rightlist:
        occurences[integer] += 1
    return occurences
