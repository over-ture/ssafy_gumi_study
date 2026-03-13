
# [BOJ] 12100 - 2048(easy) (Java)

## 🔗 문제 링크
[백준 12100번: 2048(easy)](https://www.acmicpc.net/problem/12100)


---
## 📊 성능 분석 (Performance)

| 메모리 (Memory) | 시간 (Time) | 언어 (Language) | 코드 길이 (Code Length) |
| :---: | :---: | :---: | :---: |
| **58556 KB** | **268 ms** | **Java 11** | **2131 B** |


## 📌 문제 개요
N x N 크기의 보드 위에서 상, 하, 좌, 우 네 방향 중 하나로 블록을 이동시키는 과정을 최대 5번 반복했을 때, 보드에 만들 수 있는 가장 큰 블록의 수를 찾는 것입니다.
같은 값을 가진 두 블록이 충돌하면 하나로 합쳐지며 값이 2배가 됩니다.한 번의 이동에서 한 블록은 딱 한 번만 합쳐질 수 있습니다. (예: 2 2 4 4가 한쪽으로 밀리면 4 8이 됩니다.)
이동하려는 방향에 빈칸이 있으면 끝까지 미끄러져 이동합니다. 이동하려는 방향에 가까운 블록부터 차례대로 처리됩니다.

---

## 💡 해결 프로세스

매 단계마다 4방향(상, 하, 좌, 우) 선택지가 있으므로, 전체 경우의 수는 $4^5 = 1024$가지입니다. 모든 경우를 다 확인하는 *브루트 포스(Brute Force)*와 *재귀(DFS)*를 사용하여 해결 가능합니다.
 1. 각 페이즈마다 4방향 푸시가 가능하므로 중복순열로 처리할 수 있습니다.
 2. 중복순열에 따른 방향을 저장하며 중복조합재귀를 수행합니다.  
 3. 중복조합  재귀함수가  레벨 5에 도달하면 원본배열의 값을 임시배열에 복사하고 기록한 순서에 따라 임시배열을 미는 작업을 5번 반복하는 시뮬레이션을 돌립니다.
 4. 각 방향에 따른 미는 함수를 만들지 않고 왼쪽으로 미는 함수와  90도 회전 함수를 구현합니다
 5. 밀기 전에 왼쪽으로 미는 함수를 적용하기 위해 회전을 통해 왼쪽으로 밀때 상대적으로 같은 동작을 하도록 만듦니다. (아래로 밀면 시계방향 1번-> 미는 작업-> 반시계 1번)    
 6. 코드에 규칙을 적용하기 위해 왼쪽 아래 오른쪽 위쪽으로 dr, dc 4방향을 지정합니다.(dx, dy 테크닉)
---

## 💻 코드 구조 상세 (Core Logic)

🔍 핵심 변수 
```Java
    static long[][] origin;
    static long[][] simul;
    static long[][] temp;
    static int k = 5;
    static int order[] = new int[5];
    static int[] dr = { 0, 1, 0, -1 };// 왼쪽 -> 반시계방향으로
    static int[] dc = { -1,0, 1, 0 };
    static long ans = 0;
```
🔍 순열 함수 적용
```Java
     static void perm_r(int lv) {
        if (lv >= k) {
            ans = Math.max(ans, DoSimul());
            return;
        }
        for (int d = 0; d < 4; ++d) {
            order[lv] = d;
            perm_r(lv + 1);
        }
    }
```

🔍 회전 함수 
```Java
    static void rotCW(long[][] tar, long[][] tmp, int num) {
        while (num-->0) {

            for (int r = 0; r < n; ++r) {
                for (int c = 0; c < n; ++c) {
                    tmp[r][c] = tar[(n - 1) - c][r];
                }
            }
            for (int r = 0; r < n; ++r) {
                for (int c = 0; c < n; ++c) {
                    tar[r][c] = tmp[r][c];
                }
            }
        }
    }
```

🔍 숫자 압축 함수 (임시 배열에 다음결과 저장하기)
```Java
     static long acc() {
        // 왼쪽으로 합친다 .
        long ret =0;
        for (int i = 0; i < n; ++i) {
            int top = 0;
            long[] arr = new long[n]; 
            long prev = -1;
            for (int j = 0; j < n; ++j) {
                if (simul[i][j] == 0)
                    continue;
                if (simul[i][j] == prev) {
                    ret = Math.max(ret, arr[top - 1] *= 2);
                    prev = -1;
                    continue;
                }
                prev = simul[i][j];
                ret = Math.max(ret, arr[top++] = prev);
            }
            simul[i] = arr.clone();
        }
        return ret;
    }
```
🔍 5번의 순서가 모두 정해졌을 떄 수행
```Java
     static long DoSimul() {
        long ret = 0;
        for (int i = 0; i < n; ++i) simul[i] = origin[i].clone();
        for (int d = 0; d < k; ++d) {
            int dir = order[d];
            //0(1)번  1(2)번 2(3)번 3(4)번
            rotCW( simul,temp,dir);
            ret = Math.max(ret, acc());
            rotCW( simul,temp,4-dir);
        }
        return ret;
    }
```

---
⚠️ 주의 및 회고
 그냥 중복 순열 문제였다. 2차원 배열을 새로 할당하여 현재상태를 저장하고 그 레퍼런스를 재귀 호출 내의 지역변수로 관리하면서 다음 상태(밀어도 같은 경우)를 구하여 가지치기하면 더 시간을 줄있수 있었는데 생각하지 못한 것이 아쉽다.
