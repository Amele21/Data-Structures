# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
# Sorting


# O(nlogn) complexity 
def mergeSort(alist):
    print("Splitting ",alist)
    # base case alist len is less than 1
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        
        # Sort the left and right halves
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        # sort left half
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        # sort right half
        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

    print("Merging ",alist)



alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)