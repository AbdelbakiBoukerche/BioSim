from typing import List
from PySide6 import QtWidgets


class Application(QtWidgets.QApplication):
    def __init__(self, argv: List[str]):
        super().__init__(argv)

        self.setDesktopFileName('BioSim')
        self.setOrganizationName('ABDELBAKI Boukerche')
        self.setApplicationName('BioSim')
        self.setApplicationVersion('1.0.0')
