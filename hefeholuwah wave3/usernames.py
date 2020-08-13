#Write a for loop that iterates over the names list to create a usernames list. To create a username for each name, make everything lowercase and replace spaces with underscores. Running your for loop over the list:

#names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

#should create 

#usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]


#HINT: Use the .replace() method to replace the spaces with underscores. Check out how to use this method in this: 

#https://stackoverflow.com/a/12723785


names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []
for name in names:
    name = name.lower()
    name = name.replace(' ', '_')
    usernames.append(name)
# write your for loop here


print(usernames)
