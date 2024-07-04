from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                             QLabel, QPushButton, QSpacerItem,
                             QSizePolicy, QStackedWidget, QGridLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys


class WelcomeView(QWidget):
    def __init__(self, parent=None):
        super(WelcomeView, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('MangiAmo')
        self.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
                color: black;
            }
            QPushButton {
                font-size: 16px;
                padding: 10px 20px;
                background-color: #FF0000;
                color: white;
                border: none;
                border-radius: 5px;
                min-width: 150px;
                min-height: 40px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)

        layout = QVBoxLayout()

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Aggiungi il QLabel per il logo
        self.logo_image_label = QLabel(self)
        pixmap = QPixmap('icone/logo.png')
        scaled_pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logo_image_label.setPixmap(scaled_pixmap)
        self.logo_image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.logo_image_label)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.mostra_login)
        layout.addWidget(self.login_button, alignment=Qt.AlignCenter)

        self.registrazione_button = QPushButton('Registrati')
        self.registrazione_button.clicked.connect(self.mostra_registrazione)
        layout.addWidget(self.registrazione_button, alignment=Qt.AlignCenter)

        # Spaziatore per centrare verticalmente i pulsanti
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(layout)

    def mostra_login(self):
        self.parentWidget().setCurrentIndex(1)

    def mostra_registrazione(self):
        self.parentWidget().setCurrentIndex(2)
