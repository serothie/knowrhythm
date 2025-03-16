class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    # def get_kth_node_from_last(self, k):
    #     # length - k + 1 번째
    #     length = 0
    #     cur = self.head
    #     res = self.head
    #     while cur is not None:
    #         cur = cur.next
    #         length += 1
    #     for i in range(length - k):
    #         print(k)
    #         res = res.next
    #     return res

    # def get_kth_node_from_last(self, k):
    #     length = 1  # 시작 노드의 길이를 세기 위해 1부터 시작합니다
    #     cur = self.head
    #
    #     while cur.next is not None:
    #         cur = cur.next
    #         length += 1
    #     end_length = length - k
    #     cur = self.head
    #     for i in range(end_length):
    #         cur = cur.next
    #     return cur

    # 시간복잡도 차이는 없지만 테크닉
    def get_kth_node_from_last(self, k):
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        return slow


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!