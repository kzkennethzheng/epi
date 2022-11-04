class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge(l1, l2):
    dummy = ListNode()
    curr = dummy
    curr1 = l1
    curr2 = l2

    while curr1 and curr2:
        if curr1.val <= curr2.val:
            curr.next = ListNode(curr1.val)
            curr1 = curr1.next
        else:
            curr.next = ListNode(curr2.val)
            curr2 = curr2.next

        curr = curr.next
    
    for c in (curr1, curr2):
        while c:
            curr.next = ListNode(c.val)
            curr = curr.next
            c = c.next
    
    return dummy.next

def make_list(a):
    dummy = ListNode()
    curr = dummy
    for x in a:
        curr.next = ListNode(x)
        curr = curr.next

    return dummy.next

def convert_list(head):
    def con_helper(curr, a):
        if curr:
            a.append(curr.val)
            con_helper(curr.next, a)
    
    a = []
    con_helper(head, a)
    return a

l1 = make_list([2, 5, 7])
l2 = make_list([3, 11])
r = merge(l1, l2)
print(convert_list(r))