# System Health Checker


## Description
    A Python script that monitors the basic health of a computer system by checking CPU, Disk, Memory, and GPU usage.

## Requirements
    - Python 3.x
    - psutil library
    - nvidia-ml-py library (for NVIDIA GPU monitoring)

## Features
    - Checks the CPU usage, Disk usage, Memory usage and GPU usage.
    - Determines the system health status based on whether any monitored resource reaches 99% or higher.
    - Generates a text report after execution.
    - GPU monitoring currently supports NVIDIA GPUs only.

## Project Structure

    system-health-checker/
    │
    ├── system-health-checker.py
    ├── .gitignore
    ├── system_health_report.txt
    └── README.md

## How to Run
    1. Open a terminal in the project directory.
    2. Install the required dependencies.
        pip install psutil nvidia-ml-py
    3. Run the Python script:
        python system-health-checker.py

## Sample Input
    N/A

## Sample Output
    Report Generated: 11/03/2026 10:03 AM 

    System Health Status

    Disk Usage: 33.2%
    CPU Usage: 40.12%
    Memory Usage: 78.12%
    GPU Usage: 23.65%

    System is Healthy, all resources does not exceed 99% threshold

## System Health Classification

    Threshold Count              Status
            0                   Healthy
            1                   Warning
            2                   Severe
        3 or more               Critical

## Future Improvements
    - Support GPU monitoring for other brands.
    - Display individual GPU utilization instead of calculating the average.
    - Identify which resources triggered a warning or critical status.

## Author
    Nik Cortez