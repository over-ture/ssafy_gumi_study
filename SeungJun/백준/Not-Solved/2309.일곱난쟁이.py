# 2309. 일곱난쟁이
nine = []
for i in range(9) :
    nine.append(int(input())) # 난쟁이 키 입력

nine_sum = sum(nine) # 난쟁이 총합

for i in range(9) : # 전체 중 2개 조합
    for j in range(i + 1, 9) :
        two_of_shorts = [nine[i], nine[j]] # 랜덤 2개 뽑은 조합
        result = [x for x in nine if x not in two_of_shorts]
        if sum(result) == 100 :
            result = set(nine) - set(two_of_shorts)
            result = list(result)
            break

sorted(result)
print(result)
# for i in range(len(result)) :
#     print(result[i])
