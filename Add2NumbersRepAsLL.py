# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        node = self
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result


class Solution:
    def to_number(self, llist: ListNode) -> int:
        sum_list = 0
        idx = 0
        while llist:
            sum_list = sum_list + (llist.val * pow(10, idx))
            idx = idx + 1
            llist = llist.next

        return sum_list

    def to_list(self, num: int) -> ListNode:
        root = None
        for digit in reversed(str(num)):
            if not root:
                root = ListNode(int(digit))
            else:
                ptr = root
                while ptr.next:
                    ptr = ptr.next
                ptr.next = ListNode(int(digit))

        return root


    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        return self.to_list(self.to_number(l1) + self.to_number(l2))


sol = Solution()
# l1 = ListNode(2, ListNode(4, ListNode(3)))
# l2 = ListNode(5, ListNode(6, ListNode(4)))
l1 = sol.to_list(9999999)
l2 = sol.to_list(9999)

# print(sol.to_number(l1))
print(l1.print())
print(l2.print())

l3 = sol.addTwoNumbers(l1, l2)

print(l3.print())
