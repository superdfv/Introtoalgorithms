#checks each combination of first and last names, and returns true if the full name is found.
def does_name_exist(first_names, last_names, full_name):
    splitname = full_name.split() 
    for first in first_names:
        if first == splitname[0]:
            for last in last_names:
                if last == splitname[1]:
                    return True
    return False




first_names = ['sally', 'jean', 'mike', 'bob0']
last_names = ['jhon', 'gonzalez0', 'perez', 'smith']
full_name = 'bob0 gonzalez0'
does_name_exist(first_names, last_names, full_name)