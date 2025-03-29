# with open("weather_data.csv") as weather:
#     data=weather.readlines()

# print(data)
import csv
temperature=[]
with open("weather_data.csv") as weather:
    data=csv.reader(weather)
    # print(data)
    for i in data:
        if i[1]!='temp':
            temperature.append(int(i[1]))
            
        print(i)


print(temperature)