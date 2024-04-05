class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class  ListNode:
   def addTwoNumbers(self, l1, l2):
        #Create a placeholder node called dummyHead
        # with a value of 0. this node will hold the 
        # resulting linked list
        # Then, initalise a tail and set it to 
        # dummyHead. The pointer will keep track of the 
        # last node in the result list
        dummyHead = ListNode()
        tail = dummyHead
        carry = 0 # this sotres the carry value during addition

        # start a loop that continues until there are no more
        # digits in both loop

        while l1 is not None and l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result 



l1 = [2, 3, 5]
l2 = [4, 5, 6]
myObject = ListNode()
output = myObject.addTwoNumbers(l1, l2)
print(output)
    
