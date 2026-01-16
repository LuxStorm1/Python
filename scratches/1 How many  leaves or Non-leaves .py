

def NOTleefs(tree):
    if tree is None:
        return 0
    c = tree.get('children')
    if len(c) ==0:
        return 0

    def countC(clist, idx):
        if idx >= len(clist):
            return 0
        return NOTleefs(clist[idx]) + countC(clist, idx+1)

    return 1 + countC(c, 0)

def leefs(tree):
    if tree is None:
        return 0

    c = tree.get('children',[])
    if len(c) ==0:
        return 1

    def countLeefs(clist, idx):
        if idx >=len(clist):
            return 0
        return leefs(c[idx]) + countLeefs(c, idx+1)

    return countLeefs(c, 0)


tree_dict = {
    'value': 1,
    'children': [
        {
            'value': 2,
            'children': [
                {'value': 5, 'children': []},
                {'value': 6, 'children': []}
            ]
        },
        {
            'value': 3,
            'children': []
        },
        {
            'value': 4,
            'children': [
                {'value': 7, 'children': []}
            ]
        }
    ]
}

print("Care nu s frunze",NOTleefs(tree_dict))
print("Sunt frunze", leefs(tree_dict))