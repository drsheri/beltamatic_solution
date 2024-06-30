from anytree import Node, RenderTree, LevelOrderIter, Walker
import uuid

# read command line arguments to get an input number for the root node
import sys
root_node = int(sys.argv[1])

numbers_available = [1, 2, 3, 4, 5, 6, 7, 8, 9]



def calculate(op1, operator, number):
    if operator == "+":
        return op1 + number
    elif operator == "-":
        return op1 - number
    elif operator == "*":
        return op1 * number
    elif operator == "/":
        return op1 / number

def is_found_solution(number):
    # if number is found in the numbers available, then it is a solution
    if number in numbers_available:
        return True

# generate unique short uuid for each node
def generate_uuid():
    return str(uuid.uuid4().int)[:8]


# create the root node
# root = Node("%d" % root_node)
root = Node(generate_uuid(), result= root_node)

def add_layer(parent):
    node_val = int(parent.op1 if hasattr(parent, "op1") else root_node)
        # create the first level of children by adding the numbers available one by one
    for number in numbers_available:
        newval = node_val + number
        # if the number is found, then it is a solution and return from function
        temp = Node(generate_uuid(), parent=parent, op1=int(newval), operator="-", number=number, result= node_val)
        if is_found_solution(newval):
            return temp
        newval = node_val - number
        temp = Node(generate_uuid(), parent=parent,op1=int(newval), operator="+", number=number, result= node_val)
        if is_found_solution(newval):
            return temp
        if node_val % number == 0:
            newval = int(node_val / number)
            temp = Node(generate_uuid(), parent=parent,op1=int(newval), operator="*", number=number, result= node_val)
            if is_found_solution(newval):
                return temp
    return False

# call add_layer function for the root node to create the tree
add_layer(root)

for node in LevelOrderIter(root):
    # print(node)
    temp = add_layer(node)
    if temp:
        w = Walker()
        x = w.walk(root, temp)
        for t in x[2]:
            print("%s = %s %s %s" % (calculate(t.op1, t.operator, t.number) ,t.op1, t.operator, t.number))
        break



# for pre, fill, node in RenderTree(root):
#     print("%s %s= %s(%s)%s" % (pre, 
#         node.result if hasattr(node, "result") else root_node, 
#         node.op1 if hasattr(node, "op1") else "",
#         node.operator if hasattr(node, "operator") else "", 
#         node.number if hasattr(node, "number") else ""))