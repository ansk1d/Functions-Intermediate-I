import random
def randInt(min=''  , max=''   ):
    num = random.random()
    return num

# print(randInt(max=100)*10) 		# should print a random integer between 0 to 100
# print(randInt(max=50)*10) 	# should print a random integer between 0 to 50
# print(randInt(min=50,max=100)*10) 	# should print a random integer between 50 to 100
print(randInt(min=50, max=500)*10)    # should print a random integer between 50 and 500

