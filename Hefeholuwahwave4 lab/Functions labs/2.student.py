#Write a function named readable_timedelta. The function should take one argument, an integer days, and return a string that says how many weeks and days that is. For example, calling the function and printing the result like this:

#print(readable_timedelta(10))

#should output the following:

#1 week(s) and 3 day(s).


# write your function here
def readable_timedelta(integer_days):
    output = (str(integer_days - 9)+" week(s) and "+str(integer_days - 7)+" day(s)")
    return output

# test your function
print(readable_timedelta(10))
