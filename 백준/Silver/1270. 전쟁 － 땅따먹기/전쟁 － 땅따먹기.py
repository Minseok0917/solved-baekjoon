import sys

n = int(sys.stdin.readline().strip())

answer = []
for _ in range(n):
    numbers = list(map(int,sys.stdin.readline().strip().split()))
    peoples = numbers[0]
    compare = peoples//2
    people_dict = {}
    is_pass = False

    if peoples == 1:
        answer.append(numbers[1])
        continue

    for people_id in numbers[1:]:
        if people_id in people_dict:
            people_dict[people_id] += 1
            if people_dict[people_id] > compare:
                is_pass = True
                answer.append(people_id)
                break
        else:
            people_dict[people_id] = 1
    
    if not is_pass:
        answer.append('SYJKGW')

for answer in answer:
    print(answer)



