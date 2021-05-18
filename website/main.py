import re


def PasswordAuth(password):
    while True:
        if len(password) < 8:
            flag = -1
            break
        elif not re.search("[a-z]", password):
            flag = -1
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            break
        elif not re.search("[0-9]", password):
            flag = -1
            break
        elif not re.search("[_@$]", password):
            flag = -1
            break
        elif re.search("\s", password):
            flag = -1
            break
        else:
            flag = 0
            print(f'Valid Password', {password})
            break

    if flag == -1:
        print(f'Invalid password', {password})


def BreadthFirstSearch():
    from collections import defaultdict

    class Graph:

        # Constructor
        def __init__(self):

            self.graph = defaultdict(list)

        def addEdge(self, u, v):
            self.graph[u].append(v)

        def BFS(self, s):

            visited = [False] * (max(self.graph) + 1)

            queue = [s]

            visited[s] = True

            while queue:

                s = queue.pop(0)
                print(s, end=" ")

                for i in self.graph[s]:
                    if not visited[i]:
                        queue.append(i)
                        visited[i] = True

    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.BFS(2)


def DuplicateNum():
    def colored(r, g, b, text_rocks):
        return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text_rocks)

    numbers = [1, 2, 3, 4]
    print(f'Unsorted Numbers: ', numbers)
    numbers.sort()
    indexOfNum = numbers[1]
    # print(indexOfNum)
    print(f'Sorted Numbers: ', numbers)
    Error1Array = []
    for i in numbers:
        if i == indexOfNum:
            Error1Array.append(i)
        # print(i)

        indexOfNum = i
    print(f'There is a Duplicate Number: ', Error1Array)

    text = 'Algorithm By KARTHIKEYA-'
    colored_text = colored(7, 214, 254, text)
    print(colored_text)


def check(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if (re.search(regex, email)):
        print("Valid Email")

    else:
        print("Invalid Email")
