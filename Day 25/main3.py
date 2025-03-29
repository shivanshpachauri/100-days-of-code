import pandas as pd
df=pd.read_csv("squirrel.csv")

black_count=len(df[df["Primary Fur Color"]=="Black"])
Grey_count=len(df[df["Primary Fur Color"]=="Gray"])
cinnamon_count=len(df[df["Primary Fur Color"]=="Cinnamon"])

print(black_count,Grey_count,cinnamon_count)


dictionary={"Fur color":["Black","Grey","Cinnamon"],"count":[black_count,Grey_count,cinnamon_count]}
countdf=pd.DataFrame(dictionary)
countdf.to_csv("squirrel_count.csv")