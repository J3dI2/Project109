import plotly.figure_factory as ff
import pandas as pd
import csv
import statistics

df = pd.read_csv("StudentsPerformance.csv")
fig = ff.create_distplot(df[["math score"].tolist()], ["math_score"], show_hist=False)
fig.show()

mean = sum("math_score") / len("math_score")
std_deviation = statistics.stdev("math_score")
median = statistics.median("math_score")
mode = statistics.mode("math_score")

fig = ff.create_distplot(["math_score"], ["Result"], show_hist=False)
fig.show()

std_deviation = statistics.stdev("math_score")

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

list_of_data_within_1_std_deviation = [result for result in "math_score" if "Result" > first_std_deviation_start and "Result" < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in "math_score" if "Result" > second_std_deviation_start and "Result" < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in "math_score" if "Result" > third_std_deviation_start and "Result" < third_std_deviation_end]


print("{}% of data lies within 1 standard deiavtion".format(len(list_of_data_within_1_std_deviation)*100/len("math_score")))
print("{}% of data lies within 2 standard deiavtion".format(len(list_of_data_within_2_std_deviation)*100/len("math_score")))
print("{}% of data lies within 3 standard deiavtion".format(len(list_of_data_within_3_std_deviation)*100/len("math_score")))

