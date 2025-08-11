# controller.py
import streamlit as st
from model import train_and_predict_production
from model import SensorDataSimulator, get_sample_oil_production_statistics, get_sample_state_wise_consumption
import view

ACCESS_KEY = "opensesame"  # simple hardcoded key for demo

def main():
    view.render_header()
    key = view.render_auth_input()
    has_access = key == ACCESS_KEY

    simulator = SensorDataSimulator()
    sensor_data = simulator.batch_generate(10)
    view.render_sensor_data_table(sensor_data)

    if has_access:
        df_trends = get_sample_oil_production_statistics()
        df_state = get_sample_state_wise_consumption()

        # Train model & get predictions
        df_predictions = train_and_predict_production(df_trends)

        view.render_industry_trends(df_trends)
        view.render_state_wise_consumption(df_state)
        view.render_ml_predictions(df_predictions)
    else:
        view.render_auth_message(False)

if __name__ == "__main__":
    main()
    