# 🧪 Chemical Equipment Visualizer

## 🌐 Live Deployment

**Frontend:**
[Chemical Equipment Visualizer Frontend](https://chemical-eq-visualizer-fossee-frontend.onrender.com?utm_source=chatgpt.com)

**Backend API:**
[Chemical Equipment Visualizer Backend API](https://chemical-equipment-visualizer-2-ezia.onrender.com?utm_source=chatgpt.com)

---

# 📌 Project Overview

Chemical Equipment Visualizer is a full-stack industrial data analysis and visualization platform developed for processing and analyzing chemical plant equipment datasets from CSV files.

The system enables engineers and users to upload industrial equipment datasets, perform automated statistical analysis, generate visual insights, and export professional PDF reports.

The project combines:

* 🌐 Web Backend using Django REST Framework
* 🖥️ Desktop GUI Application using PyQt5
* 📊 Data Analytics using Pandas
* 📈 Visualization using Matplotlib
* 📄 Automated PDF Report Generation

This project demonstrates real-world software engineering concepts including REST API development, desktop-to-server communication, industrial data processing, and analytical reporting workflows.

---

# 🚀 Key Features

## ✅ Backend (Django REST Framework)

* CSV file upload via REST API
* Equipment dataset validation & processing
* Automated analytical computations:

  * Total equipment count
  * Equipment category distribution
  * Average flowrate
  * Average pressure
  * Average temperature
* JSON-based API responses
* Automated downloadable PDF report generation

---

## ✅ Desktop Application (PyQt5)

* Modern desktop dashboard interface
* CSV dataset upload support
* Interactive tabular dataset visualization
* Graphical equipment analytics
* Real-time summary statistics
* One-click PDF report download

---

## ✅ Data Visualization & Reporting

* Equipment distribution charts
* Interactive data tables
* Statistical summaries
* Professionally formatted PDF reports

---

# 🏗️ System Architecture

```
CSV Dataset
     ↓
Desktop Application (PyQt5)
     ↓  REST API Request
Django Backend API
     ↓
Data Processing Engine (Pandas)
     ↓
Analytics + Visualization + PDF Report
```

---

# 📂 Project Structure

```
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
```

---

# 📄 Expected CSV Format

```
Equipment Name,Type,Flowrate,Pressure,Temperature
Pump-1,Pump,120,5.2,110
Compressor-1,Compressor,95,8.4,95
Valve-1,Valve,60,4.1,105
```

---

# 📊 Analytical Metrics Generated

The platform automatically computes:

* Total Equipment Records
* Equipment Type Distribution
* Average Flowrate
* Average Pressure
* Average Temperature

---

# 🛠️ Technologies Used

## Backend Technologies

* Python 3
* Django
* Django REST Framework
* Pandas
* ReportLab

## Desktop Application

* PyQt5
* Requests
* Matplotlib

## Development Tools

* Git & GitHub
* VS Code
* Render Cloud Deployment

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```
git clone https://github.com/parv9999/chemical-equipment-visualizer.git

cd chemical-equipment-visualizer
```

---

## 2️⃣ Backend Setup

```
cd backend

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

Backend runs at:

```
http://127.0.0.1:8000/
```

---

## 3️⃣ Desktop Application Setup

```
cd desktop

pip install pyqt5 pandas matplotlib requests

python main.py
```

---

# 🔌 REST API Endpoints

| EndpointMethodDescription |      |                                 |
| ------------------------- | ---- | ------------------------------- |
| `/api/upload/`            | POST | Upload CSV & generate analytics |
| `/api/summary/`           | GET  | Retrieve dataset summaries      |
| `/api/report/`            | GET  | Download generated PDF report   |

---

# 📈 Output Capabilities

## ✔ Dashboard Analytics

* Total Equipment Count
* Flowrate Analysis
* Pressure Analysis
* Temperature Analysis

## ✔ Visual Insights

* Equipment Distribution Charts
* Tabular Dataset Representation

## ✔ Exportable Reports

* Automated PDF generation
* Structured industrial summaries
* Academic & industry-ready documentation

---

# 🎯 Real-World Use Cases

* Chemical plant equipment analysis
* Industrial operational monitoring
* Engineering dataset visualization
* Academic research projects
* REST API learning projects
* Desktop-to-backend integration systems

---

# 📚 Learning Outcomes

This project demonstrates practical understanding of:

* REST API Development
* Full-Stack Application Architecture
* Industrial Data Processing
* Desktop GUI Development
* Client-Server Communication
* Data Visualization
* Automated Report Generation
* Software Deployment Workflows

---

# 🔮 Future Enhancements

* User Authentication & Authorization
* Cloud Deployment on AWS
* Advanced Interactive Dashboards
* Real-Time Equipment Monitoring
* Database Integration
* Predictive Maintenance using Machine Learning
* Equipment Health Forecasting

---

# 👨‍💻 Author

**Parv Chauhan**
B.Tech Computer Science
VIT Bhopal University

---

# 📌 Project Status

✅ Fully Functional
✅ Frontend & Backend Deployed
✅ Industrial Dataset Analysis Supported
✅ PDF Report Generation Implemented
✅ Ready for Academic & Portfolio Showcase
