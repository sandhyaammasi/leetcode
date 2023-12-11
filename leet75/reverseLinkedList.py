class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(revList):
    revList = revList.next
    if revList is not None:
        reverseList(revList)
        
        '''newRevList.next = revList
        newRevList.next.val = revList.val
        newRevList = newRevList.next'''
        newRevList.next = ListNode(int(revList.val))
        newRevList = newRevList.next
    else:
        newRevList = ListNode()
        global hr
        hr = newRevList




        
list1 = ListNode(1)
head = list1
list1.next = ListNode(2)
list1 = list1.next 
list1.next = ListNode(3)
list1 = list1.next 
list1.next = ListNode(4)
list1 = list1.next 
list1.next = ListNode(5)

head1 = head
'''print("list1")
while head1 is not None:   
   print(head1.val)
   head1 = head1.next '''

global newRevList
newRevList= ListNode(100)
newRevListHead = newRevList

reverseList(head)
 
 

while newRevListHead is not None:   
   print(newRevListHead.val)
   newRevListHead = newRevListHead.next 




