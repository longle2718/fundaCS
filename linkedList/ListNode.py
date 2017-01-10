'''
List node

Long Le <longle1@illinois.edu>
University of Illinois
'''

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def serialize(l):
    buf = []

    while l != None:
        buf.append(l.val)
        l = l.next

    return buf

def deserialize(buf):
    head = ListNode(-1)
    p = head

    while len(buf) > 0:
        p.next = ListNode(buf.pop(0))
        p = p.next

    tmp = head.next
    head = head.next
    del tmp

    return head
