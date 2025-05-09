from faultTolerantReport import FaultTolerantReport
from report import Report

class Data:
  def __init__(self, inputFilepath: str) -> None:
    self.inputFilepath = inputFilepath
    self.reports: list[Report] = self.getReportsFromPuzzleInput()

  def __repr__(self) -> str:
    displayed_str = ""
    for report in self.reports:
      displayed_str += f"{print(report)}\n"
    return displayed_str

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
  
  # for part 2
  def countSafeReportsAfterCorrection(self) -> int:
    safeReportCount = 0
    for report in self.reports:
      if report.isSafe():
        safeReportCount += 1
      else:
        faultTolerantReport = FaultTolerantReport(report)
        if faultTolerantReport.acceptUnsafeReport():
          safeReportCount += 1
    return safeReportCount
