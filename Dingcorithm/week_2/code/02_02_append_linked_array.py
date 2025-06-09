# 링크드 리스트의 노드는 두 가지의 정보를 가집니다.
# 1) 노드에 있는 데이터
# 2) 다음 노드가 무엇인지 (포인터)
# 노드라는 객체가 두 가지의 데이터를 가져야 하니, 클래스를 이용할 수 있습니다.
# Node 구현

class Node():
    def __init__(self, data):
        self.data = data    # data는 노드가 가지는 데이터
        self.next = None

# LinkedList 구현
# 1) LinkedList는 self.head에 시작하는 노드를 저장합니다.
# 2) 다음 노드를 보기 위해서는 각 노드의 next를 조회해서 찾아가야 합니다.

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)     # head 에 시작하는 Node를 연결한다.

    def append(self, value):        # LinkedLIst 가장 끝에 있는 노드에 새로운 노드를 연결하는 동작을 구현한다.
        cur = self.head
        while cur.next is not None: # 다음 노드가 없는 마지막 노드까지 이동한다.
            cur = cur.next
        cur.next = Node(value)      # 마지막 노드 뒤에 새로운 노드를 추가한다.

    def print_all(self):            # 모든 노드를 출력하는 동작을 구현한다.
        cur = self.head
        while cur is not None:      # 현재 노드의 값이 없을 때까지 출력한다.
            print(cur.data)
            cur = cur.next

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.print_all()

