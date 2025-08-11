import random
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

class SensorDataSimulator:
    """
    Simulates sensor readings for flow rate, pressure, temperature, and status.
    Values generated within realistic bounds.
    """
    def __init__(self):
        self.flow_rate_range = (1000, 5000)        # example units: barrels/hour
        self.pressure_range = (50, 150)            # example units: psi
        self.temperature_range = (50, 120)         # example units: Fahrenheit
        self.status_choices = ["Normal", "Warning", "Critical"]

    def generate_reading(self) -> dict:
        return {
            "flow_rate": round(random.uniform(*self.flow_rate_range), 2),
            "pressure": round(random.uniform(*self.pressure_range), 2),
            "temperature": round(random.uniform(*self.temperature_range), 2),
            "status": random.choices(self.status_choices, weights=[0.8, 0.15, 0.05])[0],
        }

    def batch_generate(self, n: int) -> list[dict]:
        return [self.generate_reading() for _ in range(n)]

def load_external_dataset(path: str) -> pd.DataFrame:
    """
    Loads a CSV dataset given a file path.
    """
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return pd.DataFrame()  # empty DataFrame as fallback

def get_hardcoded_industry_trends():
    data = {
        "Year": [2015, 2016, 2017, 2018, 2019],
        "Crude Oil Production (MMT)": [30.5, 32.1, 31.8, 33.4, 34.0],
        "Natural Gas Production (BCM)": [40.2, 41.5, 43.0, 44.1, 45.0],
        # add more columns as needed
    }
    df = pd.DataFrame(data)
    return df

def get_sample_oil_production_statistics():
    """
    Returns a small hardcoded sample DataFrame resembling
    oil production statistics (year-wise).
    """
    data = {
        "Year": [2015, 2016, 2017, 2018, 2019, 2020],
        "Crude Oil Production (MMT)": [30.5, 32.1, 31.8, 33.4, 34.0, 32.5],
        "Natural Gas Production (BCM)": [40.2, 41.5, 43.0, 44.1, 45.0, 44.3],
        "Petroleum Products (MMT)": [25.4, 26.0, 27.3, 28.1, 29.0, 28.5],
    }
    df = pd.DataFrame(data)
    return df

def get_sample_state_wise_consumption():
    """
    Returns a small hardcoded sample DataFrame resembling
    state-wise consumption of oil products.
    """
    data = {
        "State": ["State A", "State B", "State C", "State D"],
        "Consumption (MMT)": [5.5, 3.2, 4.1, 2.8],
        "Production (MMT)": [2.5, 4.0, 3.5, 1.5],
    }
    df = pd.DataFrame(data)
    return df

def train_and_predict_production(df, years_to_predict=3):
    """
    Trains a linear regression model to predict Crude Oil Production based on Year.
    Returns predictions for the next 'years_to_predict' years.
    """
    # Prepare data
    X = df['Year'].values.reshape(-1, 1)  # feature
    y = df['Crude Oil Production (MMT)'].values  # target

    model = LinearRegression()
    model.fit(X, y)

    last_year = df['Year'].max()
    future_years = np.array([last_year + i for i in range(1, years_to_predict + 1)]).reshape(-1, 1)

    predictions = model.predict(future_years)
    prediction_df = pd.DataFrame({
        'Year': future_years.flatten(),
        'Predicted Crude Oil Production (MMT)': predictions.round(2)
    })

    return prediction_df