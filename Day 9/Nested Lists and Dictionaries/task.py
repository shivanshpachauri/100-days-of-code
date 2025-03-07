# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

# print(travel_log['France'][1])

# for i in travel_log:
#     for j in travel_log[i]:
#         if j=='Lille':
#             print(j)
# nested_list = ["A", "B", ["C", "D"],"D"]


# print(travel_log.values())
# for i in nested_list:
#     if(i=='D'):
#         print(i)
#     for j in i:
#         if(j=='D'):
#             print(j)

# for i in range(len(nested_list)):
#     if(nested_list[i]=='D'):
#         print(i)
#     for j in nested_list[i]:
#         if(j=='D'):
#             print(j,"at position",i+1)
# for i in range(len(nested_list)):
#     print(i+1)
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5
   },
}
for i in travel_log:
    for j in travel_log[i]:
        if(j=='cities_visited'):
            if travel_log[i][j][2]=='Stuttgart':
                print(i,j,travel_log[i][j][2])
        # for k in j:
        #     print(k)
            # if(k=='Stuttgart'):
            #     print(k)
print(travel_log["Germany"]["cities_visited"][2] )