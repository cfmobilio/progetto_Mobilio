from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QComboBox


class ReportViewer(QWidget):
    def __init__(self, amministratore):
        super(ReportViewer, self).__init__()
        self.amministratore = amministratore
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('MangiAmo - Visualizza Report')
        self.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: black;
            }
            QPushButton {
                font-size: 16px;
                padding: 10px 20px;
                background-color: white;
                color: black;
                border: 1px solid #ddd;
                border-radius: 5px;
                min-width: 200px;
                min-height: 40px;
                text-align: left;
                padding-left: 30px;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
        """)

        layout = QVBoxLayout()

        self.tipo_report_combo = QComboBox()
        self.tipo_report_combo.addItems(["Report Prenotazioni", "Report Scorte", "Report Abbonamenti"])
        layout.addWidget(self.tipo_report_combo)

        self.visualizza_report_button = QPushButton("Visualizza")
        self.visualizza_report_button.clicked.connect(self.mostra_report)
        layout.addWidget(self.visualizza_report_button)

        self.setLayout(layout)

    def mostra_report(self):
        global report_text
        tipo_report = self.tipo_report_combo.currentText()

        if tipo_report == "Report Prenotazioni":
            report = self.amministratore.visualizza_report_prenotazioni()
            report_text = f"Prenotazioni Totali: {report['prenotazioni_totali']}\n"
        elif tipo_report == "Report Scorte":
            report = self.amministratore.visualizza_report_scorte()

            if not report['scorte']:
                QMessageBox.information(self, "Report", "Non ci sono scorte disponibili.")
                return
            scorte_text = "\n".join(
                [f"{ingrediente}: {quantita}" for ingrediente, quantita in report['scorte'].items()])
            report_text = f"Scorte:\n{scorte_text}\n"

        elif tipo_report == "Report Abbonamenti":
            report = self.amministratore.visualizza_report_abbonamenti()
            report_text = f"Abbonamenti Attivi: {report['abbonamenti_attivi']}"

        QMessageBox.information(self, "Report", report_text)
