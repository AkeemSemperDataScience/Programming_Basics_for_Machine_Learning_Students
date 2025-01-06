
import pandas as pd
import SAMP_SOL_Lab_1


columns = ["Question", "Test_Num", "Input", "Expected_Output", "Function_Call"]
df_tests = pd.DataFrame(columns=columns)

q1_corr_1 = SAMP_SOL_Lab_1.lab1Question1(1)
q1_corr_2 = SAMP_SOL_Lab_1.lab1Question1(128)
q1_corr_3 = SAMP_SOL_Lab_1.lab1Question1(0)

q2_corr_1 = SAMP_SOL_Lab_1.lab1Question2("John")
q2_corr_2 = SAMP_SOL_Lab_1.lab1Question2("Janet")
q2_corr_3 = SAMP_SOL_Lab_1.lab1Question2("Laquisha")

q3_corr_1 = SAMP_SOL_Lab_1.lab1Question3("Hello", 0)
q3_corr_2 = SAMP_SOL_Lab_1.lab1Question3("Yesterday", 3)
q3_corr_3 = SAMP_SOL_Lab_1.lab1Question3("Tomorrow", 148)

q4_corr_1 = SAMP_SOL_Lab_1.lab1Question4("lab1_test_file.txt")

q5_corr_1 = SAMP_SOL_Lab_1.lab1Question5([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q5_corr_2 = SAMP_SOL_Lab_1.lab1Question5([1, 2, 3, 3, 3, 4, 5, 1, 2, 7, 7, 7, 7, 7, 7, 7, 456, 456])
q5_corr_3 = SAMP_SOL_Lab_1.lab1Question5([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

q6_corr_1 = SAMP_SOL_Lab_1.lab1Question6(4, 3, 2, 1)
q6_corr_2 = SAMP_SOL_Lab_1.lab1Question6(0, 0, 0, 0)
q6_corr_3 = SAMP_SOL_Lab_1.lab1Question6(1, 1, 1, 1)

df_tests = df_tests.append({"Question": 1, "Test_Num": 1, "Input": 1, "Expected_Output": q1_corr_1, "Function_Call": "lab1Question1(1)"}, ignore_index=True)
df_tests = df_tests.append({"Question": 1, "Test_Num": 2, "Input": 128, "Expected_Output": q1_corr_2, "Function_Call": "lab1Question1(128)"}, ignore_index=True)
df_tests = df_tests.append({"Question": 1, "Test_Num": 3, "Input": 0, "Expected_Output": q1_corr_3, "Function_Call": "lab1Question1(0)"}, ignore_index=True)
df_tests = df_tests.append({"Question": 2, "Test_Num": 1, "Input": "John", "Expected_Output": q2_corr_1, "Function_Call": "lab1Question2('John')"}, ignore_index=True)
df_tests = df_tests.append({"Question": 2, "Test_Num": 2, "Input": "Janet", "Expected_Output": q2_corr_2, "Function_Call": "lab1Question2('Janet')"}, ignore_index=True)
df_tests = df_tests.append({"Question": 2, "Test_Num": 3, "Input": "Laquisha", "Expected_Output": q2_corr_3, "Function_Call": "lab1Question2('Laquisha')"}, ignore_index=True)
df_tests = df_tests.append({"Question": 3, "Test_Num": 1, "Input": ("Hello", 0), "Expected_Output": q3_corr_1, "Function_Call": "lab1Question3('Hello', 0)"}, ignore_index=True)
df_tests = df_tests.append({"Question": 3, "Test_Num": 2, "Input": ("Yesterday", 3), "Expected_Output": q3_corr_2, "Function_Call": "lab1Question3('Yesterday', 3)"}, ignore_index=True)
df_tests = df_tests.append({"Question": 3, "Test_Num": 3, "Input": ("Tomorrow", 148), "Expected_Output": q3_corr_3, "Function_Call": "lab1Question3('Tomorrow', 148)"}, ignore_index=True)
df_tests = df_tests.append({"Question": 4, "Test_Num": 1, "Input": "lab1_test_file.txt", "Expected_Output": q4_corr_1, "Function_Call": "lab1Question4('lab1_test_file.txt')"}, ignore_index=True)
df_tests = df_tests.append({"Question": 5, "Test_Num": 1, "Input": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Expected_Output": q5_corr_1, "Function_Call": "lab1Question5([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)"}, ignore_index=True)
df_tests = df_tests.append({"Question": 5, "Test_Num": 2, "Input": [1, 2, 3, 3, 3, 4, 5, 1, 2, 7, 7, 7, 7, 7, 7, 7, 456, 456], "Expected_Output": q5_corr_2, "Function_Call": "lab1Question5([1, 2, 3, 3, 3, 4, 5, 1, 2, 7, 7, 7, 7, 7, 7, 7, 456, 456)"}, ignore_index=True)
df_tests = df_tests.append({"Question": 5, "Test_Num": 3, "Input": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Expected_Output": q5_corr_3, "Function_Call": "lab1Question5([1, 2, 3, 4, 5, 6, 7, 8, 9, 10)"}, ignore_index=True)
df_tests = df_tests.append({"Question": 6, "Test_Num": 1, "Input": (4, 3, 2, 1), "Expected_Output": q6_corr_1, "Function_Call": "lab1Question6(4, 3, 2, 1)"}, ignore_index=True)
df_tests = df_tests.append({"Question": 6, "Test_Num": 2, "Input": (0, 0, 0, 0), "Expected_Output": q6_corr_2, "Function_Call": "lab1Question6(0, 0, 0, 0)"}, ignore_index=True)
df_tests = df_tests.append({"Question": 6, "Test_Num": 3, "Input": (1, 1, 1, 1), "Expected_Output": q6_corr_3, "Function_Call": "lab1Question6(1, 1, 1, 1)"}, ignore_index=True)

df_tests.to_csv("SAMP_SOL_responses.csv", index=False) # Save the test results to a CSV file