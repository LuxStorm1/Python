

def sum_dict_depth(tree,k):
    if tree is None or k<0:
        return 0
    if k==0:
        return tree['value']
    children = tree.get('children',[])

    def sum_at_levelK(childList, idx):
        if idx>=len(childList):
            return 0
        return sum_dict_depth(childList[idx],k-1) + sum_at_levelK(childList,idx+1)

    return sum_at_levelK(children,0)

def sum_list_depth(tree,k):
    if not tree or k<0:
        return 0
    if k==0:
        return tree[0]

    def sum_at_levelkk(node, idx):
        if idx>=len(node):
            return 0
        return sum_list_depth(node[idx],k-1) + sum_at_levelkk(node,idx+1)

    return sum_at_levelkk(tree,1)

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

print(sum_dict_depth(generic_tree_dict,3))

print(sum_list_depth(generic_tree_list,2))