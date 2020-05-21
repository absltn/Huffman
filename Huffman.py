from collections import Counter, deque


class Node:
    def __init__(self, data='', weight=0, left=None, right=None, is_lvisited=False, is_rvisited=False):
        self.data = data
        self.weight = weight
        self.left = left
        self.right = right
        self.is_lvisited = is_lvisited
        self.is_rvisited = is_rvisited

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        else:
            return False

'''функция huffman(str) принимает строку в кодировке UTF-8, а возвращает битовую строку'''


def huffman(str):
    if len(str) == 1:
        return str, 0b0

    else:
        sym_counter = Counter()
        sym_deque = deque()
        encoding = []

        for i in range(len(str)):

            sym_counter[str[i]] += 1

        sorted_counter = list(sym_counter.most_common())
        sorted_counter.reverse()

        # подготовим две очереди: символов и частот их вхождения в строку

        for i in range(len(sorted_counter)):

            data, weight = sorted_counter[i]
            print(data,weight)
            node = Node(data, weight)
            sym_deque.append(node)

        while len(sym_deque) > 1:

            new_weight = sym_deque[0].weight + sym_deque[1].weight
            leaf_1 = sym_deque.popleft()
            leaf_2 = sym_deque.popleft()
            root = Node(None, new_weight, leaf_1, leaf_2)

            if len(sym_deque) > 0:
                i = 0
                while i < len(sym_deque):
                    if root.weight <= sym_deque[i].weight:
                        sym_deque.insert(i, root)
                        break
                    else:
                        i += 1
            else:
                sym_deque.append(root)

        return str, traverse(sym_deque[0], len(sym_counter))


#функция обхода дерева

def traverse(node, qty):
    pass