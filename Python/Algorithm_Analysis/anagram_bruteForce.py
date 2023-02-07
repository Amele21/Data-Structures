# Anagram detection problem for strings ex. 'heart' and 'earth'
# Solution 3: Brute Force
# Big-O: O(n!)

def anagramSolution3(s1,s2, i, exist):
    length = len(s1)
    data = list(s1)
   
    if data == list(s2): 
        return True    
    else: 
        for j in range(i, length): 
            # swap
            data[i], data[j] = data[j], data[i] 

            # recursion
            rec = anagramSolution3(data, s2, i+1, exist) 
            if rec == True:
                exist = True
          
            # backtrack
            data[i], data[j] = data[j], data[i]

 
        return exist




print(anagramSolution3('abc', 'bca', 0, exist=False))


