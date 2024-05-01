from enum import Enum
from typing import List
import numpy as np


class ESoilDepletionFunction(Enum):
    EXPONENTIAL = 0
    SIGMOID = 1
    POWER_LAW = 2


class Soil:
    def __init__(self, soil_type: str, max_depth: float, o2_depletion_rate: float, nutrient_depletion_rate: float):
        self.soil_type = soil_type
        self.max_depth = max_depth
        self.o2_depletion_rate = o2_depletion_rate
        self.nutrient_depletion_rate = nutrient_depletion_rate
        self.initial_o2 = 0.21  # 21% Oxygen at ground level
        self.initial_nutrient = 0.75  # 75% Nutrients at ground level

    def oxygen_availability(self, depth: float, depletion_function: ESoilDepletionFunction):
        """Calculates oxygen availability at a specific depth for this soil,
        ensuring 21% at 0cm."""
        if depth == 0:
            return self.initial_o2  # 21% oxygen at 0cm

        elif depletion_function == ESoilDepletionFunction.EXPONENTIAL:
            decay_factor = -self.o2_depletion_rate * np.power(depth, 0.3)
            return self.initial_o2 * np.exp(decay_factor)

        elif depletion_function == ESoilDepletionFunction.SIGMOID:
            return self.initial_o2 / (1 + np.exp(self.o2_depletion_rate * (depth - self.max_depth / 2)))

        elif depletion_function == ESoilDepletionFunction.POWER_LAW:
            # alpha: parameter controlling depletion rate (0 < alpha < 1)
            alpha = 0.8
            return self.initial_o2 * (1 - depth ** alpha / self.max_depth ** alpha)

    def nutrient_availability(self, depth: float, depletion_function: ESoilDepletionFunction):
        """Calculates nutrient availability at a specific depth for this soil."""

        if depth == 0:
            return self.initial_nutrient

        elif depletion_function == ESoilDepletionFunction.EXPONENTIAL:
            decay_factor = -self.nutrient_depletion_rate * np.power(depth, 0.3)
            return self.initial_nutrient * np.exp(decay_factor)

        elif depletion_function == ESoilDepletionFunction.SIGMOID:
            return self.initial_nutrient / (1 + np.exp(self.nutrient_depletion_rate * (depth - self.max_depth / 2)))

        elif depletion_function == ESoilDepletionFunction.POWER_LAW:
            # alpha: parameter controlling depletion rate (0 < alpha < 1)
            alpha = 0.8
            return self.initial_nutrient * (1 - depth ** alpha / self.max_depth ** alpha)


soil_list: List[Soil] = [
    Soil(
        soil_type='Sandy',
        max_depth=200,  # Can be very deep depending on location
        o2_depletion_rate=0.05,  # Well-aerated due to large pore spaces
        nutrient_depletion_rate=0.5,  # Low nutrient retention due to fast drainage
    ),
    Soil(
        soil_type='Clay',
        max_depth=200,  # Depth depends on formation process
        o2_depletion_rate=0.8,  # Poorly aerated due to small pore spaces
        nutrient_depletion_rate=0.1,  # High nutrient retention due to charged clay particles
    ),
    Soil(
        soil_type='Loam',
        max_depth=200,  # Typically shallower than sandy soil
        o2_depletion_rate=0.2,  # Balanced between sandy and clay
        nutrient_depletion_rate=0.15,  # Moderately fertile
    ),
    Soil(
        soil_type='Silt',
        max_depth=200,  # Often shallow due to wind deposition
        o2_depletion_rate=0.15,  # Holds oxygen slightly better than loam
        nutrient_depletion_rate=0.1,  # Highly fertile due to fine particles
    ),
    Soil(
        soil_type='Peat',
        max_depth=200,  # Can be very deep in wetlands
        o2_depletion_rate=0.8,  # Highly depleted due to water saturation
        nutrient_depletion_rate=0.05,  # Rich in organic matter, slow nutrient release
    ),
    Soil(
        soil_type='Calcareous',
        max_depth=200,  # Depends on underlying rock formations
        o2_depletion_rate=0.25,  # Can vary depending on drainage
        nutrient_depletion_rate=0.12,  # Moderately fertile, influenced by calcium carbonate content
    ),
    Soil(
        soil_type='Lateritic',
        max_depth=200,  # Can be deep in tropical regions
        o2_depletion_rate=0.4,  # Often well-drained, leading to faster oxygen depletion
        nutrient_depletion_rate=0.2,  # Low in nutrients due to high iron oxide content
    )
]
