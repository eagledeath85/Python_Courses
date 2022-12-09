dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

value1_dic1 = dic1[1]
print(value1_dic1)
value2_dic1 = dic1[2]
print(value2_dic1)
# Return an error
value1_dic2 = dic2["3"]

print(dic2.get(3))
# Return None
print(dic3.get("6"))
