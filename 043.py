# Reverse slicing method
original_str = "NAMAN"
#new*
def is_palindrome(original_str):
    rev_str = original_str[::-1]
    print(rev_str)
    if original_str == rev_str:
       print("Palindrome")
    else:
      print("It is not")
print(is_palindrome(original_str))