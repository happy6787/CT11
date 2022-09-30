# a={10,20,30,40}
# print(a,type(a))    ###sets

# ### dictionary is collection of key value pairs
# a={10:20,20:40,30:60,40:80}     ### key:value
# print(a,type(a))        ### dictionary

# a={'Name':'Abhinav','Mob':7758856787,'Age':27,'BGrp':"b+","Sal":120000}
# print(a,type(a))

# print(a['Age'])        ###print(a[key])

# #pirnt(a[])          ###ctrl+space to get list of all keys in bet[]

# a["Sal"]=150000
# print(a['Sal'])     ###It is mutable >>> we can change elements

# print(a)

#a={'Name':'Abhinav', 'Mob':7758856787, 1:999, 2:999, 3:999, 'Age':27, 'BGrp':"b+", "Sal":120000, True:"Yes"}
# print(a[1])         ### As 1 and True are same; Dictionary cannot contain duplicate keys
#                     ### latest value will be considered and overwrite

# print(a[3])                     
###################################################

#a.clear()   ### will clear the elements of dict and return none
#print(a)
####################################################

#a.copy()     ### returns a shallow copy without changing original
#print(a)
###############################################

#print(a.items()) ### returns a view object that displays a list of dictionary's (key, value) tuple pairs.
#################################################

#get

# print(a.get('Mob')) ### will return the value for the specified key if key is in the dictionary.
# print(a.get(4))       ### will return None if the key is not found and value is not specified.

# print(a['bom'])     #### if not using get function and directly finding key which is not present will return key error 
# print(a.get('bom'))   ### if using get function finding key which is not present will return None 

##################################################

#print(a.keys())     ###will return keys from the dictionary
#print(a.values())     ### will return values from the dictionary
##############################################################

# print(a.pop("Age"))    ### will removes and returns an element from a dictionary having the given key.
# print(a)
#####################################################################

# b={"gender":"Male"}     ###updates the dictionary with the elements from another dictionary object or from an iterable of key/value pairs.
# a.update(b)
# print(a)

# b={"Age":28}   
# a.update(b)
# print(a)

# a.update([('x',3),('y',2)])  ### When Tuple is Passed
# print(a)

# a["pass"]='yes'
# print(a)
##The update() method adds element(s) to the dictionary if the key is not in the dictionary. 
# If the key is in the dictionary, it updates the key with the new value.


#######################################################################

# a.setdefault('happy','yes')     ### returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.
# print(a)

# a.setdefault('caste')     ### returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.
# print(a)
###############################################

# a.popitem()    ### will removes and returns the last element (key, value) pair inserted into the dictionary.
# print(a)

# a['profession']='IT Eng'
# print(a)
# a.popitem()
# print(a)
#################################################################