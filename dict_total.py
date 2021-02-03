d = {}
marks =0
print("enter Rollno and Marks with a comma and type q to stop:  ")

while True:
    data = input()
    if data == 'q':
        break
    rollno, marks = data.split(',')
    if rollno not in d:
        d[rollno] = int(marks)
    else:
        d[rollno] += int(marks)

print(d)