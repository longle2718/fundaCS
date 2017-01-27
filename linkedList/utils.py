'''
Linked list utilities.
Since there's no pointer in python, a dummy node is 
required to modify a linked list

Long Le <longle1@illinois.edu>
University of Illinois
'''
from ListNode import ListNode
import time

def addTwoNumbers(l1,l2):
    # dummy node
    rv = ListNode(-1)
    p = rv

    # carry-in
    cin = 0
    while True:
        if l1 == None and l2 == None:
            break
        
        v1 = 0
        if l1 != None:
            v1 = l1.val
            l1 = l1.next

        v2 = 0
        if l2 != None:
            v2 = l2.val
            l2 = l2.next

        out = cin+v1+v2
        if out >= 10:
            cin = out//10
            out = out%10
        else:
            cin = 0

        p.next = ListNode(out)
        p = p.next

    # carry-out
    if cin > 0:
        p.next = ListNode(cin)
        p = p.next

    # remove the dummy node
    tmp = rv.next
    rv = rv.next
    del tmp

    return rv

def mergeTwoLists(l1,l2):
    rv = ListNode(-1)
    p = rv

    while l1 != None or l2 != None:
        # either the other list is over or
        # the current list has smaller values
        if l2 == None or (l1 != None and l1.val <= l2.val):
            p.next = ListNode(l1.val)
            l1 = l1.next
        else:
            p.next = ListNode(l2.val)
            l2 = l2.next
        p = p.next

    tmp = rv.next
    rv = rv.next
    del tmp

    return rv

def hasCycle(l):
    if l == None or l.next == None:
        return False

    slow = l
    fast = l.next
    while fast != slow:
        if fast == None or fast.next == None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True

def intersection(l0,l1):
    if l0 == None or l1 == None:
        return

    p = l0
    q = l1
    while True:
        if p == None and q == None:
            return
        if p == None:
            p = l1
        if q == None:
            q = l0
        if p == q:
            return p

        p = p.next
        q = q.next

