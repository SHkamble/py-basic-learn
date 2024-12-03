original_str = "sharda"
reverse_str = lambda original_str : original_str[::-1]

if reverse_str("Sharda") == original_str:
    print("Palindrome")

else:
    print("Not a palindrome")



add = lambda x,y : x+y

print(add(3,4))