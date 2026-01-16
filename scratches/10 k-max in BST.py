
def kSmallesElement(tree,k):
    def inorder(node):
        if node is None:
            return []
        return inorder(node.get('left')) + [node['value']] + inorder(node.get('right'))

    sorted_tree = inorder(tree)

    def kth(arr,idx,target):
        if idx >= len(arr) or idx<0:
            return None
        if idx == target-1:
            return arr[idx]

        return kth(arr,idx+1,target) if idx <target-1 else None

    return kth(sorted_tree,0,k) if sorted_tree else None




valid_bst = {
    'value': 10,
    'left': {
        'value': 5,
        'left': {'value': 3, 'left': None, 'right': None},
        'right': {'value': 7, 'left': None, 'right': None}
    },
    'right': {
        'value': 15,
        'left': {'value': 12, 'left': None, 'right': None},
        'right': {'value': 20, 'left': None, 'right': None}
    }
}

print(kSmallesElement(valid_bst,3))