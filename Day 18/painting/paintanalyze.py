# import painting
import colorgram
color=colorgram.extract(r"C:\Users\shiva\PycharmProjects\100 Days of Code - The Complete Python Pro Bootcamp\Day 18\painting\painting.jpg",26)
# color=colorgram.extract('painting.jpg',30)
li=[]
for i in color:
    r=i.rgb.r
    g=i.rgb.g
    b=i.rgb.b
    tuple=(r,g,b)
    li.append(tuple)

print(li)
# [(211, 210, 210), (189, 167, 121), (57, 90, 111), (113, 43, 35), (163, 89, 64), (210, 212, 214)]
