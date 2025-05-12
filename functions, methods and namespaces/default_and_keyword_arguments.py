def exceeds_threshold(value, threshold = 0.):
    if value > threshold:
        return True
    else:
        return False

exceeds_threshold(2)

print(sum([1,2,3])) #prints sum of 1, 2 and 3
print(sum([1,2,3],100)) #100 is now a start value and it will be added to the sum

exceeds_threshold(threshold =100, value =2)
#if you specify which is what, order does not matter. 
#this is called KEYWORD ARGUMENT
#if you provide a keyword for one place, you have to do it for all places


