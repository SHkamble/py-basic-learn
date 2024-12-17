# Order dict
my_dict = {'a':1,'b':2,'c': 3}
print(my_dict)
val = my_dict.pop('a')
print(val)


print(my_dict.pop('b'))
print(my_dict.pop('c'))
print(my_dict)
my_dict['a'] = val
print(my_dict)


# Order dict
# Key - value pairs based on the order of insertion

# list,set,tuple,dict,Order dict.- API Automation

from collections import OrderedDict
od = OrderedDict()
od['a'] =45
od['b'] =75
od['c'] =95
od['d'] =25
od['e'] =11

print(od)

# selenium - Insert the web elements into a Dict
# you want to keep the order - login elements, dashboard elements,
 # Dict -  It will not keep the order of Insertion
 # OrderedDict - It will keep the order of insertion

keys = list(od.keys())
print(keys)
keys_sort=keys.sort()
print(keys_sort)
