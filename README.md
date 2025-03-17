# California Housing Price Predictor

A machine learning project to predict housing prices in California based on the California Housing dataset.

## Project Overview

This project was developed to analyze housing prices in California and build a model that can predict a house's price based on features like location, income level, and housing characteristics. I started with exploratory data analysis to understand the data, then built and compared several machine learning models before deploying the best one as an API.

## What's Inside

- **Data Analysis**: Thorough exploration of the California Housing dataset with visualizations
- **Model Training**: Multiple regression models with hyperparameter tuning
- **Model Deployment**: A simple Flask API to serve predictions

## Directory Structure

```
assessment/
├── data/                  # Dataset files and model results
├── models/                # Saved model and scaler
├── notebooks/             # Jupyter notebooks
│   └── EDA_and_Model_training.ipynb
├── api/                   # Flask API for serving predictions
└── README.md              # You are here!
```

## Getting Started

### Prerequisites

You'll need:
- Python 3.7+
- Basic packages: pandas, numpy, matplotlib, scikit-learn, xgboost, flask
- Jupyter Notebook (for the analysis notebook)

I recommend using a virtual environment:

```bash
# Create a virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (macOS/Linux)
source venv/bin/activate
```

### Running the Notebook

The notebook contains all the EDA, model training, and evaluation steps:

1. Start Jupyter:
   ```bash
   jupyter notebook
   ```

2. Open `notebooks/EDA_and_Model_training.ipynb`

3. Run the cells to see the analysis and train models

### Using the API

After you've trained the models (or if you're using the pre-trained models), you can run the API:

1. Go to the API directory:
   ```bash
   cd api
   ```

2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the API:
   ```bash
   python app.py
   ```

4. Send requests to `http://localhost:5000/predict` with feature data

## The Data

I used the California Housing dataset, which contains information about housing blocks in California from the 1990 census. Each record represents a block group and includes:

- Median income
- House age
- Number of rooms/bedrooms
- Population
- Occupancy
- Location (latitude/longitude)
- Housing prices (the target value)

## Model Performance

After trying several models, XGBoost with tuned hyperparameters performed the best:

- **RMSE**: 0.4549
- **R²**: 0.8421 (the model explains ~84% of price variance)

The visualizations in the notebook show that the model captures the overall distribution of housing prices quite well, although as with any model, there are some outliers it struggles with.

## Challenges & Lessons

Some interesting challenges I faced:
- The geographic component of housing prices required creative feature engineering
- Finding the right balance between model complexity and overfitting took some experimentation
- Scaling the numerical features properly was important for algorithm performance