# Wine Quality Prediction on Heroku
By: Leticia Genao
Course: N.U. ANA680

# Heroku Deployment: Wine Quality Prediction
Detailed steps and descriptions of the Heroku deployment process for the Wine Quality Prediction model.

## Deployment Overview
This folder contains the application code and configuration needed to deploy the wine quality prediction model on Heroku.

## Contents
- `app.py`: The Flask application file.
- `requirements.txt`: A list of Python package dependencies.
- `Procfile`: A file that specifies the commands that are executed by the app on startup.
- `runtime.txt`: Specifies the Python version.

## Problem Statement
This project aims to predict the quality of wine based on its physicochemical properties using a Ridge regression model. The model provides insights into how different factors affect wine quality, serving as a useful tool for winemakers and connoisseurs alike.

## Dataset Description
The dataset used is the Wine Quality Dataset from the UCI Machine Learning Repository. It contains data for red and white variants of the Portuguese "Vinho Verde" wine.

- Data Source: Wine Quality Dataset
- Rows: Red Wine - 1,599; White Wine - 4,898
- Columns: 12 (including the target variable 'quality')

## Methodology
### Data Preprocessing
Data was normalized and split into training and testing sets with a ratio of 70:30.

### Model Building
A Ridge regression model was built using Python's Scikit-learn library, with hyperparameters optimized through grid search.

### Model Evaluation
The model's performance was evaluated using MSE (Mean Squared Error) and R2 score, emphasizing prediction accuracy and explaining variance respectively.

## Results
- Final Test MSE: 0.0182
- Final Test R2 Score: 0.205

## Discussion
The Ridge regression model demonstrates the complex nature of predicting wine quality based on physicochemical properties alone, highlighting the challenge of modeling sensory data. The selected hyperparameters aim to balance bias and variance.

## Conclusion
While the model provides a foundational approach to predicting wine quality, further refinement with additional data and potentially more complex algorithms like ensemble methods could enhance predictive performance.

## Deployment
The model is deployed on Heroku, making it accessible via a web interface for public interaction.

- Live Application: [Visit Heroku App](https://winequalityapp-d6fc38e6a369.herokuapp.com/)

## Reference
Cortez, Paulo, Cerdeira,A., Almeida,F., Matos,T., and Reis,J.. (2009). Wine Quality. UCI Machine Learning Repository. https://doi.org/10.24432/C56S3T.