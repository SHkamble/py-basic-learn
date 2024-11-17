#Assignment 2
#Leap year
year = 2024
is_a_leap_year =False
if(year%4==0 and year%100!=0) or(year % 400 ==0):
 is_leap_year =True
else :
 is_leap_year =False
print (f"{year} is {is_leap_year}")
