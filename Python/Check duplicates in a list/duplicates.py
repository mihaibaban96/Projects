######################EXERCISE####################
########CHECK FOR DUPLICATES IN LIST #############
##################################################


some_list = ['a','b','c','b','d','m','n','n']
duplicates = []


# TODO: Check for duplicates ina  list -> create a simple algorithm   
# For each value in list, check the number of apparitions
# Check if a value has a number of apparitions > 1
# If a value has the number of apparitions > 1, check if it is already in the list of duplicates or not
# If not, append it in the list of duplicates 

for value in some_list:
  if some_list.count(value) > 1:
    if value not in duplicates:
      duplicates.append(value)
print(duplicates)