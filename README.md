# 🧪 Chemical Equipment Visualizer

[![Frontend](https://img.shields.io/badge/Frontend-Live-brightgreen?style=for-the-badge&logo=render)](https://chemical-eq-visualizer-fossee-frontend.onrender.com)
[![Backend API](https://img.shields.io/badge/Backend%20API-Live-blue?style=for-the-badge&logo=render)](https://chemical-equipment-visualizer-2-ezia.onrender.com)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PyQt5](https://img.shields.io/badge/PyQt5-Desktop%20GUI-41CD52?style=for-the-badge&logo=qt&logoColor=white)

> A full-stack industrial data analysis and visualization platform for processing chemical plant equipment datasets — combining a Django REST API backend with a PyQt5 desktop application.

---

## 🌐 Live Deployment

| Service | URL |
|---|---|
| 🖥️ Frontend | [chemical-eq-visualizer-fossee-frontend.onrender.com](https://chemical-eq-visualizer-fossee-frontend.onrender.com) |
| ⚙️ Backend API | [chemical-equipment-visualizer-2-ezia.onrender.com](https://chemical-equipment-visualizer-2-ezia.onrender.com) |

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [CSV Format](#expected-csv-format)
- [API Endpoints](#rest-api-endpoints)
- [Getting Started](#getting-started)
- [Output Capabilities](#output-capabilities)
- [Future Enhancements](#future-enhancements)
- [Author](#author)

---

## 📖 Overview

**Chemical Equipment Visualizer** enables engineers to upload industrial equipment datasets (CSV), perform automated statistical analysis, generate visual insights, and export professional PDF reports — all through a clean desktop GUI or REST API.

The project combines:
- 🌐 **Django REST Framework** — Web backend & API
- 🖥️ **PyQt5** — Desktop GUI application
- 📊 **Pandas** — Data analytics engine
- 📈 **Matplotlib** — Data visualization
- 📄 **ReportLab** — Automated PDF report generation

---

## 🚀 Key Features

### ⚙️ Backend (Django REST Framework)
- CSV file upload via REST API
- Equipment dataset validation & processing
- Automated analytical computations:
  - Total equipment count
  - Equipment category distribution
  - Average flowrate, pressure & temperature
- JSON-based API responses
- Downloadable PDF report generation

### 🖥️ Desktop Application (PyQt5)
- Modern dashboard interface
- CSV dataset upload support
- Interactive tabular dataset visualization
- Graphical equipment analytics
- Real-time summary statistics
- One-click PDF report download

### 📊 Data Visualization & Reporting
- Equipment distribution charts
- Interactive data tables
- Statistical summaries
- Professionally formatted PDF reports

---

## 🏗️ System Architecture

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

## 🛠️ Tech Stack

| Layer | Technologies |
|---|---|
| **Backend** | Python 3, Django, Django REST Framework |
| **Data Processing** | Pandas |
| **PDF Generation** | ReportLab |
| **Desktop GUI** | PyQt5, Matplotlib |
| **HTTP Client** | Requests |
| **Deployment** | Render Cloud |
| **Dev Tools** | Git, GitHub, VS Code |

---

## 📁 Project Structure

```
chemical-equipment-visualizer/
│
├── backend/
│   ├── backend/
│   │   ├── settings.py
│   │   └── urls.py
│   │
│   ├── api/
│   │   ├── models.py
│   │   ├── views.py
│   │   └── urls.py
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

## 📄 Expected CSV Format

```csv
Equipment Name,Type,Flowrate,Pressure,Temperature
Pump-1,Pump,120,5.2,110
Compressor-1,Compressor,95,8.4,95
Valve-1,Valve,60,4.1,105
```

---

## 🔌 REST API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/upload/` | Upload CSV & generate analytics |
| `GET` | `/api/summary/` | Retrieve dataset summaries |
| `GET` | `/api/report/` | Download generated PDF report |

---

## ⚙️ Getting Started

### Prerequisites
- Python 3.8+
- pip

### 1. Clone the Repository

```bash
git clone https://github.com/parv9999/chemical-equipment-visualizer.git
cd chemical-equipment-visualizer
```

### 2. Backend Setup

```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Backend runs at → `http://127.0.0.1:8000/`

### 3. Desktop Application Setup

```bash
cd desktop
pip install pyqt5 pandas matplotlib requests
python main.py
```

---

## 📈 Output Capabilities

### ✅ Dashboard Analytics
- Total Equipment Count
- Flowrate, Pressure & Temperature Analysis

### ✅ Visual Insights
- Equipment Distribution Charts
- Tabular Dataset Representation

### ✅ Exportable Reports
- Automated PDF generation
- Structured industrial summaries
- Academic & industry-ready documentation

---

## 🎯 Real-World Use Cases

- Chemical plant equipment analysis
- Industrial operational monitoring
- Engineering dataset visualization
- Academic research projects
- REST API & desktop-to-backend integration learning

---

## 🔮 Future Enhancements

- [ ] User Authentication & Authorization
- [ ] Advanced Interactive Dashboards
- [ ] Real-Time Equipment Monitoring
- [ ] Database Integration
- [ ] Predictive Maintenance using Machine Learning
- [ ] Equipment Health Forecasting
- [ ] Cloud Deployment on AWS

---

## 📌 Project Status

| Feature | Status |
|---|---|
| Frontend & Backend Deployed | ✅ |
| Industrial Dataset Analysis | ✅ |
| PDF Report Generation | ✅ |
| Desktop GUI Application | ✅ |
| Portfolio & Academic Ready | ✅ |

---

## 👨‍💻 Author

**Parv Chauhan**
B.Tech Computer Science — VIT Bhopal University

- GitHub: [@parv9999](https://github.com/parv9999)

---

<p align="center">⚗️ Bringing data analytics to industrial chemical engineering workflows</p>
