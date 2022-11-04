from re import I


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_ht_balanced(root):
    def ht_traversal(curr):
        if not curr:
            return (True, float('-inf'))
        
        lbalanced, lht = ht_traversal(curr.left)
        if not lbalanced:
            return (False, None)
        rbalanced, rht = ht_traversal(curr.right)
        if not rbalanced:
            return (False, None)
        
        ht = None
        if not curr.left and not curr.right:
            ht = 0
        elif curr.left and curr.right:
            if abs(lht - rht) > 1:
                return (False, None)

            ht = max(lht, rht) + 1
        elif curr.left:
            if lht > 1:
                return (False, None)

            ht = lht + 1
        else:
            if rht > 1:
                return (False, None)

            ht = rht + 1
    
        return (True, ht)
    
    balanced, _ = ht_traversal(root)
    return balanced

root1 = Node(1)
l1 = Node(2)
l2 = Node(3)
l3 = Node(4)
root1.left = l1
l1.left = l2
l2.left = l3
print(is_ht_balanced(root1))

root2 = Node(1)
root2.left = l1
l1.left = None
root2.right = l2
print(is_ht_balanced(root2))

class Wrapper:
    def __init__(self, best=0):
        self.best = best

def lgst_comp_subtree_sz(root, wrapper):
    if not root:
        return (True, 0)

    lcomplete, lsz = lgst_comp_subtree_sz(root.left, wrapper)
    rcomplete, rsz = lgst_comp_subtree_sz(root.right, wrapper)

    if lcomplete and rcomplete:
        nxt = 1 + 2*min(lsz, rsz)
        wrapper.best = max(wrapper.best, nxt)
        return (True, nxt)
    else:
        nxt = max(1, lsz, rsz)
        wrapper.best = max(wrapper.best, nxt)
        return (False, nxt)

w = Wrapper()
lgst_comp_subtree_sz(root2, w)
print(w.best)