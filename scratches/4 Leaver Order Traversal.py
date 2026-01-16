from collections import deque

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


def leverOrder(tree):
    if tree is None:
        return []

    q=deque([tree])

    def bfs(queue,acc):
        if not queue:
            return acc
        levelSize = len(queue)

        def consumeLevel(k,val):
            if k==0:
                return val
            node = queue.popleft()
            val.append(node['value'])

            left = node.get('left')
            right = node.get('right')
            if left is not None:
                queue.append(left)
            if right is not None:
                queue.append(right)
            return consumeLevel(k-1,val)

        levelValues = consumeLevel(levelSize, [])
        acc.append(levelValues)

        return bfs(queue,acc)
    return bfs(q,[])



print("Level Order", leverOrder(binary_tree_dict))