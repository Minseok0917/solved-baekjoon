def init():
    while True:
        try:
            n = input()
            l = len(n)
            message = 'yes'
            if n == '0':
                break
            for i in range(l//2):
                if n[i] == n[-1-i]:
                    message = 'yes'
                    continue
                else:
                    message = 'no'
                    break 
            print(message)
        except:
            return  
init()
        