# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking

# Anagram detection problem for strings ex. 'heart' and 'earth'
# Solution 2: Sort and Compare
# Big-O: O(n^2) or O(nlogn)


def anagramSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()                       # O(n^2) or O(nlogn)
    alist2.sort()                       # O(n^2) or O(nlogn)

    pos = 0
    matches = True

    while pos < len(s1) and matches:    # n
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

print(anagramSolution2('abcde','edcba'))