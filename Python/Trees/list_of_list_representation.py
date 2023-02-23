# Citation
# Problem Solving with Algorithms and Data Structures using Python
# By Brad Miller and David Ranum, Luther College
# https://runestone.academy/ns/books/published/pythonds/index.html
# Meant for pratice and note taking
# Trees

# List of Lists Representation example 1

myTree = \
['a', 
    ['b', 
     ['d',[],[]], 
     ['e',[],[]] 
    ],
    \
    ['c', 
     ['f',[],[]], 
     []
    ] 
]

print(myTree)                           
print('left subtree = ', myTree[1])     # b is the left subtree
print('root = ', myTree[0])             # a is the root
print('right subtree = ', myTree[2])    # c is the right subtree
print('left subtree children = ', myTree[1][1], myTree[1][2])