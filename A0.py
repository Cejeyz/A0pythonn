def finders(file, pattern, alpha):
    file = str(file)
    pattern = str(pattern)
    alpha = int(alpha)
    count = 0
    test = 0
    hold = 0
    tot = 0
    flag = False
    with open(file, 'r') as f:
        data = f.read()
        plen = len(pattern)
        for x in data:
            if x == pattern[count] and flag == False:
                flag = True
                hold = tot
            if flag==True:
                if x != pattern[count]:
                    test = test + 1
            count = count+1
            if test <= alpha and count == plen:
                return hold

            if test > alpha:
                test = 0
                count = 0
                flag = False
            #count = count+1
            tot = tot+1

        return -1


