import sys
import requests
import pandas as pd

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QFileDialog, QLabel,
    QTableWidget, QTableWidgetItem
)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


API_UPLOAD = "http://127.0.0.1:8000/api/upload/"


class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chemical Equipment Visualizer (Desktop)")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.label = QLabel("Upload CSV file")
        layout.addWidget(self.label)

        self.button = QPushButton("Upload CSV")
        self.button.clicked.connect(self.upload_csv)
        layout.addWidget(self.button)

        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

    def upload_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open CSV", "", "CSV Files (*.csv)"
        )

        if not file_path:
            return

        files = {'file': open(file_path, 'rb')}
        response = requests.post(API_UPLOAD, files=files)

        if response.status_code != 200:
            self.label.setText("Upload failed")
            return

        data = response.json()
        self.label.setText(f"Total Records: {data['total_count']}")

        self.display_table(file_path)
        self.display_chart(data['type_distribution'])

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
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
