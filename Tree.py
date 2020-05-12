from node import Node

class Tree:
    def __init__(self , root):
        """ 
        param root: Node object/none
        """
        self.root=root
        self.value_set={self.root.value}

    def insert_node(self, new_node):

        if not self.search_node(new_node.value):
            a=self.root
            v=new_node.value
        
            while (a is not None):
                p = a
                if (a.value>v):
                    a=a.left_child
            
                else:
                    a=a.right_child
            
            if (new_node.value>p.value):
                p.set_rightchild(new_node)
            else:
                p.set_leftchild(new_node)

            self.value_set.add(v)

    def search_node(self, v):
        """
        :param v: float, value to search
        """
        return v in self.value_set

    def inorder_traversal(self, node):
        """
        traverse the tree inorder, and output the resulting list
        """
        if node.left_child is None and node.right_child is None:
            return [node.value]
        if node.left_child is not None:
            left_res = self.inorder_traversal(node.left_child)
        else:
            left_res = []
        if node.right_child is not None:
            right_res = self.inorder_traversal(node.right_child)
        else:
            left_res = []
        return left_res + [node.value] + right_res

    def self_balance(self):
        """
        turn the tree to be a balanced BST
        """
        def construct_from_list(l):
            n = len(l)
            if n == 0:
                return None
            if n == 1:
                return Node(l[0])
            mid = n//2
            root = Node(l[mid])
            left = construct_from_list(l[:mid])
            right = construct_from_list(l[mid+1:])
            root.set_leftchild(left)
            root.set_rightchild(right)
            return root

        sorted_list = self.inorder_traversal(self.root)
        self.root = construct_from_list(sorted_list)


node1=Node(2)
tree=Tree(node1)
initial_values = [1, 9, 4, 10, 11, 12]
for v in initial_values:
    tree.insert_node(Node(v))
print(tree.root.value)
print(tree.root.left_child.value)
print(tree.root.left_child.left_child is None)
print(tree.inorder_traversal(tree.root))
tree.self_balance()
print(tree.root.value)
print(tree.root.left_child.value)
print(tree.root.right_child.value)
