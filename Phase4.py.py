import random
import datetime
import statistics
from typing import List
from dataclasses import dataclass

# Configuration Parameters
TARGET_DEFECT_RATE = 0.02  # 2% target defect rate
SAMPLE_SIZE = 50  # Number of units to sample in each inspection
ACCEPTABLE_DEFECTS = 2  # Maximum number of defects allowed in a sample
NUM_SAMPLES = 10  # Number of samples to collect for analysis
REWORK_COST_PER_UNIT = 10.0  # Cost to rework a defective unit
SCRAP_COST_PER_UNIT = 5.0  # Cost to scrap a defective unit
INSPECTION_COST_PER_SAMPLE = 20.0  # Cost to inspect one sample
DAILY_PRODUCTION_VOLUME = 1000  # Number of units produced per day
REPORT_FILENAME = "quality_control_report.txt"  # Name of the report file

# Data Class for Inspection Results
@dataclass
class InspectionResult:
    """Represents the result of a single quality control inspection."""
    timestamp: datetime.datetime
    defects_found: int
    sample_passed: bool
    sample_data: List[bool]  # True = good, False = defective
    inspection_cost: float
    rework_cost: float = 0.0
    scrap_cost: float = 0.0

    def __str__(self):
        status = "Passed" if self.sample_passed else "Failed"
        return (f"Inspection Time: {self.timestamp}, Defects: {self.defects_found}, "
                f"Status: {status}, Inspection Cost: {self.inspection_cost:.2f}, "
                f"Rework Cost: {self.rework_cost:.2f}, Scrap Cost: {self.scrap_cost:.2f}")

# Function to simulate a single inspection
def inspect_sample(sample_size: int, defect_rate: float) -> InspectionResult:
    """Simulates the inspection of a sample of units for defects."""
    sample_data = [random.random() > defect_rate for _ in range(sample_size)]
    defects_found = sample_data.count(False)

    sample_passed = defects_found <= ACCEPTABLE_DEFECTS
    inspection_cost = INSPECTION_COST_PER_SAMPLE
    rework_cost = defects_found * REWORK_COST_PER_UNIT if not sample_passed else 0.0
    scrap_cost = defects_found * SCRAP_COST_PER_UNIT if not sample_passed else 0.0

    return InspectionResult(
        timestamp=datetime.datetime.now(),
        defects_found=defects_found,
        sample_passed=sample_passed,
        sample_data=sample_data,
        inspection_cost=inspection_cost,
        rework_cost=rework_cost,
        scrap_cost=scrap_cost
    )

# Function to perform quality control and calculate costs
def perform_quality_control(num_samples: int, sample_size: int, defect_rate: float) -> List[InspectionResult]:
    """Performs a series of quality control inspections and returns a list of results."""
    results = [inspect_sample(sample_size, defect_rate) for _ in range(num_samples)]
    return results

# Run inspections and print results
inspection_results = perform_quality_control(NUM_SAMPLES, SAMPLE_SIZE, TARGET_DEFECT_RATE)
for result in inspection_results:
    print(result)
