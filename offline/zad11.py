class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def find(root: BSTNode, key):
    while root is not None:
        if root.key == key:
            return root
        root = root.left if key < root.key else root.right

    return None


def insert(root :BSTNode, key):
    side = -1
    while root is not None:
        if root.key == key:
            return
        par = root
        if key < root.key:
            root = root.left
            side = 0
        else:
            root = root.right
            side = 1

    if side == 0:
        root = BSTNode(key)
        par.left = root
    else:
        root = BSTNode(key)
        par.right = root

    root.parent = par
    return


def get_min(root: BSTNode):
    while root.left is not None:
        root = root.left
    return root


def get_max(root: BSTNode):
    while root.right is not None:
        root = root.right
    return root


def climb_leftwards(root: BSTNode):
    while root.parent.right is root:
        root = root.parent
    return root


def climb_rightwards(root: BSTNode):
    while root.parent.left is root:
        root = root.parent
    return root


def get_succ(node: BSTNode):
    if node.right is not None:
        return get_min(node.right)
    else:
        node = climb_leftwards(node)  # climb right branch until it's possible (climb leftwards)
        node = node.parent if node.parent is not None else node  # then jump to parent (jump right) if exists
        return node


def get_pred(node: BSTNode):
    if node.left is not None:
        return get_max(node.left)
    else:
        node = climb_rightwards(node)
        node = node.parent if node.parent is not None else node
        return node


def remove(root: BSTNode, key):
    root = find(root, key)

    if root is None:
        return False

    # if root has two children
    if root.left is not None and root.right is not None:
        succ = get_succ(root)
        root.key = succ.key
        if succ.parent != root:
            succ.parent.left = None
        elif succ.parent is root and succ.right is not None:
            root.right = succ.right
            succ.right.parent = root
        else:
            root.right = None

    # elif root has one child
    elif bool(root.left) != bool(root.right):
        # root is right child
        if root.parent.right is root:
            root.parent.right = root.right if root.right is not None else root.left
        # root is left child
        else:
            root.parent.left = root.right if root.right is not None else root.left

        # root has right child
        if root.right is not None:
            root.right.parent = root.parent
        # root has left child
        else:
            root.left.parent = root.parent

    # if root has no children
    else:
        if root.parent.left is root:
            root.parent.left = None
        else:
            root.parent.right = None

    return True


root = BSTNode(10)
insert(root, 9)
insert(root, 15)
insert(root, 22)
insert(root, 25)
insert(root, 35)
insert(root, 30)
insert(root, 20)
insert(root, 7)
insert(root, 8)
insert(root, 6)
insert(root, 19)
insert(root, 21)
remove(root, 22)
remove(root, 9)
remove(root, 30)
remove(root, 10)
pass
