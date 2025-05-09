from report import Report

class FaultTolerantReport(Report):
  """A fault tolerant report has a min size of 2 because a report of smaller size is safe"""

  def __init__(self, report: Report):
    self._levels = report._levels.copy()
    self._faultyLevelIndex = 0

  def __repr__(self) -> str:
    return super().__repr__()

  def acceptUnsafeReport(self) -> bool:
    """Apply the problem of Dampener to accept or not an unsafe report"""
    for faultyLevelIndex in range(len(self._levels)):
      self._faultyLevelIndex = faultyLevelIndex
      candidateLevels = self.removeFaultyLevelFromLevels()
      candidateReport = Report(candidateLevels)
      if candidateReport.isSafe():
        return True
    return False
    
  def removeFaultyLevelFromLevels(self) -> list[int]:
    return self._levels[:self._faultyLevelIndex] + self._levels[self._faultyLevelIndex + 1:]
  