# BAN6420-FINAL-PROJECT
SURVEY TOOL FOR INCOME SPENDING ANALYSIS

Final Project – BAN6420 | Nexford University Developed by: Kendra Onah

## Project Overview
This project delivers a full-stack data collection and analysis tool built with Flask, MongoDB, and Python/R, designed to support a healthcare product launch by analyzing participant income and spending behavior. The tool collects demographic and financial data via a web interface, stores it in MongoDB, processes it into CSV format, and visualizes key insights in a Jupyter notebook. Charts are exported for use in client presentations.
## Objectives
Build a responsive Flask web application for survey data collection

Store structured user data in MongoDB

Process and export data using a custom Python class

Analyze income and spending patterns in Jupyter

Generate visualizations for PowerPoint-ready charts

Deploy the application on AWS for real-world accessibility

## Technologies Used
Layer	Tools & Libraries
Frontend	HTML (via Flask templates)
Backend	Flask, Python
Database	MongoDB (local or Atlas)
Data Processing	Pandas, Python class (User)
Visualization	Matplotlib, Bokeh
Notebook	Jupyter
Deployment	AWS Elastic Beanstalk or EC2
CI/Runtime Tools	Gunicorn, python-dotenv

 ## Features
✅ Web form with checkboxes and textboxes for expense categories

✅ MongoDB integration for persistent storage

✅ Python class to process and export data to CSV

✅ Jupyter notebook for analysis and chart generation

✅ AWS deployment instructions and configuration

✅ Charts saved as PNG for client presentations

## Quickstart (Local Setup)
1. Clone the repository
bash
git clone https://github.com/digitalcurrencymom/BAN6420-MODULE-6-ASSIGNMENT.git
cd BAN6420-MODULE-6-ASSIGNMENT
2. Create and activate a virtual environment
powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
3. Start MongoDB (local or Atlas)
Set your MongoDB URI:

powershell
$env:MONGO_URI='mongodb://localhost:27017/'
4. Run the Flask app
powershell
python app.py
Visit http://localhost:5000 to submit survey responses.

 ## Data Export to CSV
After collecting responses, export data from MongoDB:

python
from pymongo import MongoClient
import pandas as pd

client = MongoClient('mongodb://localhost:27017/')
db = client['survey_db']
rows = list(db.users.find({}, {'_id': 0}))
df = pd.DataFrame(rows)
df.to_csv('survey_users.csv', index=False)


## Data Analysis in Jupyter
Open notebook.json in Jupyter (rename to .ipynb if needed). Run the notebook to:

Analyze average income by age

Visualize gender-based spending across categories

Save charts as PNG for PowerPoint

Charts generated:

ages_highest_income.png

gender_utilities.png

gender_entertainment.png

gender_school_fees.png

gender_shopping.png

gender_healthcare.png

## AWS Deployment Options
Option A: Elastic Beanstalk (Recommended)
Includes Procfile and EB config for easy deployment.

bash
eb init -p python-3.10 survey-final-app --region us-east-1
eb create survey-final-env
eb setenv MONGO_URI='your_mongo_uri_here'
eb deploy
Option B: EC2 Manual Setup
Launch EC2 instance

Install Python and dependencies

Configure Flask as a systemd service

Use nginx as reverse proxy

Secure with HTTPS (e.g., Certbot)

## Project Structure
Code
BAN6420-MODULE-6-ASSIGNMENT/

 app.py                  # Flask application
 user.py                 # Data processing class
 templates/              # HTML form
requirements.txt        # Python dependencies
notebook.json           # Jupyter notebook (rename to .ipynb)
survey_users.csv        # Exported data (generated)
charts/                 # PNG charts for presentation
Procfile                # AWS EB config
README.md               # Project documentation
run_notes.txt           # Notes on runtime environment

##  Educational Value
This project demonstrates:

Full-stack development with Flask and MongoDB

Real-world data collection and analysis

Deployment and environment configuration

Visualization and reporting for business decision-making

 ## Author
Kendra Onyinye Onah 
R & Python Developer 
Nexford University Location: Washington, DC 
GitHub: digitalcurrencymom
