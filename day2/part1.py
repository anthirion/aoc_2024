from __future__ import annotations

class Data:
  def __init__(self, inputFilepath: str) -> None:
    self.inputFilepath = inputFilepath
    self.reports: list[Report] = self.getReportsFromPuzzleInput()

  def getReportsFromPuzzleInput(self) -> list[Report]:
    parsedReports: list[Report] = []
    try:
      with open(self.inputFilepath, "r", encoding="utf-8") as file:
        for lineContent in file:
          strippedLine = lineContent.strip()
          if strippedLine:
            try:
              levels: list[int] = [int(s) for s in strippedLine.split()]
              reportInstance = Report(levels)
              parsedReports.append(reportInstance)
            except ValueError:
              raise ValueError(f"Line contains non-integer values: '{strippedLine}'")
    except FileNotFoundError:
      raise FileNotFoundError(f"Input file not found: {self.inputFilepath}")
    return parsedReports

  def countSafeReports(self) -> int:
    safeReportCount = 0
    for report in self.reports:
      if report.isSafe():
        safeReportCount += 1
    return safeReportCount


class Report:
  def __init__(self, levelsValue: list[int]) -> None:
    self._levels = levelsValue
    self._greatestStep = 3
    self._leastStep = 1

  @property
  def levels(self) -> list[int]:
    return self._levels
  
  @levels.setter
  def levels(self, levelsValue: list[int]) -> None:
    if not isinstance(levelsValue, list) or not all(isinstance(level, int) for level in levelsValue):
      raise ValueError("Levels must be a list of integers")
    if not levelsValue:
      raise ValueError("Report cannot be empty")
    self._levels = levelsValue

  def isSafe(self) -> bool:
    return self.isMonotonic() and self.stepsBounded()
  
  def isMonotonic(self) -> bool:
    if len(self.levels) < 2:
      return True
    
    isIncreasing = all(self.levels[i] <= self.levels[i+1] for i in range(len(self.levels)-1))
    isDecreasing = all(self.levels[i] >= self.levels[i+1] for i in range(len(self.levels)-1))

    return isDecreasing or isIncreasing


  def stepsBounded(self) -> bool:
    if len(self.levels) < 2:
      return True
    
    for i in range(len(self.levels) - 1):
      step = abs(self.levels[i+1] - self.levels[i])
      if not (self._leastStep <= step <= self._greatestStep):
        return False
    return True
