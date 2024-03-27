# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QComboBox,
    QDoubleSpinBox, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(713, 393)
        self.action_startSimulation = QAction(MainWindow)
        self.action_startSimulation.setObjectName(u"action_startSimulation")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_simulation = QGroupBox(self.centralwidget)
        self.groupBox_simulation.setObjectName(u"groupBox_simulation")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_simulation.sizePolicy().hasHeightForWidth())
        self.groupBox_simulation.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_simulation)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.gridLayout_3.addWidget(self.groupBox_simulation, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.groupBox_bacteriaProperties = QGroupBox(self.centralwidget)
        self.groupBox_bacteriaProperties.setObjectName(u"groupBox_bacteriaProperties")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_bacteriaProperties.sizePolicy().hasHeightForWidth())
        self.groupBox_bacteriaProperties.setSizePolicy(sizePolicy1)
        self.groupBox_bacteriaProperties.setMinimumSize(QSize(0, 180))
        self.gridLayout = QGridLayout(self.groupBox_bacteriaProperties)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_competitionFactor = QLabel(self.groupBox_bacteriaProperties)
        self.label_competitionFactor.setObjectName(u"label_competitionFactor")

        self.verticalLayout_7.addWidget(self.label_competitionFactor)

        self.doubleSpinBox_competitionFactor = QDoubleSpinBox(self.groupBox_bacteriaProperties)
        self.doubleSpinBox_competitionFactor.setObjectName(u"doubleSpinBox_competitionFactor")
        self.doubleSpinBox_competitionFactor.setDecimals(5)

        self.verticalLayout_7.addWidget(self.doubleSpinBox_competitionFactor)


        self.gridLayout.addLayout(self.verticalLayout_7, 3, 1, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_deathRate = QLabel(self.groupBox_bacteriaProperties)
        self.label_deathRate.setObjectName(u"label_deathRate")
        self.label_deathRate.setMaximumSize(QSize(16777215, 28))

        self.verticalLayout_6.addWidget(self.label_deathRate)

        self.doubleSpinBox_deathRate = QDoubleSpinBox(self.groupBox_bacteriaProperties)
        self.doubleSpinBox_deathRate.setObjectName(u"doubleSpinBox_deathRate")
        self.doubleSpinBox_deathRate.setDecimals(5)

        self.verticalLayout_6.addWidget(self.doubleSpinBox_deathRate)


        self.gridLayout.addLayout(self.verticalLayout_6, 3, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_minNutrient = QLabel(self.groupBox_bacteriaProperties)
        self.label_minNutrient.setObjectName(u"label_minNutrient")
        self.label_minNutrient.setMaximumSize(QSize(16777215, 16))

        self.verticalLayout_4.addWidget(self.label_minNutrient)

        self.doubleSpinBox_minNutrient = QDoubleSpinBox(self.groupBox_bacteriaProperties)
        self.doubleSpinBox_minNutrient.setObjectName(u"doubleSpinBox_minNutrient")
        self.doubleSpinBox_minNutrient.setDecimals(5)

        self.verticalLayout_4.addWidget(self.doubleSpinBox_minNutrient)


        self.gridLayout.addLayout(self.verticalLayout_4, 1, 1, 1, 1)

        self.pushButton_insertBacteria = QPushButton(self.groupBox_bacteriaProperties)
        self.pushButton_insertBacteria.setObjectName(u"pushButton_insertBacteria")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_insertBacteria.sizePolicy().hasHeightForWidth())
        self.pushButton_insertBacteria.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton_insertBacteria, 3, 2, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_bacteria = QLabel(self.groupBox_bacteriaProperties)
        self.label_bacteria.setObjectName(u"label_bacteria")
        self.label_bacteria.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_bacteria.sizePolicy().hasHeightForWidth())
        self.label_bacteria.setSizePolicy(sizePolicy3)
        self.label_bacteria.setMinimumSize(QSize(0, 0))
        self.label_bacteria.setMaximumSize(QSize(16777215, 16))

        self.verticalLayout.addWidget(self.label_bacteria)

        self.comboBox_bacteria = QComboBox(self.groupBox_bacteriaProperties)
        self.comboBox_bacteria.setObjectName(u"comboBox_bacteria")

        self.verticalLayout.addWidget(self.comboBox_bacteria)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_growthRate = QLabel(self.groupBox_bacteriaProperties)
        self.label_growthRate.setObjectName(u"label_growthRate")
        self.label_growthRate.setMaximumSize(QSize(16777215, 16))

        self.verticalLayout_5.addWidget(self.label_growthRate)

        self.doubleSpinBox_growthRate = QDoubleSpinBox(self.groupBox_bacteriaProperties)
        self.doubleSpinBox_growthRate.setObjectName(u"doubleSpinBox_growthRate")
        self.doubleSpinBox_growthRate.setDecimals(5)
        self.doubleSpinBox_growthRate.setStepType(QAbstractSpinBox.DefaultStepType)

        self.verticalLayout_5.addWidget(self.doubleSpinBox_growthRate)


        self.gridLayout.addLayout(self.verticalLayout_5, 1, 2, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_name = QLabel(self.groupBox_bacteriaProperties)
        self.label_name.setObjectName(u"label_name")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy4)
        self.label_name.setMaximumSize(QSize(16777215, 16))

        self.verticalLayout_2.addWidget(self.label_name)

        self.lineEdit_name = QLineEdit(self.groupBox_bacteriaProperties)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.verticalLayout_2.addWidget(self.lineEdit_name)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_oxygenRequirements = QLabel(self.groupBox_bacteriaProperties)
        self.label_oxygenRequirements.setObjectName(u"label_oxygenRequirements")
        self.label_oxygenRequirements.setMaximumSize(QSize(16777215, 16))

        self.verticalLayout_3.addWidget(self.label_oxygenRequirements)

        self.comboBox_oxygenRequirements = QComboBox(self.groupBox_bacteriaProperties)
        self.comboBox_oxygenRequirements.setObjectName(u"comboBox_oxygenRequirements")

        self.verticalLayout_3.addWidget(self.comboBox_oxygenRequirements)


        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_bacteriaProperties)

        self.groupBox_soilProperties = QGroupBox(self.centralwidget)
        self.groupBox_soilProperties.setObjectName(u"groupBox_soilProperties")
        sizePolicy1.setHeightForWidth(self.groupBox_soilProperties.sizePolicy().hasHeightForWidth())
        self.groupBox_soilProperties.setSizePolicy(sizePolicy1)
        self.groupBox_soilProperties.setMinimumSize(QSize(0, 180))
        self.gridLayout_4 = QGridLayout(self.groupBox_soilProperties)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_o2DepletionRate = QLabel(self.groupBox_soilProperties)
        self.label_o2DepletionRate.setObjectName(u"label_o2DepletionRate")
        self.label_o2DepletionRate.setMaximumSize(QSize(16777215, 16))

        self.verticalLayout_10.addWidget(self.label_o2DepletionRate)

        self.doubleSpinBox_o2DepletionRate = QDoubleSpinBox(self.groupBox_soilProperties)
        self.doubleSpinBox_o2DepletionRate.setObjectName(u"doubleSpinBox_o2DepletionRate")
        self.doubleSpinBox_o2DepletionRate.setDecimals(5)

        self.verticalLayout_10.addWidget(self.doubleSpinBox_o2DepletionRate)


        self.gridLayout_4.addLayout(self.verticalLayout_10, 1, 0, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_maxDepth = QLabel(self.groupBox_soilProperties)
        self.label_maxDepth.setObjectName(u"label_maxDepth")
        self.label_maxDepth.setMaximumSize(QSize(16777215, 16))

        self.verticalLayout_9.addWidget(self.label_maxDepth)

        self.spinBox_maxDepth = QSpinBox(self.groupBox_soilProperties)
        self.spinBox_maxDepth.setObjectName(u"spinBox_maxDepth")
        self.spinBox_maxDepth.setMinimum(1)
        self.spinBox_maxDepth.setMaximum(500)

        self.verticalLayout_9.addWidget(self.spinBox_maxDepth)


        self.gridLayout_4.addLayout(self.verticalLayout_9, 0, 1, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_nutrientDepletionRate = QLabel(self.groupBox_soilProperties)
        self.label_nutrientDepletionRate.setObjectName(u"label_nutrientDepletionRate")
        self.label_nutrientDepletionRate.setMaximumSize(QSize(16777215, 16))

        self.verticalLayout_11.addWidget(self.label_nutrientDepletionRate)

        self.doubleSpinBox_nutrientDepletionRate = QDoubleSpinBox(self.groupBox_soilProperties)
        self.doubleSpinBox_nutrientDepletionRate.setObjectName(u"doubleSpinBox_nutrientDepletionRate")
        self.doubleSpinBox_nutrientDepletionRate.setDecimals(5)

        self.verticalLayout_11.addWidget(self.doubleSpinBox_nutrientDepletionRate)


        self.gridLayout_4.addLayout(self.verticalLayout_11, 1, 1, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_soilType = QLabel(self.groupBox_soilProperties)
        self.label_soilType.setObjectName(u"label_soilType")
        self.label_soilType.setMaximumSize(QSize(16777215, 16))

        self.verticalLayout_8.addWidget(self.label_soilType)

        self.comboBox_soilType = QComboBox(self.groupBox_soilProperties)
        self.comboBox_soilType.setObjectName(u"comboBox_soilType")

        self.verticalLayout_8.addWidget(self.comboBox_soilType)


        self.gridLayout_4.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.pushButton_useSoil = QPushButton(self.groupBox_soilProperties)
        self.pushButton_useSoil.setObjectName(u"pushButton_useSoil")

        self.gridLayout_4.addWidget(self.pushButton_useSoil, 2, 1, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_depletionFunction = QLabel(self.groupBox_soilProperties)
        self.label_depletionFunction.setObjectName(u"label_depletionFunction")
        self.label_depletionFunction.setMaximumSize(QSize(16777215, 16))

        self.verticalLayout_12.addWidget(self.label_depletionFunction)

        self.comboBox_depletionFunction = QComboBox(self.groupBox_soilProperties)
        self.comboBox_depletionFunction.setObjectName(u"comboBox_depletionFunction")

        self.verticalLayout_12.addWidget(self.comboBox_depletionFunction)


        self.gridLayout_4.addLayout(self.verticalLayout_12, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_soilProperties)

        self.groupBox_simulationData = QGroupBox(self.centralwidget)
        self.groupBox_simulationData.setObjectName(u"groupBox_simulationData")
        self.gridLayout_5 = QGridLayout(self.groupBox_simulationData)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tableWidget_bacteriaList = QTableWidget(self.groupBox_simulationData)
        self.tableWidget_bacteriaList.setObjectName(u"tableWidget_bacteriaList")
        self.tableWidget_bacteriaList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_bacteriaList.setAlternatingRowColors(True)
        self.tableWidget_bacteriaList.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.tableWidget_bacteriaList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_bacteriaList.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_bacteriaList.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.gridLayout_5.addWidget(self.tableWidget_bacteriaList, 0, 0, 1, 1)

        self.pushButton_removeBacteria = QPushButton(self.groupBox_simulationData)
        self.pushButton_removeBacteria.setObjectName(u"pushButton_removeBacteria")

        self.gridLayout_5.addWidget(self.pushButton_removeBacteria, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_simulationData)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 2)

        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setRowStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 713, 22))
        self.menuSimulation = QMenu(self.menubar)
        self.menuSimulation.setObjectName(u"menuSimulation")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label_competitionFactor.setBuddy(self.doubleSpinBox_competitionFactor)
        self.label_deathRate.setBuddy(self.doubleSpinBox_deathRate)
        self.label_minNutrient.setBuddy(self.doubleSpinBox_minNutrient)
        self.label_bacteria.setBuddy(self.comboBox_bacteria)
        self.label_growthRate.setBuddy(self.doubleSpinBox_growthRate)
        self.label_name.setBuddy(self.lineEdit_name)
        self.label_oxygenRequirements.setBuddy(self.comboBox_oxygenRequirements)
        self.label_o2DepletionRate.setBuddy(self.doubleSpinBox_o2DepletionRate)
        self.label_maxDepth.setBuddy(self.spinBox_maxDepth)
        self.label_nutrientDepletionRate.setBuddy(self.doubleSpinBox_nutrientDepletionRate)
        self.label_soilType.setBuddy(self.comboBox_soilType)
        self.label_depletionFunction.setBuddy(self.comboBox_depletionFunction)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.comboBox_bacteria, self.lineEdit_name)
        QWidget.setTabOrder(self.lineEdit_name, self.comboBox_oxygenRequirements)
        QWidget.setTabOrder(self.comboBox_oxygenRequirements, self.doubleSpinBox_minNutrient)
        QWidget.setTabOrder(self.doubleSpinBox_minNutrient, self.doubleSpinBox_growthRate)
        QWidget.setTabOrder(self.doubleSpinBox_growthRate, self.doubleSpinBox_deathRate)
        QWidget.setTabOrder(self.doubleSpinBox_deathRate, self.doubleSpinBox_competitionFactor)
        QWidget.setTabOrder(self.doubleSpinBox_competitionFactor, self.pushButton_insertBacteria)
        QWidget.setTabOrder(self.pushButton_insertBacteria, self.comboBox_soilType)
        QWidget.setTabOrder(self.comboBox_soilType, self.spinBox_maxDepth)
        QWidget.setTabOrder(self.spinBox_maxDepth, self.doubleSpinBox_o2DepletionRate)
        QWidget.setTabOrder(self.doubleSpinBox_o2DepletionRate, self.doubleSpinBox_nutrientDepletionRate)
        QWidget.setTabOrder(self.doubleSpinBox_nutrientDepletionRate, self.comboBox_depletionFunction)

        self.menubar.addAction(self.menuSimulation.menuAction())
        self.menuSimulation.addAction(self.action_startSimulation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_startSimulation.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.groupBox_simulation.setTitle(QCoreApplication.translate("MainWindow", u"Simulation", None))
        self.groupBox_bacteriaProperties.setTitle(QCoreApplication.translate("MainWindow", u"Bacteria Properties", None))
        self.label_competitionFactor.setText(QCoreApplication.translate("MainWindow", u"Competition Factor", None))
        self.label_deathRate.setText(QCoreApplication.translate("MainWindow", u"Death Rate", None))
        self.label_minNutrient.setText(QCoreApplication.translate("MainWindow", u"Min Nutrient", None))
        self.pushButton_insertBacteria.setText(QCoreApplication.translate("MainWindow", u"INSERT", None))
        self.label_bacteria.setText(QCoreApplication.translate("MainWindow", u"Bacteria", None))
        self.label_growthRate.setText(QCoreApplication.translate("MainWindow", u"Growth Rate", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_oxygenRequirements.setText(QCoreApplication.translate("MainWindow", u"Oxygen Requirements", None))
        self.groupBox_soilProperties.setTitle(QCoreApplication.translate("MainWindow", u"Soil Properties", None))
        self.label_o2DepletionRate.setText(QCoreApplication.translate("MainWindow", u"O\u00b2 Depletion Rate", None))
        self.label_maxDepth.setText(QCoreApplication.translate("MainWindow", u"Max Depth", None))
        self.label_nutrientDepletionRate.setText(QCoreApplication.translate("MainWindow", u"Nutrient Depletion Rate", None))
        self.label_soilType.setText(QCoreApplication.translate("MainWindow", u"Soil Type", None))
        self.pushButton_useSoil.setText(QCoreApplication.translate("MainWindow", u"USE", None))
        self.label_depletionFunction.setText(QCoreApplication.translate("MainWindow", u"Depletion Simulation Function", None))
        self.groupBox_simulationData.setTitle(QCoreApplication.translate("MainWindow", u"Simulation Data", None))
        self.pushButton_removeBacteria.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.menuSimulation.setTitle(QCoreApplication.translate("MainWindow", u"Simulation", None))
    # retranslateUi

