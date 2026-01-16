
def leavesGenericDict(tree):
    if tree is None:
        return 0
    children = tree.get('children',[])
    #Nu are copii, e frunza , deci return 1
    if len(children) == 0:
        return 1

    def count_in_children(childList, idx):
        if idx >= len(childList):
            return 0
        return leavesGenericDict(childList[idx]) + count_in_children(childList, idx+1)

    return count_in_children(children, 0)

def leavesGenericList(tree):
    if not tree:
        return 0
    def count_in_children(node, idx):
        if idx >= len(node):
            return 0
        return leavesGenericList(node[idx]) + count_in_children(node, idx+1)

    if len(tree) == 1:
        return 1
    return count_in_children(tree, 1)




generic_tree_dict = {
    'value': 1,
    'children': [
        {
            'value': 2,
            'children': [
                {
                    'value': 4,
                    'children': [
                        {'value': 7, 'children': []},
                        {'value': 8, 'children': []},
                        {'value': 11, 'children': []},
                    ]
                },
                {'value': 5, 'children': []}
            ]
        },
        {
            'value': 3,
            'children': [
                {
                    'value': 6,
                    'children': [
                        {'value': 9, 'children': []}
                    ]
                }
            ]
        }
    ]
}
generic_tree_list = [1,
    [2,
        [4,
            [7],  # frunză
            [8]   # frunză
        ],
        [5]       # frunză
    ],
    [3,
        [6,
            [9]   # frunză
        ]
    ]
]
print(leavesGenericDict(generic_tree_dict))
print(leavesGenericList(generic_tree_list))