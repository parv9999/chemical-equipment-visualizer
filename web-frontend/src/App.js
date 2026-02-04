import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Bar, Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  LineElement,
  PointElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';
import 'bootstrap/dist/css/bootstrap.min.css';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  LineElement,
  PointElement,
  Title,
  Tooltip,
  Legend
);

const API_BASE = 'http://127.0.0.1:8000/api/';

axios.defaults.auth = {
  username: 'admin',
  password: 'admin123'
};

function App() {
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState(null);
  const [error, setError] = useState('');

  const handleUpload = async () => {
    if (!file) {
      setError('Please select a CSV file');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const res = await axios.post(API_BASE + 'upload/', formData);
      setSummary(res.data);
      setError('');
    } catch (err) {
      setError('Upload failed');
    }
  };

  return (
    <div className="container mt-4">
      <h2>Chemical Equipment Visualizer</h2>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <button className="btn btn-primary" onClick={handleUpload}>
        Upload CSV
      </button>

      {error && <p style={{ color: 'red' }}>{error}</p>}

      {summary && (
        <>
          <h3>Total Records: {summary.total_count}</h3>

          <Bar
            data={{
              labels: Object.keys(summary.type_distribution),
              datasets: [{
                label: 'Equipment Type Count',
                data: Object.values(summary.type_distribution),
                backgroundColor: 'rgba(75,192,192,0.6)'
              }]
            }}
          />

          <Line
            data={{
              labels: ['Flowrate', 'Pressure', 'Temperature'],
              datasets: [{
                label: 'Average Values',
                data: Object.values(summary.averages),
                borderColor: 'red'
              }]
            }}
          />
        </>
      )}
    </div>
  );
}

export default App;
