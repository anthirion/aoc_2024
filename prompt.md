# Instructions pour l'écriture de code

Complète moi le code fourni en suivant les commentaires et les règles suivantes:

## Règles générales

- Garde la structure fournie
- N'hésite pas à reformuler certains noms de fonctions ou de variables s'ils ne sont pas assez clair
- Le code doit être le plus lisible possible -> évite de chainer plusieurs appels de fonction, éviter les lignes trop longues
- Le code doit être le plus simple possible
- Utilise le camel case uniquement

## Règles de nommage des variables et fonctions

- Donne des noms explicites et compréhensibles aux variables
- Toutes les variables et noms de fonctions doivent être écrits en anglais
- Les noms de variables (mais pas de fonctions) peuvent être très courts (jusqu'à un seul caractère) uniquement si leur scope est limité -> plus le nom de la variable est court, plus le scope doit être limité

## Règles sur les commentaires

- N'ajoute **AUCUN** commentaire
- Supprime les commentaires fournissant des instructions de complétion de code

## Règles sur les fonctions

- Le nom de la fonction doit être suffisamment clair pour comprendre ce que fait la fonction
- Une fonction doit réaliser une seule tâche
- Une fonction doit avoir un seul niveau d'abstraction : soit la fonction manipule des concepts de bas niveau soit de haut niveau, pas les 2. Si tu as besoin des 2, crée une nouvelle fonction et utilise la dans la première.
- Dans l'idéal, une fonction doit avoir un argument et retourner un résultat. Il est possible d'avoir 2 arguments dans une fonction mais c'est à éviter. Eviter le plus possible les autres situations: 3 arguments ou plus, pas de retour.
- Les fonctions doivent rester concises: pas plus de 20 lignes par fonction

## Gestion des erreurs

- Préférer les exceptions aux codes d'erreurs
- Traiter toutes les erreurs possibles (par exemple une erreur d'ouverture d'un fichier)
- Les messages d'erreur ne doivent pas se terminer par un point

## Typage

- Ajoute les type en respectant les conventions de mypy

# Exemples de code

Pour t'aider dans l'écriture de code, voici un exemple dont tu peux t'inspirer:

```python
def main():
    leftList, rightList = fillListsWithPuzzleInput("./day1/puzzle.txt")
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

def fillListsWithPuzzleInput(filepath: str) -> tuple[list[int], list[int]]:
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

def computeSimilarityScore(leftList: list[int], rightList: list[int]) -> int:
  occurrences = computeLeftListOccurrences(rightList)
  similarityScore = 0
  for leftListInteger in leftList:
      similarityScore += leftListInteger * occurrences.get(leftListInteger, 0)
  return similarityScore

def computeLeftListOccurrences(rightList: list[int]) -> dict[int, int]:
  """Returns a dictionary where rightList elements are keys and occurrences are values"""
  # using a default dict removes the need to check if the key exists
  occurrences: dict[int, int] = defaultdict(lambda: 0)
  for integer in rightList:
      occurrences[integer] += 1
  return occurrences
```
