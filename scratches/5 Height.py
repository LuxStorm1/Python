
def HeightDict(tree):
    if tree is None:
        return -1

    left = tree.get('left') is not None
    right = tree.get('right') is not None

    if not right and not left:
        return 0

    left = HeightDict(tree.get('left'))
    right = HeightDict(tree.get('right'))

    return max(left,right) + 1

def HeightDict2(tree):
    if tree is None:
        return -1
    left = HeightDict2(tree.get('left'))
    right = HeightDict2(tree.get('right'))

    return max(left,right) + 1


binary_tree_dict = {
        'value': 1,
        'left': {
            'value': 2,
            'left': {
                'value': 4,
                'left': {'value':7, 'left':None, 'right':None},
                'right': None
            },
            'right': {'value': 5, 'left': None, 'right': None}
        },
        'right': {
            'value': 3,
            'left': None,
            'right': {'value': 6, 'left': None, 'right': None}
        }
    }

print("Height v1",HeightDict(binary_tree_dict))
print("Height v2",HeightDict2(binary_tree_dict))

def HeightList(tree):
    if tree is None:
        return -1
    hasLeft = len(tree)>1 and tree[1] is not None
    hasRight = len(tree)>2 and tree[2] is not None

    if not hasLeft and not hasRight:
        return 0

    left = HeightList(tree[1] if len(tree) >1 else None)
    right= HeightList(tree[2] if len(tree)>2 else None)

    return max(left,right) + 1


binary_tree_list = [
    2,
    [3,
        [6,
            [9,
                [17]

             ],
            [10]
        ],
        [8]
    ],
    [5,
        [7],
        [11]
    ]
]


print("Height with list", HeightList(binary_tree_list))