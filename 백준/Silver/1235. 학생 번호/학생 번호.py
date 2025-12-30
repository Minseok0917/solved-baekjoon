import sys

n = int(sys.stdin.readline().strip())
student_ids = []
for _ in range(n):
    student_id = str(sys.stdin.readline().strip())
    student_ids.append(student_id)


student_count = len(student_ids)
student_id_prefix_length = len(student_ids[0])


for i in range(1,student_id_prefix_length+1):
    student_id_set = set()
    for student_id in student_ids:
        student_id_set.add(student_id[student_id_prefix_length-i:])
    
    if len(student_id_set) == student_count:
        print(i)
        break

