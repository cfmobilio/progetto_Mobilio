import sys
from PyQt5.QtWidgets import QApplication
from viste.home_view import HomeView

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = HomeView()
    main_window.show()
    sys.exit(app.exec_())
