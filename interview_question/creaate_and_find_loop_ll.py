
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def create_linked_list(arr):
    dummyNode = Node(-1)
    temp = dummyNode
    n = len(arr)
    for i in range(n-2):
        newNode = Node(arr[i])
        temp.next = newNode 
        temp = temp.next
    return dummyNode.next, temp
    
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end='->')
        temp = temp.next
    
def create_loop(arr, i):
    head, tail = create_linked_list(arr)
    print(head.data, tail.data)
    print(i)
    if i == -1:
        return head
    temp = head
    count = 0
    while temp is not None:
        if count == i:
            break
        count += 1
        temp = temp.next
    
    print(temp.data)
    tail.next = temp
    return head
    
def find_loop(head):
    m = {}
    temp = head
    # slow = head
    # fast = head
    # while fast is not None and fast.next is not None:
    while temp is not None:
        # slow = slow.next
        # fast = fast.next.next
        # if slow == fast:
        #     return True
        if temp in m:
            return True
        m[temp] = 1
        temp = temp.next
    return False
    
    
# def generator_func():
#     value = 5
#     while value >= 0:
#         yield value
#         value -= 1

# i = generator_func()

# for item in i:
#     print(item)

    
    

arr = list(map(int, input().split())) # 1 2 3 4 5 -1 2
head, tail = create_linked_list(arr)
head = create_loop(arr, arr[-1])
# print_linked_list(head)
print(find_loop(head))


# SELECT p.id, SUM(o.quantity)
# FROM product p LEFT JOIN
# orders o 
# ON p.id = o.prod_id
# GROUP BY p.id

# SELECT c.id
# FROM customers c LEFT JOIN
# orders o 
# ON c.id = o.cust_id
# WHERE o.id is NULL 

    
    