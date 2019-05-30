# Crash Course in Python
# Author: Breanna McBean
# Key functions in the Pandas package using TitanicSurvival.csv from R.
# May 29, 2019

##############################################
# Using the Pandas Package
import pandas as pd

# Using "pd" instead of pandas saves us some letters when we have to type it in the future

# Pandas can be used to create a data frame
data = {"Country": ["Belgium", "India", "Brazil"],
        "Capital": ["Brussels", "New Delhi", "Brasilia"],
        "Population": [11190846, 1303171035, 207847528]}
# Here, we have a dictionary we can turn into a pandas data frame by making the values associated
# with the keys the columns of the data frame. You can also turn lists and numpy arrays into pandas
# data frames.

df = pd.DataFrame(data, columns=["Country", "Capital", "Population"])
print("dictionary data frame:")
print(df)

# We can also use the "read_csv(x)" function to read in a csv file as a data frame.
# Similarly, there is a "to_csv(x)" function to write data frames to csv files.
survival_data = pd.read_csv("TitanicSurvival.csv")

# Note: If the file you are trying to read is not in the same folder as the Python file you are
# trying to read it from, you must provide the path through your file system.

# The "head(n)" function will show the first n rows of the data frame (default value is 5)
print("survival_data head:")
print(survival_data.head())

# The "info()" function tells you a bit about the data frame (name of columns, entries, size of data frame, etc.).
print("survival_data info:")
survival_data.info()

# The "shape" function gives you a tuple with the size of the data frame. This may be useful for loops.
print("survival_data size:")
print(survival_data.shape)

# The "describe" function gives the number of non-null data points, mean, standard deviation, and a five-number
# summary of numerical values in the data frame.
print("survival_data.describe():")
print(survival_data.describe())

# There are also individual functions that can provide you with specific information about the numerical columns
# of a data frame that can be saved to variables. For example, "data.mean()", "data.min()", "data.max()",
# "data.median()", and "data.std()" are all fairly self-explanatory. "data.corr()" returns a pandas data frame of
# correlation values for the numerical columns. "data.count()" returns the number of non-null entries.

# You can find these values for each column of numerical data.
print("survival_data mean")
print(survival_data.mean())
# The type returned here is a "series", which is a one-dimensional labeled array.

# You can also find these values for a specific column of numerical data.
print("Min age:", survival_data["age"].min())

# You can look up specific observations.
print("first entry of survival_data:")
print(survival_data.loc[0])
# There are two functions you can use, "loc" and "iloc". You can use "loc" with any type of label to access the
# element, but "iloc" works only for indices, so it accepts only integers.
# Here is a Stack Overflow thread that explains the differences in more detail if you're interested:
# https://stackoverflow.com/questions/31593201/how-are-iloc-ix-and-loc-different

# You can look up specific values by index.
print("first attribute of the first entry of survival_data:")
print(survival_data.loc[0][0])

# You can look up specific values by attribute names, as well.
print("age associated with the first entry of survival_data:")
print(survival_data.loc[0, "age"])

# You can examine specific attributes for each observation.
print("ages recorded in survival_data:")
ages = survival_data.loc[:, "age"]
print(ages.head())

# You can filter your data based on a certain attribute.
# This is like the "filter" function in R.
print("filer survival_data for passengers younger than 18:")
children = survival_data[survival_data["age"] < 18]
print(children.head())

# You can sort the data frame by an attribute. This works like the "arrange" function in R.
# You can add an argument "ascending=False" after the value to sort by to sort it in descending order.
print("arrange survival_data in ascending order by age")
by_age = survival_data.sort_values(by="age")
print(by_age.head())

# There is a "groupby" function which functions like the "group_by" function in R.
classes = survival_data.groupby("passengerClass")
# Get the first observation for each group
print("First observation for each class:")
print(classes.first())
# Look at a group
print("3rd class passenger data:")
print(classes.get_group("3rd").head())

# We can also group by multiple attributes.
survived_by_class = survival_data.groupby(["passengerClass", "survived"])
print("Passengers grouped by class and if they survived:")
print(survived_by_class.first())

# We can apply functions to a column of a data frame (like the "apply" function in R).
def string_to_boolean(status):
    if status == "no":
        return 0
    elif status == "yes":
        return 1


print("Boolean survival:")
print(survival_data["survived"].apply(string_to_boolean).head())

# You can add this as a new column to your data frame with the modifications.
survival_data["bool_survived"] = survival_data["survived"].apply(string_to_boolean)
print("new survival_data:")
print(survival_data.head())

# In this example, we changed a string of "yes" or "no" to the numerical 1 or 0. You could have also
# added values to numerical columns, etc.

# You can also apply functions to rows with the "assign" function. It automatically adds the new column
# you create to the data frame.
# (This functions like the "mutate" function in R).
print("Using assign:")
survival_data = survival_data.assign(nonsense=lambda x: survival_data["age"] + survival_data["bool_survived"])
print(survival_data.head())
# Above is a "lambda function". This is a shortcut you can use in certain cases to define a function
# without a formal definition (like an anonymous function in MATLAB). You could also define the function
# before the using the "assign" function as we did above with the "apply" function.

# You can also use the "drop()" function to remove columns. There are many ways you can use this command. Here,
# we are giving it the name of the column to remove, setting axis=1 to tell the function it is a column, and using
# inplace=True to automatically modify the data frame. Instead of the "inplace" argument, you can also set
# survival_data = survival_data.drop(...).
survival_data.drop("nonsense", axis=1, inplace=True)
print("removing nonsense column:")
print(survival_data.head(5))

# You can also rename columns with the "rename" function, like the rename function in R.
print(survival_data.rename(columns={"name": "Name", "bool_survived": "Bool_Survived"}))

# Pandas has a method to check if entries are null. "data.isnull()" returns a boolean array. The "data.dropna()"
# function allows you to drop the rows with null entries. You could also use "data.fillna(x)" to fill the null
# values with the "x" of your choosing (for example, you could fill it with the mean value).

# You can also replace values in the data frame. column_name.replace(1,"one") would replace any 1 in the column
# with the string "one". You can also use lists to replace multiple values
# (column_name.replace([1,2], ["one","two"]))

# Finally, you can put together multiple data frames, and add rows and columns. For two data frames with identical
# columns, you can use "data1.append(data2)". This will add the rows in data1 to the end of data2. If you have the
# same columns, you can also do "pd.concat([data1, data2])". Adding "axis=1" as an argument for these functions
# does the same but for identical rows, adding the columns of data1 to the end of data2. Lastly, there is the
# "join" command which works as the "join" family of commands in r. Doing "data1.join(data2, on=col1, how="left")"
# performs a left-join by matching values in col1.

# There are many functions from R that have analogs in the Pandas library. A good list can be found here:
# https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_r.html
