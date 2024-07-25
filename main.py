# Реалізація двійкового дерева взята з конспекту з доданими додатковими вузлами
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

# Завдання 1
def find_max(root):
    current = root
    while current.right is not None:
        current = current.right
    return current.val

# Завдання 2
def find_min(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.val

# Завдання 3
def sum_of_values(root):
    if root is None:
        return 0
    return root.val + sum_of_values(root.left) + sum_of_values(root.right)

# Початкові вузли
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

# Нові вузли
root = insert(root, 10)
root = insert(root, 12)
root = insert(root, 13)
root = insert(root, 15)
root = insert(root, 21)

# Пошук найбільшого значення
max_value = find_max(root)
print(f"Найбільше значення у дереві: {max_value}")

# Пошук найменшого значення
min_value = find_min(root)
print(f"Найменше значення у дереві: {min_value}")

# Пошук суми всіх значень
total_sum = sum_of_values(root)
print(f"Сума всіх значень у дереві: {total_sum}")