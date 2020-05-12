from node import Node

class Tree:
    def __init__(self , root):
        """ 
        param root: Node object/none
        """
        self.root=root
        self.value_set={self.root.value}

    def insert_node(self, new_Node):
        a=self.search_node(new_Node)
        if (a!=True):
    
            a=self.root
            v=new_Node.value
        
            while (a is not None):
            
                p=a
                if (a.value>v):
                    a=a.left_child
            
                else:
                    a=a.right_child
            
            if (new_Node.value>p.value):
                p.set_rightchild(new_Node)
            else:
                p.set_leftchild(new_Node)

    def search_node(self,new_Node):
        
        v=new_Node.value
        a=self.root
        while (a is not None):
            
            if (v<a.value):
                a=a.left_child
            
            elif(v>a.value):
                a=a.right_child
            
            else:
                return True
        return False

node1=Node(2)
tree=Tree(node1)
print(tree.root.value)
node2=Node(9)
node3=Node(1)
tree.insert_node(node2)
tree.insert_node(node1)
tree.search_node(node2.value)
