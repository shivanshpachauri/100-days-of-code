import json

# with open("./dummy.json",mode='r') as file:
#     data=file.read()

# print(data)
data={
    "shivansh":["lpu","trinity"],
    "shivali":["lpu","sistech"]
}
new_data={
    "ajay":"bundelkhand-university"
}
# with open('dummy2.json',mode='w') as file:
#     json.dump(data,file,indent=4)
with open("dummy2.json",'r') as file:
    data=json.load(file)
    data.update(new_data)
with open("dummy2.json",'w') as file2:
    json.dump(data,file2,indent=4)

