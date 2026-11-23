import pandas as pd

# pandas-Series
temperature = [34,56,78,89]

# Pandas series
temperature_series =  pd.Series(temperature)
print(temperature_series)

#get specific value
print(temperature_series[1])

print(temperature_series.mean())
print(temperature_series.median())
print(temperature_series.max())
print(temperature_series.min())

# custom indexes
temperature_series =  pd.Series(temperature, index=["Colombo", "kandy", "A","B"])
print(temperature_series)

# Pandas - DataFrame

data = {
    "city":["Colombo", "kandy", "A","B"],
    "temperature":[34,56,78,89],
    "precipitation":[4,6,8,9]
}

data_dataframe = pd.DataFrame(data)

print(data_dataframe)

print(data_dataframe["city"])
print(data_dataframe["temperature"])

print(data_dataframe[["city","temperature"]])

# to add an extra column
data_dataframe["condition"]= ["Sunny", "Cloudy", "Rainy","Normal"]
print(data_dataframe)