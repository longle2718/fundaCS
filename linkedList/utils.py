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
