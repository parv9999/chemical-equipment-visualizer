import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Bar, Line } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, LineElement, PointElement, Title, Tooltip, Legend } from 'chart.js';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Tabs, Tab, Alert, Spinner, Card, Button, Table } from 'react-bootstrap';

ChartJS.register(CategoryScale, LinearScale, BarElement, LineElement, PointElement, Title, Tooltip, Legend);

const API_BASE = "https://chemical-equipment-visualizer-2-ezia.onrender.com/api/";

axios.defaults.auth = { username: 'admin', password: 'admin123' };

function App() {
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState(null);
  const [history, setHistory] = useState([]);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchHistory();
  }, []);

  const fetchHistory = async () => {
    try {
      setLoading(true);
      const res = await axios.get(API_BASE + 'summary/');
      const data = Array.isArray(res.data) ? res.data : [];
      setHistory(data);
      setError('');
    } catch (err) {
      console.error('Fetch history failed:', err);
      setHistory([]);
      setError('Could not load history (is backend running?)');
    } finally {
      setLoading(false);
    }
  };

  const handleUpload = async () => {
    if (!file) {
      setError('Please select a CSV file first');
      return;
    }
    setLoading(true);
    setError('');
    const formData = new FormData();
    formData.append('file', file);
    try {
      const res = await axios.post(API_BASE + 'upload/', formData);
      setSummary(res.data || null);
      await fetchHistory();
    } catch (err) {
      setError(
  'Upload failed: ' +
  (err.response?.data?.error ||
   err.response?.data?.detail ||
   err.response?.data?.message ||
   err.response?.data?.toString() ||
   err.response?.statusText ||
   err.message ||
   'Unknown server error - check browser console (F12)')
);
    } finally {
      setLoading(false);
    }
  };

  const downloadPDF = () => {
    window.open(API_BASE + 'report/');
  };

  // Safe chart data preparation
  const getTypeData = () => {
    if (!summary?.type_distribution) return null;
    return {
      labels: Object.keys(summary.type_distribution),
      datasets: [{
        label: 'Type Distribution',
        data: Object.values(summary.type_distribution),
        backgroundColor: 'rgba(75,192,192,0.6)',
      }]
    };
  };

  const getAvgData = () => {
    if (!summary?.averages) return null;
    return {
      labels: ['Flowrate', 'Pressure', 'Temperature'],
      datasets: [{
        label: 'Averages',
        data: Object.values(summary.averages),
        borderColor: 'rgb(255,99,132)',
        tension: 0.1,
      }]
    };
  };

  const typeData = getTypeData();
  const avgData = getAvgData();

  return (
    <div className="container mt-5">
      <h1 className="text-center mb-4 text-primary">Chemical Equipment Visualizer (Web)</h1>

      {error && <Alert variant="danger" onClose={() => setError('')} dismissible>{error}</Alert>}

      <Card className="mb-4 shadow-sm">
        <Card.Body>
          <div className="d-flex align-items-center gap-3 flex-wrap">
            <input
              type="file"
              accept=".csv"
              className="form-control"
              onChange={(e) => setFile(e.target.files?.[0] || null)}
            />
            <Button
              variant="primary"
              onClick={handleUpload}
              disabled={loading || !file}
            >
              {loading ? (
                <>
                  <Spinner animation="border" size="sm" className="me-2" />
                  Processing...
                </>
              ) : (
                'Upload & Analyze'
              )}
            </Button>
          </div>
        </Card.Body>
      </Card>

      {loading && <div className="text-center my-5"><Spinner animation="border" variant="primary" /><p>Loading...</p></div>}

      <Tabs defaultActiveKey="summary" id="app-tabs" className="mb-4" fill>
        <Tab eventKey="summary" title="Summary">
          {summary ? (
            <Card className="shadow-sm">
              <Card.Body>
                <h4 className="mb-3">Analysis Results</h4>
                <p className="lead">Total Equipment: <strong>{summary.total_count ?? '—'}</strong></p>

                <h5>Averages</h5>
                <ul className="list-group list-group-flush mb-3">
                  {summary.averages && Object.entries(summary.averages).map(([key, value]) => (
                    <li key={key} className="list-group-item">
                      {key}: <strong>{Number(value).toFixed(2)}</strong>
                    </li>
                  )) || <li className="list-group-item text-muted">No averages available</li>}
                </ul>

                <h5>Type Distribution</h5>
                <ul className="list-group list-group-flush mb-4">
                  {summary.type_distribution && Object.entries(summary.type_distribution).map(([type, count]) => (
                    <li key={type} className="list-group-item">
                      {type}: <strong>{count}</strong>
                    </li>
                  )) || <li className="list-group-item text-muted">No distribution data</li>}
                </ul>

                <Button variant="success" onClick={downloadPDF}>
                  Download PDF Report
                </Button>
              </Card.Body>
            </Card>
          ) : (
            <div className="alert alert-info text-center py-4">
              Upload a CSV file to see summary statistics.
            </div>
          )}
        </Tab>

        <Tab eventKey="charts" title="Charts">
          {summary && typeData && avgData ? (
            <div className="row g-4">
              <div className="col-md-6">
                <Card className="shadow-sm h-100">
                  <Card.Body>
                    <Bar data={typeData} options={{ responsive: true, plugins: { title: { display: true, text: 'Equipment Type Distribution' } } }} />
                  </Card.Body>
                </Card>
              </div>
              <div className="col-md-6">
                <Card className="shadow-sm h-100">
                  <Card.Body>
                    <Line data={avgData} options={{ responsive: true, plugins: { title: { display: true, text: 'Average Parameters' } } }} />
                  </Card.Body>
                </Card>
              </div>
            </div>
          ) : (
            <div className="alert alert-info text-center py-4">
              Analyze a file to view charts.
            </div>
          )}
        </Tab>

        <Tab eventKey="history" title="History (Last 5)">
          {history.length > 0 ? (
            <Table striped bordered hover responsive>
              <thead className="table-dark">
                <tr>
                  <th>#</th>
                  <th>Total</th>
                  <th>Avg Flow / Press / Temp</th>
                  <th>Types</th>
                </tr>
              </thead>
              <tbody>
                {history.map((s, i) => (
                  <tr key={i}>
                    <td>{i + 1}</td>
                    <td>{s.total_count ?? '—'}</td>
                    <td>
                      {s.averages
                        ? Object.values(s.averages).map(v => Number(v).toFixed(2)).join(' / ')
                        : '—'}
                    </td>
                    <td>
                      {s.type_distribution
                        ? Object.entries(s.type_distribution).map(([k, v]) => `${k}: ${v}`).join(', ')
                        : '—'}
                    </td>
                  </tr>
                ))}
              </tbody>
            </Table>
          ) : (
            <div className="alert alert-info text-center py-4">
              No previous uploads found.
            </div>
          )}
        </Tab>
      </Tabs>
    </div>
  );
}

export default App;