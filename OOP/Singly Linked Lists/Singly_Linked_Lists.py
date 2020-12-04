class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self
    
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self

class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()


# Additional Challenges
# These are challenging! Hop up to a whiteboard, grab a cohort mate if available, and try to work through these together.

# remove_from_front(self) - remove the first node and return its value
# remove_from_back(self) - remove the last node and return its value
# remove_val(self, val) - remove the first node with the given value
# Consider the following cases:
# the node with the given value is the first node
# the node with the given value is in the middle of the list
# the node with the given value is the last node
# insert_at(self, val, n) - insert a node with value val as the nth node in the list
# Consider the following cases:
# n is 0
# n is the length of the list
# n is between 0 and the length of the list

#  Create a new Python file and recreate the Node and SList classes
#  Add the add_to_front method to your SList class
#  Add the print_values method to your SList class
#  Add the add_to_back method to your SList class
#  Practice the above in code and on paper/whiteboard. Then try to write these methods from scratch without referencing the platform!
#  Practice the above on your computer and on paper or a whiteboard. Then try to write these methods from scratch without referencing the platform!
#  NINJA BONUS: complete the remove_from_front method
#  NINJA BONUS: complete the remove_from_back method
#  NINJA BONUS: complete the remove_val method
#  SENSEI BONUS: complete the insert_at method
#  SENSEI BONUS: consider and account for edge cases for all previous methods