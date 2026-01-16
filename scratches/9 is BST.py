def validate(tree):
    def validate_helper(node,minV, maxV):
        if node is None:
            return True
        val=node['value']

        if val<minV or val>maxV:
            return False

        leftValid = validate_helper(node.get('left'),minV,val)
        rightValid = validate_helper(node.get('right'),val,maxV)

        return leftValid and rightValid

    return validate_helper(tree, float('-inf'), float('inf'))


binary_tree_dict = {
        'value': 10,
        'left': {
            'value': 5,
            'left': {
                'value': 3,
                'left': {'value':1, 'left':None, 'right':None},
                'right': None
            },
            'right': {'value': 6, 'left': None, 'right': None}
        },
        'right': {
            'value': 20,
            'left': {'value': 13, 'left': None, 'right': None},
            'right': {
                'value': 64,
                'left':None,
                'right': None}
        }
    }

print(validate(binary_tree_dict))