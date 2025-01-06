
import pandas
import SAMP_SOL_Lab_2


columns = ["Question", "Test_Num", "Input", "Expected_Output"]
df_tests = pandas.DataFrame(columns=columns)

q1_corr_1 = SAMP_SOL_Lab_2.lab2Question1("purple")
q1_corr_2 = SAMP_SOL_Lab_2.lab2Question1("ada")
q1_corr_3 = SAMP_SOL_Lab_2.lab2Question1("hello")

q2_corr_1 = SAMP_SOL_Lab_2.lab2Question2(7)
q2_corr_2 = SAMP_SOL_Lab_2.lab2Question2(12)
q2_corr_3 = SAMP_SOL_Lab_2.lab2Question2(-5)

q3_corr_1 = SAMP_SOL_Lab_2.lab2Question3("Coding is cool", "co")
q3_corr_2 = SAMP_SOL_Lab_2.lab2Question3("Attitude is everything", "tt")
q3_corr_3 = SAMP_SOL_Lab_2.lab2Question3("Superstitious and superfluous", "super")

q4_corr_1 = SAMP_SOL_Lab_2.lab2Question4([1, 2, 3, 4], [5, 6, 7, 8])
q4_corr_2 = SAMP_SOL_Lab_2.lab2Question4([0, 0, 0, 0], [0, 0, 0])
q4_corr_3 = SAMP_SOL_Lab_2.lab2Question4([1, 2, 8, 3], [4, 5, 6, 7])

q5_corr_1 = SAMP_SOL_Lab_2.isValidPassword("password")
q5_corr_2 = SAMP_SOL_Lab_2.isValidPassword("Password1")
q5_corr_3 = SAMP_SOL_Lab_2.isValidPassword("12345678")

df_tests = df_tests.append({"Question": 1, "Test_Num": 1, "Input": "purple", "Expected_Output": q1_corr_1}, ignore_index=True)
df_tests = df_tests.append({"Question": 1, "Test_Num": 2, "Input": "ada", "Expected_Output": q1_corr_2}, ignore_index=True)
df_tests = df_tests.append({"Question": 1, "Test_Num": 3, "Input": "hello", "Expected_Output": q1_corr_3}, ignore_index=True)
df_tests = df_tests.append({"Question": 2, "Test_Num": 1, "Input": 7, "Expected_Output": q2_corr_1}, ignore_index=True)
df_tests = df_tests.append({"Question": 2, "Test_Num": 2, "Input": 12, "Expected_Output": q2_corr_2}, ignore_index=True)
df_tests = df_tests.append({"Question": 2, "Test_Num": 3, "Input": -5, "Expected_Output": q2_corr_3}, ignore_index=True)
df_tests = df_tests.append({"Question": 3, "Test_Num": 1, "Input": ("Coding is cool", "co"), "Expected_Output": q3_corr_1}, ignore_index=True)
df_tests = df_tests.append({"Question": 3, "Test_Num": 2, "Input": ("Attitude is everything", "tt"), "Expected_Output": q3_corr_2}, ignore_index=True)
df_tests = df_tests.append({"Question": 3, "Test_Num": 3, "Input": ("Superstitious and superfluous", "super"), "Expected_Output": q3_corr_3}, ignore_index=True)
df_tests = df_tests.append({"Question": 4, "Test_Num": 1, "Input": ([1, 2, 3, 4], [5, 6, 7, 8]), "Expected_Output": q4_corr_1}, ignore_index=True)
df_tests = df_tests.append({"Question": 4, "Test_Num": 2, "Input": ([0, 0, 0, 0], [0, 0, 0]), "Expected_Output": q4_corr_2}, ignore_index=True)
df_tests = df_tests.append({"Question": 4, "Test_Num": 3, "Input": ([1, 2, 8, 3], [4, 5, 6, 7]), "Expected_Output": q4_corr_3}, ignore_index=True)
df_tests = df_tests.append({"Question": 5, "Test_Num": 1, "Input": "password", "Expected_Output": q5_corr_1}, ignore_index=True)
df_tests = df_tests.append({"Question": 5, "Test_Num": 2, "Input": "Password1", "Expected_Output": q5_corr_2}, ignore_index=True)
df_tests = df_tests.append({"Question": 5, "Test_Num": 3, "Input": "12345678", "Expected_Output": q5_corr_3}, ignore_index=True)

df_tests.to_csv("course_material/labs/lab2/SAMP_SOL_responses.csv", index=False) # Save the test results to a CSV file