from node import node

class linkedist:
  def __init__(self,head:node):
    self.head=head
  def add(self,new_node:node): #will add the element in the beginig
    new_node.next=self.head
    self.head=new_node
  def delete():
    self.head=self.head.next
  def display(self):
    n=self.head
    while(n!=None):
      print(n.value)
      n=n.next
    