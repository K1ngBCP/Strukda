class Node:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None
        self.height = 0

class BST :
    def __init__ (self):
        self.root = None
    
    def add_node (self, val , currNode = None):
        #jika BST masih kosong langsung isi ke root
        if self.root is None:
            self.root = Node(val)
            return

        #meng-copy root node
        if currNode is None :
            currNode = self.root

        #jika new node < current node left isi ke bagian kiri
        if val <= currNode.value :
            #jika ternyata child kiri kosong, langsung isi dgn yg baru
            if currNode.left_node is None:
                currNode.left_node = Node(val)
                return
            #jika masih ada child, lanjut traverse ke bawah    
            else :
                self.add_node(val, currNode.left_node)
        
        #jika new node > current node right isi ke bagian kiri
        if val > currNode.value:
            #jika ternyata child kanan kosong, langsung isi dgn yg baru
            if currNode.right_node is None:
                currNode.right_node = Node(val)
                return
            #jika masih ada child, lanjut traverse ke bawah
            else :
                self.add_node(val, currNode.right_node)
                       
    def preorder(self, node = None):
        if node is None:
            node = self.root

        if node:
            #visit
            print(node.value, end = ' ')

            #traverse kiri
            if node.left_node is not None:
                self.preorder(node.left_node)

            #traverse kanan
            if node.right_node is not None:
                self.preorder(node.right_node)

    def postorder(self, node = None):
        if node is None:
            node = self.root

        if node:
            #traverse kiri
            if node.left_node is not None:
                self.postorder(node.left_node)
            #traverse kanan
            if node.right_node is not None:
                self.postorder(node.right_node)
            #visit
            print(node.value, end = ' ')

    def inorder(self, node = None):
        if node is None:
            node = self.root

        if node:  
            #traverse kiri  
            if node.left_node is not None:
                self.inorder(node.left_node)
            #visit
            print(node.value, end = ' ')
            #traverse kanan
            if node.right_node is not None:
                self.inorder(node.right_node)

#Data : 54, 58, 66, 94, 71, 70, 64, 16, 13, 70
myBST = BST()
myBST.add_node(54)
myBST.add_node(58)
myBST.add_node(66)
myBST.add_node(94)
myBST.add_node(71)
myBST.add_node(70)
myBST.add_node(64)
myBST.add_node(16)
myBST.add_node(13)
myBST.add_node(70)

print('preorder :')
myBST.preorder()
print('\npostorder : ')
myBST.postorder()
print('\ninorder  :')
myBST.inorder()


class AVL(BST):
    def find_height(self, node = ''):
        if node == '':
            node = self.root

        if node is None:
            return -1

        left = self.find_height(node.left_node)
        right = self.find_height(node.right_node)
        return max(left,right) + 1

myAVL = AVL()
myAVL.add_node(4)
myAVL.add_node(2)
myAVL.add_node(1)
myAVL.add_node(-10)
myAVL.add_node(-15)
myAVL.add_node(-8)
myAVL.add_node(-2)
myAVL.add_node(7)
print('\navl inorder : ')
myAVL.inorder()

print()
print(myAVL.find_height())