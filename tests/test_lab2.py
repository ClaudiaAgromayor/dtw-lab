from src.dtw_lab.lab2 import get_statistic
import pandas as pd
import pytest
from dtw_lab.lab1 import calculate_statistic
from dtw_lab.lab1 import encode_categorical_vars
from dtw_lab.lab2 import get_statistic

def test_calculate_statistic():
    df = pd.DataFrame({"Charge_Left_Percentage": [39, 60, 30, 30, 41]})
    assert calculate_statistic("mean", df["Charge_Left_Percentage"]) == 40
    assert calculate_statistic("median", df["Charge_Left_Percentage"]) == 39
    assert calculate_statistic("mode", df["Charge_Left_Percentage"]) == 30

def test_encode_categorical_vars():
    df = pd.DataFrame({
        "Battery_Size": ["AAA", "AA", "C", "D"],
        "Discharge_Speed": ["Slow", "Medium", "Fast", "Slow"],
        "Manufacturer": ["A", "B", "A", "C"]
    })
    encoded_df = encode_categorical_vars(df)
    assert encoded_df["Battery_Size"].tolist() == [1, 2, 3, 4]
    assert encoded_df["Discharge_Speed"].tolist() == [1, 2, 3, 1]
    assert encoded_df["Manufacturer_A"].tolist() == [1, 0, 1, 0]
    assert encoded_df["Manufacturer_B"].tolist() == [0, 1, 0, 0]
    assert encoded_df["Manufacturer_C"].tolist() == [0, 0, 0, 1]

def test_api_call(mocker):
    # Setup the mock for read_csv_from_google_drive
    fake_df = pd.DataFrame({
        "Charge_Left_Percentage": [10, 20, 30, 10],
        "Serial_Number": [1, 2, 3, 4],
        "Voltage_Cutoff": [0.9, 0.8, 0.7, 0.6],
        "Nominal_Voltage": [1.5, 1.5, 1.5, 1.5],
        "Avg_Operating_Temperature": [90, 95, 85, 80],
        "Days_Since_Production": [10000, 15000, 12000, 8000],
        "Current_Voltage": [1.49, 3, 5, 6],
        "Serial_Number": ["E", "F", "T", "V"],
        "Battery_Size": ["C", "A", "D", "C"]
    })
    mock_read_csv = mocker.patch('dtw_lab.lab2.read_csv_from_google_drive', return_value=fake_df)

    # Run the function with required arguments
    result = get_statistic("mean", "Charge_Left_Percentage")

    # Assertions
    assert result is not None  # Adjust as needed for your function's expected output
    assert mock_read_csv.called
    mock_read_csv.assert_called_once()