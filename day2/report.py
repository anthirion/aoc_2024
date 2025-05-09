class Report:
  MAX_STEP = 3
  MIN_STEP = 1

  def __init__(self, levelsValue: list[int]) -> None:
    self._levels = levelsValue

  def __repr__(self) -> str:
    return " ".join([str(level) for level in self._levels])

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
      if not (self.MIN_STEP <= step <= self.MAX_STEP):
        return False
    return True
