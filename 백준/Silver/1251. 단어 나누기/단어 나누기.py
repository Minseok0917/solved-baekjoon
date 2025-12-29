import sys 

text = str(sys.stdin.readline().strip())

text_len = len(text)
answer = ''
for i in range(1,text_len-1):
    for j in range(i+1,text_len):
        start_text = text[:i][::-1]
        middle_text = text[i:j][::-1]
        end_text = text[j:][::-1]
        new_answer = f'{start_text}{middle_text}{end_text}'
        if new_answer < answer or answer == '':
            answer = new_answer
print(answer)
