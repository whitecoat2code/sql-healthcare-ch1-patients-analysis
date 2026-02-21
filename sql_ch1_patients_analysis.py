# SQL Chapter 1: Healthcare Patient Analysis
# Dr Aadil Khan (MBBS) - HealthTech Learning Project
# GitHub: whitecoat2code | Date: Feb 21, 2026

import sqlite3
import pandas as pd

# Step 1: Create in-memory DB + Patient data (realistic hospital)
conn = sqlite3.connect(':memory:')
data = {
    'patient_id': [1,2,3,4,5,6],
    'age': [45,67,34,52,29,78],
    'diagnosis': ['Hypertension','Diabetes','Flu','Hypertension','Diabetes','Heart Disease'],
    'bill': [5000,8000,2000,6000,7000,12000]
}
df = pd.DataFrame(data)
df.to_sql('patients', conn, index=False)

# Chapter 1 Queries (Test Passed 100%)
print("1. All Patients:\n", pd.read_sql_query("SELECT * FROM patients;", conn))

print("2. High Bill Patients (age DESC):\n", 
      pd.read_sql_query("SELECT patient_id, age, diagnosis, bill FROM patients WHERE bill > 5000 ORDER BY age DESC;", conn))

print("3. Flu Count:\n", pd.read_sql_query("SELECT COUNT(*) as flu_count FROM patients WHERE diagnosis = 'Flu';", conn))

print("4. Avg Age:\n", pd.read_sql_query("SELECT AVG(age) as avg_age FROM patients;", conn))

print("5. Disease Summary:\n", 
      pd.read_sql_query("SELECT diagnosis, COUNT(*) as count, SUM(bill) as total_bill FROM patients GROUP BY diagnosis;", conn))

print("SQL Ch1 Complete! Ready for JOINs & Projects.")
