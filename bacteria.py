from enum import Enum
from typing import List


class EBacteriaType(Enum):
    AEROBIC = 0
    ANAEROBIC = 1
    FACULTATIVE_ANAEROBIC = 2


class Bacteria:
    def __init__(self, uid: int, species_name: str, oxygen_requirement: EBacteriaType, min_nutrient: float,
                 growth_rate: float, death_rate: float, competition_factor: float):
        self.uid = uid
        self.species_name = species_name
        self.oxygen_requirement = oxygen_requirement  # EBacteriaType enum
        self.min_nutrient = min_nutrient  # Minimum nutrient requirement for growth
        self.min_oxygen = 0.1 if oxygen_requirement == EBacteriaType.AEROBIC else 0.001 if oxygen_requirement == EBacteriaType.FACULTATIVE_ANAEROBIC else 0
        self.growth_rate = growth_rate  # Base growth rate
        self.death_rate = death_rate  # Death rate per iteration
        self.competition_factor = competition_factor  # Factor influencing competition with other bacteria


bacteria_list: List[Bacteria] = [
    # AEROBIC
    Bacteria(
        uid=1,
        species_name="Bacillus subtilis",
        oxygen_requirement=EBacteriaType.AEROBIC,
        min_nutrient=0.1,
        growth_rate=0.7,
        death_rate=0.05,
        competition_factor=0.5,
    ),
    Bacteria(
        uid=2,
        species_name="Pseudomonas aeruginosa",
        oxygen_requirement=EBacteriaType.AEROBIC,
        min_nutrient=0.3,
        growth_rate=0.6,
        death_rate=0.02,
        competition_factor=0.7,
    ),
    Bacteria(
        uid=3,
        species_name="Nitrosomonas europaea",
        oxygen_requirement=EBacteriaType.AEROBIC,
        min_nutrient=0.05,
        growth_rate=0.3,
        death_rate=0.01,
        competition_factor=0.1,
    ),
    # ANAEROBIC
    Bacteria(
        uid=5,
        species_name="Clostridium perfringens",
        oxygen_requirement=EBacteriaType.ANAEROBIC,
        min_nutrient=0.4,
        growth_rate=0.4,
        death_rate=0.04,
        competition_factor=0.2,
    ),
    Bacteria(
        uid=6,
        species_name="Desulfovibrio desulfuricans",
        oxygen_requirement=EBacteriaType.ANAEROBIC,
        min_nutrient=0.1,
        growth_rate=0.2,
        death_rate=0.005,
        competition_factor=0.1,
    ),
    Bacteria(
        uid=7,
        species_name="Methanosarcina barkeri",
        oxygen_requirement=EBacteriaType.ANAEROBIC,
        min_nutrient=0.2,
        growth_rate=0.3,
        death_rate=0.001,
        competition_factor=0.2,
    ),
    # FACULTATIVE_ANAEROBIC
    Bacteria(
        uid=9,
        species_name="E. coli",
        oxygen_requirement=EBacteriaType.FACULTATIVE_ANAEROBIC,
        min_nutrient=0.2,  # Minimum nutrient requirement
        growth_rate=0.5,  # Base growth rate per iteration
        death_rate=0.03,  # Death rate per iteration (low mortality)
        competition_factor=0.3,  # Moderately competitive impact on other bacteria
    ),
    Bacteria(
        uid=10,
        species_name="Staphylococcus aureus",
        oxygen_requirement=EBacteriaType.FACULTATIVE_ANAEROBIC,
        min_nutrient=0.25,  # Minimum nutrient requirement
        growth_rate=0.45,  # Base growth rate per iteration
        death_rate=0.04,  # Death rate per iteration (low mortality)
        competition_factor=0.4,  # Moderately competitive impact on other bacteria
    ),
    Bacteria(
        uid=11,
        species_name="Enterococcus faecalis",
        oxygen_requirement=EBacteriaType.FACULTATIVE_ANAEROBIC,
        min_nutrient=0.2,
        growth_rate=0.4,
        death_rate=0.02,
        competition_factor=0.35,
    ),
]
