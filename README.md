# Python Log Analyzer & Report Generator

A Python-based automation tool that analyzes application log files and generates a summary report automatically.

This project was developed as part of the Python Developer Internship at SWYNEX Technologies.

## Project Objective

Checking application logs manually can take time, especially when a log file contains many entries.

This tool automates the process by reading a log file, identifying different log levels, detecting errors, and generating a report.

## Features

- Accepts a log file path from the user
- Reads application log files automatically
- Detects INFO, WARNING, ERROR, and CRITICAL entries
- Counts each log level
- Detects invalid log lines
- Calculates error rate
- Determines the overall application status
- Extracts ERROR and CRITICAL messages
- Generates a text report automatically
- Handles missing or unreadable log files

## Project Structure

Python-Log-Analyzer/
│
├── main.py
├── log_analyzer.py
├── report_generator.py
├── sample.log
├── .gitignore
└── README.md

## How the Automation Works

The automation follows these steps:

1. The user provides the path of a log file.
2. main.py starts the analysis process.
3. log_analyzer.py reads the log file and identifies log levels.
4. The tool counts INFO, WARNING, ERROR, and CRITICAL entries.
5. ERROR and CRITICAL messages are extracted separately.
6. Invalid log lines are detected.
7. The error rate and overall status are calculated.
8. report_generator.py creates a report.txt file containing the analysis results.

## How to Run

Make sure Python is installed on your system.

Open the project folder in a terminal and run:

python main.py

Enter the log file path when prompted:

sample.log

The generated report will be saved as:

report.txt

## Example

For the included sample.log, the analyzer produces results such as:

Total Log Lines    : 15
Valid Log Entries  : 15
Invalid Log Lines  : 0

Log Level Summary:
INFO              : 9
WARNING           : 2
ERROR             : 3
CRITICAL          : 1

Error Rate        : 26.67%
Overall Status    : CRITICAL

## Technologies Used

- Python
- Regular Expressions
- File Handling
- Exception Handling
- Text Report Generation

## Real-World Use

This type of automation can help software development and IT teams quickly review application or server logs and identify errors or critical issues without checking every log entry manually.