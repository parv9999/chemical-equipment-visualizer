import sys
import requests
import pandas as pd
import matplotlib
matplotlib.use("Qt5Agg")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QFileDialog, QLabel, QTableWidget,
    QTableWidgetItem, QMessageBox, QGroupBox
)
from PyQt5.QtCore import Qt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

# ================= API CONFIG =================

API_BASE = "https://chemical-equipment-visualizer-2-ezia.onrender.com/api/"
API_UPLOAD = API_BASE + "upload/"
API_REPORT = API_BASE + "report/"

# =============================================


class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chemical Equipment Visualizer – Desktop")
        self.setGeometry(100, 100, 1000, 700)

        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)

        # ===== Header =====
        title = QLabel("Chemical Equipment Analysis Dashboard")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        main_layout.addWidget(title)

        self.status_label = QLabel("Upload a CSV file to begin")
        self.status_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.status_label)

        # ===== Buttons =====
        btn_layout = QHBoxLayout()

        self.upload_btn = QPushButton("Upload CSV")
        self.upload_btn.clicked.connect(self.upload_csv)
        btn_layout.addWidget(self.upload_btn)

        self.pdf_btn = QPushButton("Download PDF Report")
        self.pdf_btn.setEnabled(False)
        self.pdf_btn.clicked.connect(self.download_pdf)
        btn_layout.addWidget(self.pdf_btn)

        main_layout.addLayout(btn_layout)

        # ===== Summary Box =====
        summary_box = QGroupBox("Summary")
        summary_layout = QHBoxLayout()

        self.total_label = QLabel("Total Records: -")
        self.flow_label = QLabel("Avg Flowrate: -")
        self.pressure_label = QLabel("Avg Pressure: -")
        self.temp_label = QLabel("Avg Temperature: -")

        for lbl in [
            self.total_label,
            self.flow_label,
            self.pressure_label,
            self.temp_label
        ]:
            lbl.setStyleSheet("font-weight: bold;")
            summary_layout.addWidget(lbl)

        summary_box.setLayout(summary_layout)
        main_layout.addWidget(summary_box)

        # ===== Table =====
        self.table = QTableWidget()
        self.table.horizontalHeader().setStretchLastSection(True)
        main_layout.addWidget(self.table, stretch=2)

        # ===== Chart =====
        self.figure = Figure(figsize=(5, 3))
        self.canvas = FigureCanvasQTAgg(self.figure)
        main_layout.addWidget(self.canvas, stretch=1)

        self.setLayout(main_layout)

    # ================== LOGIC ==================

    def upload_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select CSV File", "", "CSV Files (*.csv)"
        )

        if not file_path:
            return

        self.status_label.setText("Uploading CSV...")

        try:
            with open(file_path, "rb") as f:
                response = requests.post(
                    API_UPLOAD,
                    files={"file": f},
                    timeout=120
                )

            if response.status_code != 200:
                raise Exception(
                    f"API Error {response.status_code}\n{response.text}"
                )

            data = response.json()

            # Update summary
            avg = data.get("averages", {})

            self.total_label.setText(f"Total Records: {data.get('total_count', '-')}")
            self.flow_label.setText(f"Avg Flowrate: {avg.get('flowrate', 'N/A')}")
            self.pressure_label.setText(f"Avg Pressure: {avg.get('pressure', 'N/A')}")
            self.temp_label.setText(f"Avg Temperature: {avg.get('temperature', 'N/A')}")

            self.display_table(file_path)
            self.display_chart(data.get("type_distribution", {}))

            self.pdf_btn.setEnabled(True)
            self.status_label.setText("Upload successful")

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            self.status_label.setText("Upload failed")

    def download_pdf(self):
        save_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save PDF",
            "chemical_equipment_report.pdf",
            "PDF Files (*.pdf)"
        )

        if not save_path:
            return

        try:
            response = requests.get(API_REPORT, timeout=30)

            if response.status_code != 200:
                raise Exception("Failed to download PDF")

            with open(save_path, "wb") as f:
                f.write(response.content)

            QMessageBox.information(
                self,
                "Success",
                "PDF downloaded successfully"
            )

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def display_table(self, file_path):
        df = pd.read_csv(file_path)

        self.table.setRowCount(len(df))
        self.table.setColumnCount(len(df.columns))
        self.table.setHorizontalHeaderLabels(df.columns)

        for i in range(len(df)):
            for j in range(len(df.columns)):
                self.table.setItem(
                    i, j, QTableWidgetItem(str(df.iat[i, j]))
                )

    def display_chart(self, type_distribution):
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        ax.bar(
            type_distribution.keys(),
            type_distribution.values()
        )
        ax.set_title("Equipment Type Distribution")
        ax.set_ylabel("Count")

        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
