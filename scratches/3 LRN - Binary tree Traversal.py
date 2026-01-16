# LEFT - NODE- RIGHT Traversal
def inOrder(tree):
    if tree is None:
        return []
    return inOrder(tree.get('left')) + [tree['value']] + inOrder(tree.get('right'))

#NON leaf Nodes

def NOT_Leaf_LNR(tree):
    if tree is None:
        return 0

    left = 0
    if 'left' in tree and tree['left']:
        left = NOT_Leaf_LNR(tree['left'])

    right = 0
    if 'right' in tree and tree['right']:
        right=NOT_Leaf_LNR(tree['right'])

    has_children = ('left' in tree and tree['left']) or ('right' in tree and tree['right'])
    k = 1 if has_children else 0

    return k + left+right

def Leaf_Nodes_LNR(tree):
    if tree is None:
        return 0
    left = 0
    if 'left' in tree and tree['left']:
        left = NOT_Leaf_LNR(tree['left'])

    right = 0
    if 'right' in tree and tree['right']:
        right = NOT_Leaf_LNR(tree['right'])

    has_children = ('left' in tree and tree['left']) and ('right' in tree and tree['right'])
    k = 0 if has_children else 1

    return k + left + right


    right =0

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

print("Inorder Traversal",inOrder(binary_tree_dict))

print("How many Non-Leaves", NOT_Leaf_LNR(binary_tree_dict))

print("How many leaves",Leaf_Nodes_LNR(binary_tree_dict))

