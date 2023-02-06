# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking

a=5     # 1
b=61    # 1
c=10    # 1
        # 3

for i in range(n):          # n
   for j in range(n):       # n
      x = i * i             # 1
      y = j * j             # 1
      z = i * j             # 1
                            #3n^2

for k in range(n):          # n
   w = a*k + 45             # 1
   v = b*b                  # 1
                            # 2n

d = 33                      # 1

# T(n) = 3 + 3n^2 + 2n + 1
# T(n) = 3n^2 + 2n + 4
