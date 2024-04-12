class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    @staticmethod
    def fromArray(arr: list) -> 'ListNode':
        if not arr:
            return ListNode()

        head = ListNode(arr[0])
        curr = head
        for i in arr:
            newNode = ListNode(i, prev=curr)
            curr.next = newNode
            curr = newNode

        return head

    def print(self) -> None:
        curr = self
        arr = []
        while curr.next:
            curr = curr.next
            arr.append(str(curr.val))

        print(' -> '.join(arr))
