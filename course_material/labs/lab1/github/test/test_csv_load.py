import pandas as pd
import START_Lab_1
import pytest 

tests = pd.read_csv("SAMP_SOL_responses.csv")

# Generate pytest tests
for index, row in tests.iterrows():
    test_name = f"test_case_{index}"
    input_data = row["input_data"]
    expected_output = row["expected_output"]

    @pytest.mark.parametrize("input_data, expected_output", [(input_data, expected_output)])
    def test_case(input_data, expected_output):
        # Call the function or code you want to test with the input_data
        result = START_Lab_1.your_function(input_data)

        # Assert the result matches the expected_output
        assert result == expected_output

    # Register the test function with the generated test name
    globals()[test_name] = test_case
