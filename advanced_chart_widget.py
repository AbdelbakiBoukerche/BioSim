from typing import List

import plotly.express as px
import pandas as pd

from PySide6 import QtCore, QtWidgets, QtWebEngineWidgets

from bacteria import Bacteria
from soil import Soil, ESoilDepletionFunction


class ChartWidget(QtWidgets.QWidget):
    def __init__(self,bacteria_list: List[Bacteria], soil: Soil, soil_depletion_function: ESoilDepletionFunction,
                 parent: QtWidgets.QWidget | None = None):
        super().__init__(parent)
        self.browser = QtWebEngineWidgets.QWebEngineView(self)

        self._active_soil = soil
        self._active_bacteria_list = bacteria_list
        self._depletion_function = soil_depletion_function

        v_layout = QtWidgets.QVBoxLayout(self)
        v_layout.addWidget(self.browser)

        self.resize(1000, 800)

    def show_graph(self, simulation_data):
        data = []
        for species_name, population in simulation_data.items():

            for i, value in enumerate(population):
                data.append({
                    'Depth': i,
                    'Population': int(value),
                    'Species': species_name,
                    'World Depth': -i,
                    'Size': value
                })

        df = pd.DataFrame(data)

        fig = px.line_3d(df, x="Depth", y="Population", z="World Depth", color="Species",
                         title='Bacteria Population Simulation')

        self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))
