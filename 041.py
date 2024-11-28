#user_input = input("Enter the input String\n")


#Palindrome
# Reverse the String and match with the old String it should be same.
# 1 By using a Traditional method
# 2 Builtin Functions

def reverse_string(input_string):
    reverse_str = " "
    for C in input_string:
        reverse_str = C + reverse_str
    return reverse_str

original_str = "NAMAN"
rev_str = reverse_string(original_str)
print(rev_str)

if original_str == rev_str:
    print("Palindrome")
else:
    print("It is not palindome")