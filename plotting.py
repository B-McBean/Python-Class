# Crash Course in Python
# Author: Breanna McBean
# How to create plots using Python
# May 28, 2019

##############################################
# Plotting in Python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# The package matplotlib allows you to create plots similar to the way you would in MATLAB

# Create a simple plot
# plt.plot([1,2,3,4])
# Giving "plot(x)" only one input causes is to plot (1,1), (2,2), (3,3), (4,4)
# plt.ylabel('some numbers')
# Similar commands can be used to add the x axis label and a title
# plt.show()
# Use the "show()" function to create the plot
# Note: I will comment out all of the "show()" functions because it is easiest to have only one
# run at a time

# You can change the style of the plots
# plt.figure()
# Using the "figure()" function is like the one in MATLAB. It allows you to generate more than one figure
# at a time and allows for different settings on each one
# plt.plot([1,2,3,4], [1,4,9,16], 'ro')
# Here, we will plot (1,1), (2,4), (3,9), (4,16) using red dots
# plt.axis([0, 6, 0, 20])
# This creates axis ranges (x will be 0 to 6, y will be 0 to 20)
# plt.show()

# You can also plot multiple elements on the same plot
# plt.figure()
# t = np.arange(0., 5., 0.2)
# evenly sampled time at 200ms intervals
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# red dashes, blue squares and green triangles
# plt.show()

# You can also plot functions and use subplots
# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)
#
# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)
#
# plt.figure()
# plt.subplot(211)
# # (Number of rows, number of columns, subplot number)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
# plt.subplot(212)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.show()

# Check out https://matplotlib.org/users/pyplot_tutorial.html for more info on ways you can modify graphs and for
# things like using nonlinear axes and other types of plots.

##############################################
# Using Pandas data frames to create plots

# # Histograms
# # Let's look at the ages of people aboard the Titanic
# survival_data = pd.read_csv("TitanicSurvival.csv")
# print(survival_data.loc[0])
#
# age_data = survival_data["age"].dropna()
# # Age has NaN values for where age was not recorded. This "dropna" removes all of those entries
# plt.figure(1)
# plt.hist(age_data)
# plt.xlabel("Age")
# plt.ylabel("Count")
# plt.text(0, 100, r"$\mu$=" + str(round(age_data.mean(), 2)) + "\n" + r"$\sigma$=" + str(round(age_data.std(), 2)))
# # The "text(x,y,text)" command allows us to add "text" starting at the (x,y) coordinate of the plot.
# # Here, we added mean and standard deviation.
# # The 'r' tells it to interpret it using TeX.
# # The "round(num,dec)" command allows us to round to "dec" decimal places
# plt.show()

# Let's look at the difference in survival rate by class
survival_data = pd.read_csv("TitanicSurvival.csv")
# Get x axis labels
group_names = survival_data["passengerClass"].unique()
print(group_names)

# Use the function we previously created to turn a string into a 0 or 1
def StringtoBoolean(status):
    if status == "no":
        return 0
    elif status == "yes":
        return 1


survival_data["bool_survived"] = survival_data["survived"].apply(StringtoBoolean)
classes = survival_data.groupby("passengerClass")
print(classes.first())
# Find averages for y axis
x = classes["bool_survived"].mean()
averages = [x[0], x[1], x[2]]
y_pos = np.arange(len(averages))
# Create the plot
plt.bar(y_pos, averages, align='center', alpha=0.5)
plt.xticks(y_pos, group_names)
plt.ylabel('Survival Rate')
plt.show()
