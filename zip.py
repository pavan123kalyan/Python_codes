names=['pavan','kalyan','vamc','chaitu']
roll=[23,15,18,20]
designation=['sde','ASE','AASE','SAP']
all_new=list(zip(names,roll,designation))
print(all_new)
#output:It used to zip all columns individually in a list.


#creating a dictionary using zip
#zip() can also be used to pair dictionary keys and values
keys = ["id", "status"]
values = [101, "Active"]
my_dict = dict(zip(keys, values)) # {'id': 101, 'status': 'Active'}
print(my_dict)

#unzipping a list of tuples
pairs = [("A", 1), ("B", 2)]
letters, numbers = zip(*pairs)
print(letters)  # Output: ('A', 'B')
print(numbers)  # Output: (1, 2)


