# List Methods

my_list.append(5)        # adds 5 to the end of my_list

your_list.index(10)      # returns first index of 10 in your_list (error if not found)

his_list.count('c')      # returns how many times 'c' appears in his_list

her_list.sort()          # sorts her_list in place (error if mixed types)

my_list.reverse()        # reverses order of my_list in place

# Tuples are immutable – can't append, sort, or reverse
# But they support some querying methods:

my_tuple.index(11)       # returns first index of 11 in my_tuple

your_tuple.count('d')    # returns how many times 'd' appears in your_tuple

# Strings act like lists of characters and are also immutable
# Indexing, slicing, and + for concatenation work on strings too

'1234'.isdigit()         # returns True – all characters are digits

'ABCdef'.islower()       # returns False – not all characters are lowercase

'ABCDEF'.isupper()       # returns True – all characters are uppercase

'ABCdef'.lower()         # returns 'abcdef' – all lowercase version

'ABCdef'.upper()         # returns 'ABCDEF' – all uppercase version

'hello'.capitalize()     # returns 'Hello' – first char uppercase, rest lowercase

'Python'.startswith('Py')   # returns True – string starts with 'Py'

'filename.csv'.endswith('.csv')  # returns True – string ends with '.csv'
