import sys
from application import Application
from main_window import MainWindow


def main():
    """
    Entry point for BioSim
    """

    # global app
    app = Application(argv=[])

    # global main_window
    main_window = MainWindow()
    main_window.show()

    exit_code = app.exec()

    del main_window
    del app

    sys.exit(exit_code)


if __name__ == '__main__':
    main()
