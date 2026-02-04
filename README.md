🧪 Chemical Equipment Visualizer

A Web + Desktop Based Data Analysis & Visualization System

📌 Project Overview

The Chemical Equipment Visualizer is a full-stack data analysis application designed to analyze chemical plant equipment data from CSV files and generate meaningful insights such as:

Equipment count
Type distribution
Average flowrate, pressure, and temperature
Tabular visualization
Graphical charts
Downloadable PDF report

The project includes:
🌐 Web backend (Django REST API)
🖥️ Desktop application (PyQt5)
📊 Data analysis using Pandas
📄 PDF report generation

This project demonstrates real-world data handling, API integration, and multi-platform visualization, making it suitable for industry and academic evaluation.

🏗️ System Architecture
CSV File
   ↓
Desktop App (PyQt5)
   ↓  (POST request)
Django REST API
   ↓
Data Processing (Pandas)
   ↓
JSON Summary + PDF Report

🚀 Features
✅ Backend (Django REST Framework)
Upload CSV files via API
Validate and process equipment data
Calculate:
   Total equipment count
  Equipment type distribution
   Average flowrate
   Average pressure
   Average temperature
   Generate downloadable PDF report

✅ Desktop Application (PyQt5)
Modern dashboard UI
CSV file upload
Tabular display of dataset
Bar chart visualization of equipment types
Summary metrics display
One-click PDF report download

✅ Data Visualization
Table view for full dataset
Bar chart for equipment distribution
Clean and readable PDF report

📂 Project Structure
chemical-equipment-visualizer/
│
├── backend/
│   ├── backend/
│   │   ├── settings.py
│   │   ├── urls.py
│   │
│   ├── api/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │
│   └── manage.py
│
├── desktop/
│   └── main.py
│
├── sample_data.csv
├── requirements.txt
└── README.md


📄 CSV File Format

The application expects the CSV file in the following format:

Equipment Name,Type,Flowrate,Pressure,Temperature
Pump-1,Pump,120,5.2,110
Compressor-1,Compressor,95,8.4,95
Valve-1,Valve,60,4.1,105

Column Description
Column	Description
Equipment Name	Name of the equipment
Type	Equipment category
Flowrate	Flow rate value
Pressure	Operating pressure
Temperature	Operating temperature

🛠️ Technologies Used
Backend

Python 3
Django
Django REST Framework
Pandas
ReportLab (PDF generation)

Desktop App
PyQt5
Requests
Matplotlib

Tools
Git & GitHub
VS Code

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/parv9999/chemical-equipment-visualizer.git
cd chemical-equipment-visualizer

2️⃣ Backend Setup
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Backend will run at:

http://127.0.0.1:8000/

3️⃣ Desktop Application Setup
cd desktop
pip install pyqt5 pandas matplotlib requests
python main.py

🔌 API Endpoints
Endpoint	Method	Description
/api/upload/	POST	Upload CSV & get summary
/api/summary/	GET	Recent dataset summaries
/api/report/	GET	Download PDF report
📊 Output Examples
✔ Dashboard Summary

Total Records
Average Flowrate
Average Pressure
Average Temperature

✔ Visualizations

Equipment type bar chart
Data table view

✔ PDF Report

Title & metadata
Equipment summary
Ready for academic submission

🎯 Use Cases

Chemical plant data analysis
Academic project submission (FOSSEE / University)
Learning Django REST APIs
Learning Desktop–Backend integration
Beginner-friendly real-world project

📌 Learning Outcomes

REST API development
CSV data processing
Desktop UI design
Client-server architecture
Git & GitHub workflow
PDF report automation

🔮 Future Enhancements

Authentication & user roles
Advanced charts (line, pie)
Cloud deployment
Database analytics dashboard
Equipment health prediction using ML

👨‍💻 Author

Parv Chauhan
B.Tech Computer Science
VIT Bhopal University

📌 This project was built as part of academic and skill-development work.
