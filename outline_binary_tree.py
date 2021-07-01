class Node(object):
    def __init__(self, value):
        self.value = value

    value = None
    left = None
    right = None


def main():
    root_node = Node(1)
    root_node.left = Node(2)
    # root_node.left.right = Node(9)
    root_node.right = Node(3)
    root_node.right.left = Node(4)
    # root_node.right.left.left = Node(8)
    root_node.right.right = Node(5)
    root_node.right.right.left = Node(6)
    root_node.right.right.right = Node(7)

    """
            1
           / \
          2   3
             / \
            4   5
               / \
              6   7
    """
    final_output = []
    visited_levels = []
    left_view(root_node, 0, visited_levels, final_output)
    final_output.reverse()
    final_output.pop()
    visited_levels = []
    right_view(root_node, 0, visited_levels, final_output)
    print(final_output)

def left_view(node: Node, level, visited_levels, final_output):
    if not node:
        return
    if not node.left and not node.right:
        # leaf node
        if level not in visited_levels:
            # print(f"({level}) {node.value}")
            final_output.append(node.value)
            visited_levels.append(level)
        return

    if node.left:
        if level not in visited_levels:
            # print(f"({level}) {node.value}")
            final_output.append(node.value)
            visited_levels.append(level)
        left_view(node.left, level + 1, visited_levels, final_output)

    if node.right:
        if level not in visited_levels:
            # print(f"({level}) {node.value}")
            final_output.append(node.value)
            visited_levels.append(level)
        left_view(node.right, level + 1, visited_levels, final_output)


def right_view(node: Node, level, visited_levels, final_output):
    if not node:
        return
    if not node.left and not node.right:
        # leaf node
        if level not in visited_levels:
            # print(f"({level}) {node.value}")
            final_output.append(node.value)
            visited_levels.append(level)
        return

    if node.right:
        if level not in visited_levels:
            # print(f"({level}) {node.value}")
            final_output.append(node.value)
            visited_levels.append(level)
        right_view(node.right, level + 1, visited_levels, final_output)

    if node.left:
        if level not in visited_levels:
            # print(f"({level}) {node.value}")
            final_output.append(node.value)
            visited_levels.append(level)
        right_view(node.left, level + 1, visited_levels, final_output)



if __name__ == '__main__':
    main()
