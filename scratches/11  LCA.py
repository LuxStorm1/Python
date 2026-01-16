
def lowest_comon_ancestor(tree,val1,val2):

    def find_lca(node):
        if node is None:
            return None
        if node['value']==val1 or node['value']==val2:
            return node
        left = find_lca(node.get('left'))
        right = find_lca(node.get('right'))

        if left and right:
            return node

        return left if left else right

    return find_lca(tree)



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
            'left': {'value': 99, 'left': None, 'right': None},
            'right': {
                'value': 6,
                'left':None,
                'right': None}
        }
    }

lca = lowest_comon_ancestor(binary_tree_dict,4,5)

print(lca['value'])