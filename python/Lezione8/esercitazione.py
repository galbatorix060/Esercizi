class Queue:
    pass

class MyStack:
    def __init__(self):
        self.stack = []
    def empty(self):
        return len(self.stack) == 0
    def top(self):
        return self.stack[-1]
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        return self.stack.pop()


def merge(nums1, m, nums2, n):
    for i in nums2:
        nums1.append(i)
    for i in nums1:
        if i == 0:
            nums1.remove(i)
    if 0 in nums1:
        nums1.remove(0)
    nums1.sort()


def is_valid_parenthesis(s: str):
    stack = []
    map = {')' : '(', '}' : '{', ']' : '['}

    for char in s:
        if char in map:
            if not (stack and stack.pop == map[char]):
                return False
        else:
            stack.append(char)
    return True


class LinkedList:
    def __init__(self):
        self.lista = []
        
class Node:
    def __init__(self):
        pass

def is_palindrome(head : Node) -> list[int]:
    head1 = reversed(head)
    if head == head1:
        return True
    else:
        return False
    

def longest_palindrome(s: str):
    stack = []
    dizionario = {}
    count = 0
    for char in s:
        stack.append(char)
    for i in stack:
        for j in stack:
            if i == j:
                count += 1
                dizionario[i] = count
        count = 0
    for k,v in dizionario.items():
        if v % 2 == 0:
            pass
        else:
            dizionario[k].remove(k)
    print(dizionario)
    
    
        