def diameter_with_path(tree):
    def height_and_path(node):
        if node is None:
            return 0, []

        left_h, left_path = height_and_path(node.get('left'))
        right_h, right_path = height_and_path(node.get('right'))

        if left_h > right_h:
            return left_h + 1, [node['value']] + left_path
        else:
            return right_h + 1, [node['value']] + right_path

    def reverse_list(lst):
        if not lst:
            return []
        return reverse_list(lst[1:]) + [lst[0]]

    def find_max_diameter(node):
        if node is None:
            return 0, []

        left_h, left_path = height_and_path(node.get('left'))
        right_h, right_path = height_and_path(node.get('right'))

        current_diameter = left_h + right_h

        if node.get('left'):
            left_path_to_root = reverse_list(left_path)
        else:
            left_path_to_root = []

        current_path = left_path_to_root + [node['value']] + right_path

        left_d, left_d_path = find_max_diameter(node.get('left'))
        right_d, right_d_path = find_max_diameter(node.get('right'))

        if current_diameter >= left_d and current_diameter >= right_d:
            return current_diameter, current_path
        elif left_d > right_d:
            return left_d, left_d_path
        else:
            return right_d, right_d_path

    return find_max_diameter(tree)


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


print(diameter_with_path(binary_tree_dict))