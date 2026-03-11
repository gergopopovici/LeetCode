from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(0)
        current = l3 
        carry = 0
        while(l1 or l2 or carry): 
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            helper = val1 + val2 + carry
            carry = 0
            if helper >= 10 :
                newNode  = ListNode(helper%10)
                current.next = newNode
                current = current.next
                carry = (helper // 10)
            else:
                newNode = ListNode(helper)
                current.next = newNode
                current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return l3.next
    
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

sol = Solution()

result = sol.addTwoNumbers(l1, l2)

current = result
while current:
    if current.next != None:
        print(current.val, end=" -> ")
    else:
        print(current.val)
    current = current.next