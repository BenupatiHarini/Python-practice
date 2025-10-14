# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to swap pairs
def swapPairs(head):
    if not head or not head.next:
        return head

    first = head
    second = head.next

    first.next = swapPairs(second.next)
    second.next = first

    return second

# Function to print linked list
def printList(head):
    temp = head
    while temp:
        print(temp.val, end=" ")
        temp = temp.next
    print()
if __name__ == "__main__":
    # Create linked list 1->2->3->4
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

    print("Original list:", end=" ")
    printList(head)

    head = swapPairs(head)

    print("After swapping pairs:", end=" ")
    printList(head)
