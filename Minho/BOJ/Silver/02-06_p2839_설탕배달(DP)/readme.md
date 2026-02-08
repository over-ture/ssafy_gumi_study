
# [BOJ] 1063 - 킹 (Java)

## 🔗 문제 링크
[백준 2578번: 빙고](https://www.acmicpc.net/problem/1063)


---
## 📊 성능 분석 (Performance)

| 메모리 (Memory) | 시간 (Time) | 언어 (Language) | 코드 길이 (Code Length) |
| :---: | :---: | :---: | :---: |
| **14404 KB** | **108 ms** | **Java 11** | **808 B** |


## 📌 문제 개요
상근이는 요즘 설탕공장에서 설탕을 배달하고 있습니다. 설탕을 정확하게 N kg 배달해야 할 때, 3kg 봉지와 5kg 봉지를 최소한으로 사용하여 배달하는 방법을 찾는 문제입니다.



---

## 💡 주요 설계 (Algorithm Design)

### 1. 상태 정의 (`memo[k]`)
memo[k]를 다음과 같이 정의합니다.
memo[k]: $k$ kg의 설탕을 담기 위해 필요한 최소 봉지 개수

### 2. 점화식
-  $k$ kg을 만드는 방법은 단 두 가지 경로뿐입니다.
 
- 1. $(k-3)$ kg에서 3kg 봉지를 하나 추가하는 경우

- 2. $(k-5)$ kg에서 5kg 봉지를 하나 추가하는 경우

- (단, $k$ 미만의 설탕들은 이미 최소 봉지로 개수로 표현되어 있다는 가정이 전제되어 있어야 통하는 논리입니다.) 
- 결론: $$memo[k] = \min(memo[k-3] + 1, memo[k-5] + 1)$$



---

## 💻 코드 구조 상세 (Core Logic)

🏗️ 초기화 (Initialization)
Java
Arrays.fill(memo, Integer.MAX_VALUE); //봉지로 표현할 수 없으면 MAX_VALUE 처리입니다.
memo[0] = 0; // 0kg을 배달하는 봉지 개수는 0개 (기본 사례)


🔄 반복문 (Iteration)작은 무게($3$kg)부터 목표 무게($N$)까지 차례대로 최적의 값을 쌓아 나갑니다.
Java
for(int i = 0; i < 5001; ++i) {
    // 1. 3kg 봉지를 추가할 수 있는 경우
    if(i >= 3 && memo[i-3] != Integer.MAX_VALUE)
        memo[i] = Math.min(memo[i-3] + 1, memo[i]);
    
    // 2. 5kg 봉지를 추가할 수 있는 경우
    if(i >= 5 && memo[i-5] != Integer.MAX_VALUE)
        memo[i] = Math.min(memo[i-5] + 1, memo[i]);
}
🔍조건 검사와 갱신
 ---> memo[i-3] != Integer.MAX_VALUE: 이전에 해당 무게를 만드는 것이 불가능했다면, 거기에 봉지를 더해도 의미가 없으므로 유효성을 검사합니다.
 Math.min(...): 기존에 저장된 방식보다 현재 새로 계산한 방식(3kg나 5kg를 추가한 방식)이 봉지 개수가 더 적다면 갱신합니다.
---
4. 시뮬레이션  
무게 (i),memo[i] 값,선택된 봉지 (경로),설명
0,0,-,기준점 (0kg은 0개)
1,INF,-,만들 수 없음
2,INF,-,만들 수 없음
3,1,memo[0] + 3kg,3kg 봉지 1개
4,INF,-,만들 수 없음
5,1,memo[0] + 5kg,5kg 봉지 1개
6,2,memo[3] + 3kg,3kg 봉지 2개
7,INF,-,만들 수 없음
8,2,memo[3] + 5kg,3kg 1개 + 5kg 1개
9,3,memo[6] + 3kg,3kg 봉지 3개
10,2,memo[5] + 5kg,5kg 봉지 2개
11,3,memo[8] + 3kg,최종 답안 (5kg+3kg+3kg)

⚠️ 주의 및 회고
5. 복잡도 분석
시간 복잡도: $O(N)$ - 0부터 N까지 단 한 번의 루프만 수행합니다. (최대 5000번)
공간 복잡도: $O(N)$ - 결과를 저장하기 위한 memo 배열이 필요합니다.