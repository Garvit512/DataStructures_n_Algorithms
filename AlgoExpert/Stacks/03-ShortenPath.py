def shortenPath(path):
    stack = []
    absolute_path = False
    if path[0] == '/':
        absolute_path = True
    # Write your code here.
    path_list = path.split('/')
    path_list = [token for token in path_list if token not in["", '.']]
    print(path_list)
    for token in path_list:
        if token == '..':
            if len(stack) != 0:
                if token == stack[len(stack)-1] and absolute_path == False:
                    stack.append(token)
                    print("pushed:", token)
                else:
                    res = stack.pop()
                    print("popped:", res)
            elif len(stack) == 0 and absolute_path == False:
                stack.append(token)
                print("pushed:", token)
        else:
            stack.append(token)
            print("pushed:", token)

    new_path = '/'.join(stack)
    if absolute_path:
        return '/'+new_path
    else:
        return new_path
