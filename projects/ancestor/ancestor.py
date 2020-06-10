from util import Stack, Queue

def has_parents(ancestors, node):
    children = set()
    for parent, child in ancestors:
        children.add(child)
    if node in children:
        return True
    return False


def earliest_ancestor(ancestors, starting_node):
    q = Queue()
    visited = set()
    most_recent = []

    # ensure that the node has ancestors
    if has_parents(ancestors, starting_node) is False:
        return -1

    # enqueue the starting node
    q.enqueue(starting_node)

    while q.size() > 0:
        v = q.dequeue()
        print(f"Curent node {v}")

        # if the current node hasn't been visited, add it to the visited set
        if v not in visited:
            visited.add(v)

            # if the node has a parent:
            if has_parents(ancestors, v):
                # clear the recent list
                most_recent.clear()

                # enqueue the current node's parent and add it to the most recent list
                for parent, child in ancestors:
                    if child == v:
                        q.enqueue(parent)
                        print(f"Queueing {parent} as the parent of {v}")
                        most_recent.append(parent)
                print()
            else:
                print(f"{v} has no parents\n")
    return min(most_recent)



