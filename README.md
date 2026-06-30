# Elisa Forecast Tracker

![Elisa Price vs Intrinsic Value](output/tracker_chart.png?raw=true)

## Background
This is a follow-up to an equity research report I wrote for my Financial 
Statement Analysis course at Aalto University. The report initiated coverage 
of Elisa Corporation (ELISA.HE) with a BUY rating and a 12-month price target 
of €51, based on an Abnormal Earnings valuation model.

After submitting the report, I was curious whether the analysis was directionally 
accurate, so I built this tracker to monitor it over time.

## What it tracks
- Elisa's closing price vs the original intrinsic value estimate (€51.05)
- The implied upside/downside gap over time

## How it works
A Python script pulls Elisa's latest closing price from LSEG Workspace via the 
`lseg-data` library, calculates the gap vs the original estimate, and logs the 
result to a local SQLite database. The script is run manually each week.

## Setup
- Python 3.11, conda environment
- LSEG Workspace must be running for authentication
- Install dependencies: `pip install lseg-data pandas`

## Usage
```bash
cd src
python elisa_tracker.py
```

## Original report
The equity report and financial model that this tracker is based on are available
in a separate repository: [https://github.com/Jiaweisun274/elisa-equity-research]