''' Dada uma árvore binária de inteiros e dois limites de intervalo, inferior e superior,
determine a soma dos elementos da árvore que estão neste intervalo de valores
(intervalo fechado).  '''

from BinaryTree import TreeNode, BinaryTree

def addTreeNodes(i, j, node:TreeNode=None):
        if node is None:
            return 0

        nodesLeft = addTreeNodes(i, j, node.left)
        nodesRight = addTreeNodes(i, j, node.right)
        
        if node.data >= i and node.data <= j:
            print(node.data)
            return node.data + nodesLeft + nodesRight
        else:
            return nodesLeft + nodesRight

if __name__ == '__main__':
    
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    n1.right = n3
    
    tree = BinaryTree(n1)
    
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)

    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    
    i = 0
    j = 8
    
    sum = addTreeNodes(i,j, tree.root)
    
    print(f'Sum of elements in the range [%d,%d] = %d\n' %(i, j, sum))
    
    i = 2
    j = 5
    
    sum = addTreeNodes(i,j, tree.root)
    
    print(f'Sum of elements in the range [%d,%d] = %d\n' %(i, j, sum))
    
    i = 30
    j = 80
    
    sum = addTreeNodes(i,j, tree.root)
    
    print(f'Sum of elements in the range [%d,%d] = %d\n' %(i, j, sum))