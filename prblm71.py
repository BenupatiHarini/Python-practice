# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = dummy
        second = dummy

        # Move first ahead by n+1 steps
        for _ in range(n + 1):
            first = first.next

        # Move both until first reaches the end
        while first:
            first = first.next
            second = second.next

        # second.next is node to remove
        to_remove = second.next
        second.next = second.next.next
        # (no explicit free in Python)

        return dummy.next

# Helper functions for demonstration
def build_list(vals):
    if not vals:
        return None
    head = ListNode(vals[0])
    cur = head
    for v in vals[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head

def print_list(head):
    cur = head
    out = []
    while cur:
        out.append(str(cur.val))
        cur = cur.next
    print(" -> ".join(out))

# Example usage
if __name__ == "__main__":
    head = build_list([1,2,3,4,5])
    print("Original list:", end=" ")
    print_list(head)

    n = 2
    sol = Solution()
    head = sol.removeNthFromEnd(head, n)

    print(f"After removing {n}-th node from end:", end=" ")
    print_list(head)
