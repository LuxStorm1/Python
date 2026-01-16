
def leaves(tree):
    if tree is None:
        return 0,[]
    left= tree.get('left')
    right= tree.get('right')
    if left is None and right is None:
        return 1,[tree['value']]
    c1,l1 = leaves(left)
    c2,l2= leaves(right)
    return c1+c2,l1+l2

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
            'left': {'value':8, 'left':None, 'right':None},
            'right': {'value': 6, 'left': None, 'right': None}
        }
    }

print(leaves(binary_tree_dict))