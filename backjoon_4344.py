n = int(input())
for i in range(n):
    arr = list(map(float, input().split()))
    total = sum(arr[1:])
    avg = total/arr[0]
    stu = sum(score > avg for score in arr[1:])
    print(format((stu/arr[0])*100, ".3f"), "%", sep = '')
