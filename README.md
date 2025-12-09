# Benchmark Web UI

A Flask-based Web Interface for the Compute-Intensive Benchmarking Suite

## Overview

Benchmark Web UI is a lightweight Flask application that provides a browser-based interface for running compute-intensive performance benchmarks.
It serves as a front-end to the Compute-Intensive Benchmarking Suite, which implements several multiprocessing strategies in Python.

The web app allows users to:

+ Select a compute algorithm (e.g., prime checking, Fibonacci)
+ Choose a multiprocessing method (map, apply, apply_async, chunked async, or single-process)
+ Configure benchmark parameters (range limit, number of processes)
+ Run the benchmark directly in the browser
+ View the computed elapsed time
+ Automatically store each benchmark run in a SQLite database

This project demonstrates how computational backends can be wrapped in clean, minimal web interfaces for usability and experimentation.

## Installation
1. Clone the repository
```
git clone https://github.com/girstmairflorian-rgb/Benchmark_Web_UI
cd Benchmark_Web_UI
```
2. Create a virtual environment (recommended)
```
python -m venv venv
source venv/bin/activate       # macOS / Linux
venv\Scripts\activate          # Windows
```
3. Install dependencies
```
pip install -r requirements.txt
```

Make sure the Benchmark Suite is accessible (installed or in PYTHONPATH).

4. Initialize the database (if empty)

The app will automatically create benchmark_results.db on first run.

If you want to reset the DB:
```
rm results.db
```
## Usage

Start the server:
```
flask run
```

Navigate to:
```
http://127.0.0.1:5000
```

You will see the benchmark configuration form.

## Screenshots

![alt text](https://github.com/girstmairflorian-rgb/Benchmark_Web_UI/blob/master/images/screenshot-app.png?raw=true)
![alt text](https://github.com/girstmairflorian-rgb/Benchmark_Web_UI/blob/master/images/screenshot-results.png?raw=true)
![alt text](https://github.com/girstmairflorian-rgb/Benchmark_Web_UI/blob/master/images/screenshot-history.png?raw=true)

## Database

All benchmark runs are stored in:
```
results.db
```

Table schema:
```
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    algorithm TEXT,
    method TEXT,
    upper_limit INTEGER,
    num_processes INTEGER,
    elapsed_time REAL,
    timestamp TEXT
);
```

## Project Structure
```
benchmark_web_ui/
│
├── app.py                   # Flask application
├── benchmarks/              # Backend Benchmark Suite (dependency)
├── database/
│   └── db.py                # Database helper functions
|   └── results.db           # SQLite file
├── templates/
│   ├── index.html           # Benchmark form
│   └── results.html         # Results page
├── requirements.txt
└── README.md
```

## Related Project

This web UI depends on:

### Compute-Intensive Benchmarking Suite

A pure-Python framework comparing multiprocessing strategies and compute algorithms.

https://github.com/girstmairflorian-rgb/Compute-intensive_Benchmarking_Suite_in_Python

## License

MIT