n, m = map(int,input().split())
arrs = [ list(input()) for _ in range(n)]
answer = -1
cases = []
for row in range(n-7):
    for column in range(m-7):
        white, black = 0, 0
        for rowIndex in range(row,row+8):
            for columnIndex in range(column,column+8):
                boardBlock = arrs[rowIndex][columnIndex]
                if (rowIndex+columnIndex)%2 == 0: 
                    if boardBlock != 'W':
                        white+=1
                    if boardBlock != 'B':
                        black+=1
                else:
                    if boardBlock != 'W':
                        black+=1
                    if boardBlock != 'B':
                        white+=1
        cases.append(white)
        cases.append(black)
print(min(cases))
        