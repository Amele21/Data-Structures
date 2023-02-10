# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
# Recursions

def listsum(numList):
    # base case: numList length must be 1
    if len(numList) == 1:
        return numList[0]  # returns 9
    else:
        # numList[1:] is shortening the list so we can reach base case
        # numList[0] is leaving a diferent value each recursion call
        return numList[0] + listsum(numList[1:])   

        # After base case is reached: 
            # first 9 is returned from above
            # then sum of 7 + 9, 16, is returned
            # sum of 5 + 16 is returned
            # sum of 3 + 21 is returned
            # lastly, sum of 1 + 24 is returned

print(listsum([1,3,5,7,9]))