# AIML-W1 – Employee Attrition Risk Analysis using Machine Learning

## About the Project

This project was developed as part of my AIML internship. The main purpose of this project is to analyze employee attrition data and understand the factors that may be related to employees leaving an organization.

I used Python and different data analysis and machine learning libraries to clean the dataset, perform Exploratory Data Analysis (EDA), create visualizations, train a machine learning model, and build a simple prediction system.

## Objective

The main objectives of this project are:

- To understand employee attrition using the given dataset.
- To clean and preprocess the employee data.
- To perform Exploratory Data Analysis (EDA).
- To identify important patterns related to employee attrition.
- To create meaningful visualizations.
- To train a machine learning model for attrition prediction.
- To evaluate the performance of the model.
- To create a simple prediction system for new employee information.

## Tools and Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## Dataset

The dataset contains information about employees and includes different attributes such as:

- Employee ID
- Age
- Department
- Job Role
- Monthly Income
- Years at Company
- Job Satisfaction
- Work Hours
- Overtime
- Distance From Home
- Training Hours
- Performance Rating
- Previous Companies
- Attrition

The target variable used for prediction is **Attrition**, which indicates whether an employee has left the organization (`Yes`) or stayed (`No`).

## Work Done in the Project

The project was completed in the following steps:

### 1. Data Collection

An employee attrition dataset was used for the analysis.

### 2. Data Cleaning

The dataset was checked for:

- Missing values
- Duplicate records
- Incorrect data types
- Inconsistent values
- Unwanted data

### 3. Data Preprocessing

The data was prepared for machine learning by converting categorical values into numerical form and preparing the required features.

### 4. Exploratory Data Analysis

EDA was performed to understand the relationship between employee attributes and attrition.

Some of the questions analyzed were:

- Which department has higher attrition?
- Does overtime have a relationship with attrition?
- Does salary differ between employees who stayed and left?
- Does experience affect attrition?
- Does distance from home have a relationship with attrition?
- Which job roles have higher attrition?

### 5. Data Visualization

Different graphs were created to understand the data more easily.

The visualizations include:

- Attrition Distribution
- Department-wise Attrition
- Job Satisfaction vs Attrition
- Salary vs Attrition
- Overtime vs Attrition

## Machine Learning Model

For the prediction part of the project, **Logistic Regression** was used.

The dataset was divided into:

- 80% Training Data
- 20% Testing Data

The model was trained using the training data and then tested using the testing data.

## Model Performance

The Logistic Regression model achieved the following results:

| Metric | Score |
|---|---:|
| Accuracy | 91.60% |
| Precision | 90.35% |
| Recall | 93.07% |
| F1-score | 91.69% |

The confusion matrix was also used to understand the correct and incorrect predictions made by the model.

## Key Findings

Based on the analysis performed on the dataset, the following findings were observed:

1. Employees working overtime showed a higher attrition tendency than employees who did not work overtime.

2. The Sales department recorded the highest attrition rate at 58.23%.

3. Sales Representatives had the highest attrition rate among the analyzed job roles at 79.62%.

4. Recruiters also showed a comparatively high attrition rate of 73.89%.

5. Employees who stayed in the organization had a higher average monthly income than employees who left.

6. Employees who left had a lower average number of years at the company compared with employees who stayed.

7. Employees who left had a higher average distance from home compared with employees who stayed.

## Prediction System

A simple prediction system was developed as part of the project.

The user can enter employee details such as:

- Age
- Monthly Income
- Years at Company
- Job Satisfaction
- Overtime
- Distance From Home

The system predicts the employee's attrition risk and displays:

```text
Prediction: High Attrition Risk