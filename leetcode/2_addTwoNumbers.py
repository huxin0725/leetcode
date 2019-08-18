
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        flag = 0
        result = ListNode(0)
        a = []
        while l1!=None or l2!=None:
            if l1==None:
                k1=0
            else:
                k1 = l1.val
            if l2==None:
                k2=0
            else:
                k2= l2.val
            key = k1 + k2+flag
            if key >= 10:
                flag = 1
                key = key % 10
            else:
                flag=0
            a.append(key)
            if l1!=None:
                l1 = l1.next
            if l2!=None:
                l2=l2.next
        if flag!=0:
            a.append(flag)
        for i in range(0,len(a)):
            node = ListNode(a[len(a)-i-1])
            p = result.next
            result.next = node
            node.next = p
        return result.next

l1 = ListNode(1)
l1.next=ListNode(0)
l1.next.next=ListNode(0)
l1.next.next.next=ListNode(0)
l1.next.next.next.next=ListNode(0)
l1.next.next.next.next.next=ListNode(0)
l1.next.next.next.next.next.next=ListNode(0)
l1.next.next.next.next.next.next.next=ListNode(1)
l2 = ListNode(5)
l2.next=ListNode(6)
l2.next.next=ListNode(4)
solution = Solution()
result = solution.addTwoNumbers(l1,l2)
while result!=None:
    print(result.val)
    result=result.next


