from typing import List

import numpy as np
import uuid
from PySide6 import QtWidgets, QtCharts, QtCore, QtGui
from ui.main_window_ui import Ui_MainWindow
from bacteria import Bacteria, bacteria_list, EBacteriaType
from soil import Soil, soil_list, ESoilDepletionFunction
from interactive_chart_view import InteractiveChartView
from advanced_chart_widget import ChartWidget


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.setMinimumHeight(640)
        self.setWindowTitle('BioSim - University of Oran 1')
        self.statusBar().showMessage('ABDELBAKI Boukerche', 0)

        self._active_bacteria_list: List[Bacteria] = []
        self._active_soil = None
        self._depletion_function: ESoilDepletionFunction = ESoilDepletionFunction.EXPONENTIAL

        self._connections()

        self.tableWidget_bacteriaList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_bacteriaList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_bacteriaList.setColumnCount(6)
        self.tableWidget_bacteriaList.setHorizontalHeaderLabels(['Name', 'Type', 'Min Nutrient', 'Growth Rate',
                                                                 'Death Rate', 'Competition'])
        self.tableWidget_bacteriaList.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        self.chart_view = InteractiveChartView()
        self.chart_view_oxygen = InteractiveChartView()
        self.chart_view_nutrient = InteractiveChartView()

        self.groupBox_simulation.layout().addWidget(self.chart_view)
        self.groupBox_simulation.layout().addWidget(self.chart_view_oxygen)
        self.groupBox_simulation.layout().addWidget(self.chart_view_nutrient)

        self._populate_bacteria()
        self._populate_bacteria_oxygen_requirements()
        self._populate_depletion_simulation_function()
        self.comboBox_depletionFunction.setCurrentIndex(ESoilDepletionFunction.EXPONENTIAL.value)
        self._populate_soil()

    def _populate_bacteria(self):
        for i, bacteria in enumerate(bacteria_list):
            self.comboBox_bacteria.insertItem(i, bacteria.species_name, userData=bacteria)
        self.comboBox_bacteria.insertItem(len(bacteria_list), 'Custom')

    def _populate_bacteria_oxygen_requirements(self):
        self.comboBox_oxygenRequirements.insertItem(0, 'Aerobic')
        self.comboBox_oxygenRequirements.insertItem(1, 'Anaerobic')
        self.comboBox_oxygenRequirements.insertItem(2, 'Facultative Anaerobic')

    def _populate_depletion_simulation_function(self):
        self.comboBox_depletionFunction.insertItem(0, 'Exponential')
        self.comboBox_depletionFunction.insertItem(1, 'Sigmoid')
        self.comboBox_depletionFunction.insertItem(2, 'Power Law')

    def _populate_soil(self):
        for i, soil in enumerate(soil_list):
            self.comboBox_soilType.insertItem(i, soil.soil_type, userData=soil)
        self.comboBox_soilType.insertItem(len(soil_list), 'Custom')

    def _plot_distribution(self, population_dict):
        chart = QtCharts.QChart()
        chart.setTitle("Bacterial Population Distribution")
        # chart.setAnimationOptions(QtCharts.QChart.AllAnimations)

        axis_x = QtCharts.QValueAxis()
        axis_x.setLabelFormat("%d")
        axis_x.setTitleText("Soil Depth (cm)")
        axis_x.setMinorTickCount(5)
        axis_x.setRange(0, len(population_dict[next(iter(population_dict))]))

        axis_y = QtCharts.QValueAxis()
        axis_y.setLabelFormat("%.2f")
        axis_y.setTitleText("Bacterial Population")
        axis_y.setMinorTickCount(5)
        axis_y.setRange(0, max([max(values) for values in population_dict.values()]))

        chart.addAxis(axis_x, QtCore.Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(axis_y, QtCore.Qt.AlignmentFlag.AlignLeft)

        for species_name, population_values in population_dict.items():
            series = QtCharts.QLineSeries()
            series.setName(species_name)

            for i, population in enumerate(population_values):
                series.append(i, population)

            chart.addSeries(series)
            series.attachAxis(axis_x)
            series.attachAxis(axis_y)

        self.chart_view.setChart(chart)

    def _plot_oxygen_availability(self):
        chart = QtCharts.QChart()
        chart.setTitle('Oxygen Availability')
        # chart.setAnimationOptions(QtCharts.QChart.AllAnimations)

        axis_x = QtCharts.QValueAxis()
        axis_x.setLabelFormat('%d')
        axis_x.setTitleText('Soil Depth (cm)')
        axis_x.setMinorTickCount(5)
        axis_x.setRange(0, self._active_soil.max_depth)

        axis_y = QtCharts.QValueAxis()
        axis_y.setLabelFormat('%.2f')
        axis_y.setTitleText('Oxygen Percentage')
        axis_y.setMinorTickCount(5)
        axis_y.setRange(0, 100)

        chart.addAxis(axis_x, QtCore.Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(axis_y, QtCore.Qt.AlignmentFlag.AlignLeft)

        series = QtCharts.QLineSeries()
        series.setName('Oxygen Percentage')
        series.setColor(QtGui.QColor('red'))

        for i in range(0, self._active_soil.max_depth):
            oxygen_available = self._active_soil.oxygen_availability(i, self._depletion_function) * 100
            series.append(i, oxygen_available)

        chart.addSeries(series)
        series.attachAxis(axis_x)
        series.attachAxis(axis_y)

        self.chart_view_oxygen.setChart(chart)

    def _plot_nutrient_availability(self):
        chart = QtCharts.QChart()
        chart.setTitle('Nutrient Availability')
        # chart.setAnimationOptions(QtCharts.QChart.AllAnimations)

        axis_x = QtCharts.QValueAxis()
        axis_x.setLabelFormat('%d')
        axis_x.setTitleText('Soil Depth (cm)')
        axis_x.setMinorTickCount(5)
        axis_x.setRange(0, self._active_soil.max_depth)

        axis_y = QtCharts.QValueAxis()
        axis_y.setLabelFormat('%.2f')
        axis_y.setTitleText('Nutrient Percentage')
        axis_y.setMinorTickCount(5)
        axis_y.setRange(0, 100)

        chart.addAxis(axis_x, QtCore.Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(axis_y, QtCore.Qt.AlignmentFlag.AlignLeft)

        series = QtCharts.QLineSeries()
        series.setName('Nutrient Percentage')
        series.setColor(QtGui.QColor('green'))

        for i in range(0, self._active_soil.max_depth):
            oxygen_available = self._active_soil.nutrient_availability(i, self._depletion_function) * 100
            series.append(i, oxygen_available)

        chart.addSeries(series)
        series.attachAxis(axis_x)
        series.attachAxis(axis_y)

        self.chart_view_nutrient.setChart(chart)

    def _connections(self):
        self.action_startSimulation.triggered.connect(self._start_simulation_slot)

        self.comboBox_bacteria.currentIndexChanged.connect(self._bacteria_changed_slot)
        self.pushButton_insertBacteria.clicked.connect(self._insert_bacteria_clicked_slot)

        self.comboBox_soilType.currentIndexChanged.connect(self._soil_type_changed_slot)
        self.comboBox_depletionFunction.currentIndexChanged.connect(self._depletion_function_changed_slot)
        self.pushButton_useSoil.clicked.connect(self._use_soil_clicked_slot)

        self.pushButton_removeBacteria.clicked.connect(self._remove_bacteria_clicked_slot)

    def _bacteria_changed_slot(self, index: int):
        if index == len(bacteria_list):
            self.lineEdit_name.clear()
            self.lineEdit_name.setEnabled(True)
            self.comboBox_oxygenRequirements.setEnabled(True)
            self.doubleSpinBox_minNutrient.setEnabled(True)
            self.doubleSpinBox_growthRate.setEnabled(True)
            self.doubleSpinBox_deathRate.setEnabled(True)
            self.doubleSpinBox_competitionFactor.setEnabled(True)

        else:
            # Predefined bacteria selected
            bacteria = bacteria_list[index]

            self.lineEdit_name.setText(bacteria.species_name)
            self.lineEdit_name.setEnabled(False)

            self.comboBox_oxygenRequirements.setCurrentIndex(bacteria.oxygen_requirement.value)
            self.comboBox_oxygenRequirements.setEnabled(False)

            self.doubleSpinBox_minNutrient.setValue(bacteria.min_nutrient)
            self.doubleSpinBox_minNutrient.setEnabled(False)

            self.doubleSpinBox_growthRate.setValue(bacteria.growth_rate)
            self.doubleSpinBox_growthRate.setEnabled(False)

            self.doubleSpinBox_deathRate.setValue(bacteria.death_rate)
            self.doubleSpinBox_deathRate.setEnabled(False)

            self.doubleSpinBox_competitionFactor.setValue(bacteria.competition_factor)
            self.doubleSpinBox_competitionFactor.setEnabled(False)

    def _soil_type_changed_slot(self, index: int):
        if index == len(soil_list):
            self.pushButton_useSoil.setEnabled(True)
            self.spinBox_maxDepth.setEnabled(True)
            self.doubleSpinBox_o2DepletionRate.setEnabled(True)
            self.doubleSpinBox_nutrientDepletionRate.setEnabled(True)

        else:
            # Predefined soil selected
            soil = soil_list[index]

            self.pushButton_useSoil.setEnabled(False)

            self.spinBox_maxDepth.setValue(soil.max_depth)
            self.spinBox_maxDepth.setEnabled(False)

            self.doubleSpinBox_o2DepletionRate.setValue(soil.o2_depletion_rate)
            self.doubleSpinBox_o2DepletionRate.setEnabled(False)

            self.doubleSpinBox_nutrientDepletionRate.setValue(soil.nutrient_depletion_rate)
            self.doubleSpinBox_nutrientDepletionRate.setEnabled(False)

            self._active_soil = soil

    def _depletion_function_changed_slot(self, index: int):
        self._depletion_function = ESoilDepletionFunction(index)

    def _use_soil_clicked_slot(self):
        max_depth = self.spinBox_maxDepth.value()
        o2_depletion_rate = self.doubleSpinBox_o2DepletionRate.value()
        nutrient_depletion_rate = self.doubleSpinBox_nutrientDepletionRate.value()

        self._active_soil = Soil(
            soil_type='Custom',
            max_depth=max_depth,
            o2_depletion_rate=o2_depletion_rate,
            nutrient_depletion_rate=nutrient_depletion_rate
        )

    def _insert_bacteria_clicked_slot(self):
        current_index = self.comboBox_bacteria.currentIndex()

        if current_index == len(bacteria_list):
            name = self.lineEdit_name.text()
            oxygen_requirement = self.comboBox_oxygenRequirements.currentIndex()
            min_nutrient = self.doubleSpinBox_minNutrient.value()
            growth_rate = self.doubleSpinBox_growthRate.value()
            death_rate = self.doubleSpinBox_deathRate.value()
            competition_factor = self.doubleSpinBox_competitionFactor.value()

            if not name:
                warning_box = QtWidgets.QMessageBox()
                warning_box.setText('A name must be specified')
                warning_box.setIcon(QtWidgets.QMessageBox.Critical)
                return warning_box.exec()

            bacteria = Bacteria(
                uid=uuid.uuid4().int,
                species_name=name,
                oxygen_requirement=EBacteriaType(oxygen_requirement),
                min_nutrient=min_nutrient,
                growth_rate=growth_rate,
                death_rate=death_rate,
                competition_factor=competition_factor
            )

            if not any(b.species_name == bacteria.species_name for b in self._active_bacteria_list):
                self._active_bacteria_list.append(bacteria)

                row_index = len(self._active_bacteria_list) - 1

                self.tableWidget_bacteriaList.insertRow(row_index)
                self.tableWidget_bacteriaList.setItem(row_index, 0,
                                                      QtWidgets.QTableWidgetItem(bacteria.species_name))
                self.tableWidget_bacteriaList.setItem(row_index, 1,
                                                      QtWidgets.QTableWidgetItem(bacteria.oxygen_requirement.name))
                self.tableWidget_bacteriaList.setItem(row_index, 2,
                                                      QtWidgets.QTableWidgetItem(str(bacteria.min_nutrient)))
                self.tableWidget_bacteriaList.setItem(row_index, 3,
                                                      QtWidgets.QTableWidgetItem(str(bacteria.growth_rate)))
                self.tableWidget_bacteriaList.setItem(row_index, 4,
                                                      QtWidgets.QTableWidgetItem(str(bacteria.death_rate)))
                self.tableWidget_bacteriaList.setItem(row_index, 5,
                                                      QtWidgets.QTableWidgetItem(str(bacteria.competition_factor)))

            else:
                warning_box = QtWidgets.QMessageBox()
                warning_box.setText('Bacteria is already added to the simulation')
                warning_box.setIcon(QtWidgets.QMessageBox.Warning)
                return warning_box.exec()

        else:
            # Predefined bacteria selected
            bacteria = bacteria_list[current_index]
            if bacteria not in self._active_bacteria_list:
                self._active_bacteria_list.append(bacteria)

                row_index = len(self._active_bacteria_list) - 1

                self.tableWidget_bacteriaList.insertRow(row_index)
                self.tableWidget_bacteriaList.setItem(row_index, 0,
                                                      QtWidgets.QTableWidgetItem(bacteria.species_name))
                self.tableWidget_bacteriaList.setItem(row_index, 1,
                                                      QtWidgets.QTableWidgetItem(bacteria.oxygen_requirement.name))
                self.tableWidget_bacteriaList.setItem(row_index, 2,
                                                      QtWidgets.QTableWidgetItem(str(bacteria.min_nutrient)))
                self.tableWidget_bacteriaList.setItem(row_index, 3,
                                                      QtWidgets.QTableWidgetItem(str(bacteria.growth_rate)))
                self.tableWidget_bacteriaList.setItem(row_index, 4,
                                                      QtWidgets.QTableWidgetItem(str(bacteria.death_rate)))
                self.tableWidget_bacteriaList.setItem(row_index, 5,
                                                      QtWidgets.QTableWidgetItem(str(bacteria.competition_factor)))

            else:
                warning_box = QtWidgets.QMessageBox()
                warning_box.setText('Bacteria is already added to the simulation')
                warning_box.setIcon(QtWidgets.QMessageBox.Warning)
                return warning_box.exec()

    def _start_simulation_slot(self):
        if len(self._active_bacteria_list) == 0:
            warning_box = QtWidgets.QMessageBox()
            warning_box.setText('Cannot start simulation without at least 1 Bacteria selected')
            warning_box.setIcon(QtWidgets.QMessageBox.Critical)
            return warning_box.exec()

        if self._active_soil is None:
            warning_box = QtWidgets.QMessageBox()
            warning_box.setText('Cannot start simulation without selecting a Soil')
            warning_box.setIcon(QtWidgets.QMessageBox.Critical)
            return warning_box.exec()

        result = self._simulate_distribution()

        self._plot_distribution(result)
        self._plot_oxygen_availability()
        self._plot_nutrient_availability()

        if self.actionAdvanced_Charts.isChecked():
            dialog = QtWidgets.QDialog(parent=self)
            dialog.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint)
            dialog.setFixedHeight(640)
            dialog.setFixedWidth(640)

            chart = ChartWidget(self._active_bacteria_list, self._active_soil, self._depletion_function, parent=dialog)
            chart.show_graph(result)

            dialog.showNormal()

    def _remove_bacteria_clicked_slot(self):
        selected_row = self.tableWidget_bacteriaList.selectionModel().selectedRows()

        if len(selected_row) == 0:
            return

        index = selected_row[0].row()
        self.tableWidget_bacteriaList.removeRow(index)
        self._active_bacteria_list.pop(index)

    def _simulate_distribution(self, initial_population=10000):
        max_iterations = self._active_soil.max_depth

        population_dict = {bacteria.species_name: np.zeros(max_iterations) for bacteria in self._active_bacteria_list}
        for bacteria in self._active_bacteria_list:
            population_dict[bacteria.species_name][0] = initial_population  # Set initial population

        for iteration in range(1, max_iterations):
            total_population = 0  # Initialize total population at current depth

            for i, bacteria in enumerate(self._active_bacteria_list):
                # Check oxygen and nutrient requirements
                aerobic_threshold = 0.01
                if (bacteria.oxygen_requirement == EBacteriaType.AEROBIC and self._active_soil.oxygen_availability(
                        iteration, self._depletion_function) > aerobic_threshold) or \
                        (bacteria.oxygen_requirement in (EBacteriaType.ANAEROBIC, EBacteriaType.FACULTATIVE_ANAEROBIC)):
                    nutrient_availability = self._active_soil.nutrient_availability(iteration, self._depletion_function)
                    # Adjust growth rate based on nutrient availability (example)
                    growth_factor = min(nutrient_availability / bacteria.min_nutrient, 1.0)

                    # Adjust growth rate for low oxygen (aerobic bacteria only)
                    if bacteria.oxygen_requirement == EBacteriaType.AEROBIC:
                        oxygen_availability = self._active_soil.oxygen_availability(iteration, self._depletion_function)
                        if oxygen_availability <= aerobic_threshold:
                            # Example function: reduce growth to 10% at zero oxygen
                            growth_factor = 0.1 + (oxygen_availability / aerobic_threshold) * 0.9
                        else:
                            growth_factor = min(nutrient_availability / bacteria.min_nutrient, 1.0)

                    # Update population considering growth, death, and competition
                    current_population = population_dict[bacteria.species_name][iteration - 1]
                    total_population += current_population

                    # Consider competition factor from Bacteria class (assuming it exists)
                    growth_factor *= 1 / (1 + total_population / bacteria.competition_factor)

                    population_dict[bacteria.species_name][iteration] = current_population * (
                            1 + bacteria.growth_rate * growth_factor) - bacteria.death_rate * current_population

            # Reset total population for the next iteration
            total_population = 0

        return population_dict
