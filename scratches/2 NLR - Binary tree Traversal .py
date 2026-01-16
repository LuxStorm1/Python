#NODE-LEFT-RIGHT

#1 Method
def preorder(tree):
    if tree is None:
        return []

    return [tree['value']] + preorder(tree.get('left')) + preorder(tree.get('right'))


#2 Method
def BinaryNLFDictionary(tree):

    def processSubtree(node):
        if node is None:
            return []

        def processChildren(left, right):
            def getLeft():
                if not left:
                    return []
                return processSubtree(node.get('left'))

            def getRight():
                if not right:
                    return []
                return processSubtree(node.get('right'))

            return getLeft() + getRight()

        return [node['value']] + processChildren('left' in node and node['left'] is not None, 'right' in node and node['right'] is not None)


    return processSubtree(tree)


binary_tree_dict = {
        'value': 1,
        'left': {
            'value': 2,
            'left': {'value': 4, 'left': None, 'right': None},
            'right': {'value': 5, 'left': None, 'right': None}
        },
        'right': {
            'value': 3,
            'left': None,
            'right': {'value': 6, 'left': None, 'right': None}
        }
    }



print("Cu dictionar", BinaryNLFDictionary(binary_tree_dict))

print(preorder(binary_tree_dict))