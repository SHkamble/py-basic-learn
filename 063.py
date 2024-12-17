# Dict is very close to jso nn.

phone_book = {"Sharda":1245789,"Varsha":655656686,"chintu":544545}
print(phone_book)
print(len(phone_book))


#How to access?
print(phone_book["Sharda"])
print(phone_book["chintu"])
#print(phone_book["544545"])

# You can access element by key only-Dict

phone_book2 = {"Sharda":15.789,"Varsha":6.566,"ST":55}
print(phone_book2)
print(len(phone_book2))

print(phone_book2['ST'])
print(phone_book2["ST"])
print(phone_book2.get("ST"))


new_dic  = dict(name="sharda",age=20,isFemale=True,Address="Mumbai")
sharda_detail  = {"name":"sharda","age":"20","isFemale":"True","Address":"Mumbai"}
print(new_dic)
print(new_dic['age'])
print(new_dic.get('age'))
print(sharda_detail)
print(sharda_detail.get('Address'))

####
my_dict = {'a':1,'b':2,'c':3,'a':1000000}
print(my_dict)
# here you will see that If you have a duplicate key, latest value of key will be used!!

#How to store keys?
keys = my_dict.keys()
values=my_dict.values()
print(keys)
print(values)


# Get all the keys into a list

keys_list = list(keys)
print(keys_list[0])
print(keys_list[1])
print(keys_list[2])


my_dict = {'a':1,'b':2,'c':3,'a':95}

# dict - key and value


copy_my_dict =my_dict.copy()
print(copy_my_dict)


#my_dict.clear()

print(my_dict)
print(my_dict.items())

