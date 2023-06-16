def solution(prices):
    answer = []
    pricesLength = len(prices)
    for index in range(pricesLength):
        counting = 0
        price = prices[index]        
        for nextIndex in range(index+1,pricesLength):
            if price > prices[nextIndex]: 
                counting+=1
                break
            counting+=1
        answer.append(counting)
    return answer