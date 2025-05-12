'''
This program demonstrates exponential growth using a classic problem: 
the "Wheat and Chessboard Problem." Starting with one grain of wheat 
on the first square of a chessboard, the amount doubles on each 
subsequent square. The goal is to calculate and display the number 
of grains on each square and compute the total amount across all 
64 squares. The compound_by_period function simulates this doubling, 
and the built-in sum function is used to total the grains.
'''

balance = 100.0
rate = 0.03

print(0, round(balance,2))
for n in range(1,11):
    balance = round(balance * (1 + rate), 2)
    print(n, round(balance,2))

def compound(balance, rate, num_periods):
    print(0, round(balance,2))
    for n in range(1,num_periods+1):
        balance = round( balance * (1 + rate), 2)
        print(n, balance)
    return balance


# Do NOT modify code above this line
# -----------------------

# Below is the function definition for compound_by_period. 
# Remove the comment before the function definition and 
# complete the function 

def compound_by_period(balance, rate, num_periods):
    balances = [round(balance,2)]
    for n in range(1,num_periods+1):
        balance = round( balance * (1 + rate), 2)
        balances.append(balance)
    return balances

# Compute the number of grains of wheat on each square (starting with 1 grain, doubling each time)
wheat = compound_by_period(1, 1, 63)  # 64 squares, so 63 periods after the first

# Print the list of grains on each square
print(wheat)

# Compute the total number of grains
total_wheat = sum(wheat)

# Print the total
print("Total grains of wheat on the chessboard:", total_wheat)

# Do NOT modify the change_per_period() function
# -----------------------------
def change_per_period(balances):
    for i in range(0,len(balances)-1):
         balances.append(balances[i+1] - balances[i])
    return balances
