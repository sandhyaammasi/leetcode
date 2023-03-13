# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(p1,p2):

    if p1 is None:
        head = p2
    if p2 is None:
        head = p1


    head = p1
    while p1.next and p2.next :

        if p1.val == p2.val or (p1.val < p2.val and p1.next.val> p2.val) :
            temp = ListNode()         
            temp.val = p2.val
            temp.next = p1.next
            p1.next = temp
            p1 = p1.next
            p2 = p2.next

        else :
            p1 = p1.next
    if p2 :        
        p1.next = p2
    else:
        p2.next = p1

    return head

list1 = ListNode(1)
head1 = list1
list1.next = ListNode(3)
list1 = list1.next 
list1.next = ListNode(4)
list1 = list1.next 
list1.next = ListNode(6)



list2 = ListNode(1)
head2 = list2
list2.next = ListNode(2)
list2 = list2.next 
list2.next = ListNode(5)
list2 = list2.next 
list2.next = ListNode(7)
list2 = list2.next 
list2.next = ListNode(7)
list2 = list2.next 
list2.next = ListNode(7)
list1 = head1

list2 = head2

'''print("list1")
while list1 is not None:
   print(list1.val)
   list1 = list1.next 

print("list2")
while list2 is not None:   
   print(list2.val)
   list2 = list2.next '''


head = mergeTwoLists(head2,head1)


while head is not None:   
   print(head.val)
   head = head.next 



'''e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

'''