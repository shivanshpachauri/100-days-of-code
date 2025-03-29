import pandas as pd
df=pd.read_csv("weather_data.csv")
print(df['temp'])

# print(len(df['temp'])) # number of values

# print(df['temp'].sum()) # sum

average=df['temp'].sum()/len(df['temp'])

print("Average : ",average)

print("Sum : ",df['temp'].sum())

print("number of elements : ",len(df['temp']))


print("maximum value : ",df['temp'].max())


# print(df[df['temp']==df['temp'].max()]) # gets largest temperature row

monday=df[df['day']=="Monday"]
temp_in_fahrenheit=((monday.temp*9)/5)+32
print("\ntemp in fahrenheit",temp_in_fahrenheit)