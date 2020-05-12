class Node:
    def __init__(self,value,parent=None,left_child=None, right_child=None):
        """
        param value: integer, value of the node
        param parent: Node()
        param left_child: Node()
        param right_child: Node()

        """
     
        self.value=value
        self.parent=parent
        self.left_child=left_child
        self.right_child=right_child

    def set_value(self,new_val):

        self.value=new_val

    def set_parent(self, new_parent, direction):

        self.parent=new_parent

        if (direction=="left" or direction=="Left"):
            self.parent.left_child=self
        else:
            self.parent.right_child=self
    
    def set_leftchild(self, leftchild):
        
        self.left_child=leftchild
        self.left_child.parent=self

    def set_rightchild(self,rightchild):
        self.right_child=rightchild
        self.right_child.parent=self


node1=Node(2)
node2=Node(5)
node2.set_value(8)
node1.set_parent(node2, "left")
#print(node1.parent.value)
        
