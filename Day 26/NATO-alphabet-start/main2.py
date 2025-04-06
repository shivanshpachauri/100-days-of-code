import pandas as pd
df=pd.read_csv("nato_phonetic_alphabet.csv")
user_input=input("enter a word : ").upper()

data_dict={value.letter:value.code for (_,value) in df.iterrows()} 
# for (index,rows) in df.iterrows():
#     # print("key: ",index)

#     print("value ; ",rows.code)


phonetic=[data_dict[x] for x in user_input]
# phonetic=[x for (_,x) in data_dict.items()]

print(phonetic)
