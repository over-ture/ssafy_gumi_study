
def selection_sort(a,N):
		for i in range(N-1):
				min_idx = i
				for j in range(i+1,N):
						if a[min_idx] > a[j]:
								min_idx = j
				a[i],a[min_idx] = a[min_idx], a[i]

num = int(input())

for seq in range(1,num+1):
    number = int(input())
    arr = list(map(int,input().split()))
    selection_sort(arr,number)
    result = []
    count = 0
    cnt = 0
    print(f'#{seq}',end=" ")
    for i in range(number):
        if i%2 == 0 :
            print(arr[number-count-1],end = " ")
            cnt +=1
        else:
            print(arr[count],end = " ")
            cnt +=1
        if cnt %2 == 0 and cnt !=0:
            count+=1
        if cnt == 10:
            break
    print()
