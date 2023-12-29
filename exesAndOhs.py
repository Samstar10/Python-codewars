# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

# Examples input/output:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

# SOLUTION

# Parameters: The function takes a string as a parameter
# Returns: It should return the number of instances x occurs and the number of instances o occurs.
#   If they're equal, it should return true.
#   If they're not equal, it should return false
# Pseudocode:
#   initialize the o count
#   initialize the x count
#   loop through the string
#   if str[i] is equal to x, add to the x count
#   if str[i] is equal to o, add to the o count
#   if o count and x count are equal, return true
#   else return false

def xo(s):
    x_count = 0
    o_count = 0
    
    for i in s:
        if i.lower() == 'x':
            x_count += 1
        elif i.lower() == 'o':
            o_count += 1
            
    if x_count == o_count:
        return True
    else:
        return False