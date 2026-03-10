
# [SWEA] 1767 -프로세서 연결하기 (Java)

## 🔗 문제 링크
[SWEA 1767번: 프로세서 연결하기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf&categoryId=AV4suNtaXFEDFAUf&categoryType=CODE&problemTitle=%ED%94%84%EB%A1%9C%EC%84%B8%EC%84%9C&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)


---
## 📊 성능 분석 (Performance)

| 메모리 (Memory) | 시간 (Time) | 언어 (Language) | 코드 길이 (Code Length) |
| :---: | :---: | :---: | :---: |
| **30020 KB** | **152 ms** | **Java 11** | **2477 B** |


## 📌 문제 개요
N x N 크기의 2차원 배열에 프로세서의 위치를 1로 표현합니다.각 프로세스에 외부와 연결되도록 전선을 가로 혹은 세로 방향으로 연결할 수 있으며 이미 경계에 프로세서가 위치하고 있으면 외부와 연결된 것으로 취급합니다. 설치되는 전선은 프로세서나 다른 전선을 통과할 수 없습니다. 전선을 설치하되 외부와 연결된 프로세서 수를 최대화 하면서 전선길이는 최소가 되도록 설치하는 경우의 길이를 출력하세요. 단, 어떤 프로세서가 외부와 연결할 수 없다면 연결하지 않아도 상관없습니다.


---

## 💡 해결 프로세스
 1. 코어를 최대한 연결하도록 하지만, 모든 코어를 연결하지 않아도 되므로 연결할 수 있는 모든 경우의 수를 조사합니다.(부분집합)
 2. 종료조건은 '모든 코어의 연결을 고려했을 경우'에 연결할 수 있는 최대 코어수를 우선 갱신하고 최대 코어수일 때, 최단 전선 길이를 '갱신'합니다. 
 3. 시뮬 단서를 기록했다가 나중에 처리하는 방식은 불편하니, 백트래킹으로 마킹만 건드리면서 현재 연결된 코어수와 현재 전선길이를 '상태'로 지정합니다.
 4. 외부와 연결될 수 있는지 확인하고 연결이 가능하면 외부까지 1을 세팅하고,(디버깅을 위해 다른 값을 세팅해도 됩니다.) 탐색 후 돌아와서 0으로 되돌립니다.
 5. 세팅한 만큼 길이를 카운트하여 누적하고 연결된 프로세스에 1을 추가하여 상태를 갱신합니다.
 6. 연결을 안하는 경우도 고려하여 백트래킹 함수를 세팅합니다.
 (부분집합 전수조사의 기본 그리디는 나중에 생각합니다. 그리고 어차피 지금 선택안하면 최대 코어수를 넘어서지 않음)  

---

## 💻 코드 구조 상세 (Core Logic)

🔍 외부 연결 가능성 체크
```Java
    public static boolean isConnectable(int r, int c, int dir)
    {
        int nr = r; int nc = c;
        while(true) {
            nr += dr[dir]; nc += dc[dir];
            if(nr<0 || nr>=n || nc<0 ||nc>=n) return true;
            if(map[nr][nc]>=1) return false;
        }
    }
```
🔍 외부 벗어날때까지 원하는 값 세팅
```Java
   static  int reset(int r, int c,int dir, int val) {
        int acc= 0, nr= r, nc =c;
        while(true) {
            nr += dr[dir]; nc += dc[dir];
            if(nr<0 || nr>=n || nc<0 ||nc>=n) return acc;
            map[nr][nc]=val; ++acc;
        }

    }
```

🔍핵심 로직 (상태 정의 및 부분집합 알고리즘)
```Java
 static void dfs(int lv,int ret ,int connected) {
        if(lv>= numProcessors) {
            if(maxConnected == connected) { if(ans< ret)return ;  ans = ret;}
            if(maxConnected < connected) {maxConnected = connected;ans = ret;}
            return;
        }

        int[] now = processors[lv];
        for(int d = 0 ;d<4;++d) {
            boolean con = isConnectable(now[0],now[1], d);
            if(con == true) {
                int len = reset(now[0],now[1], d,2);
                dfs(lv+1, ret+len ,connected +1);
                reset(now[0],now[1], d,0);
            }
        }
        dfs(lv+1, ret ,connected); //나 연결 안한다.
    }
```
🔍프로세서 정보는 배열로 관리
```Java
 for (int t = 1; t <= TC; ++t) {
            n = Integer.parseInt(br.readLine());
            processors = new int[12][2];
            ans = Integer.MAX_VALUE;
            maxConnected = 0 ;
            numProcessors=0;
            for (int i = 0; i < n; ++i) {
                st= new StringTokenizer( br.readLine());
                for (int j = 0; j < n; ++j) {
                    map[i][j] = Integer.parseInt(st.nextToken());
                    if(map[i][j]  ==1) {
                        if(i==0|| i==n-1 ||j==0||j==n-1) continue;
                        processors[numProcessors++] = new int[] {i,j};
                    }
                }
            }
            dfs(0,0,0);

            sb.append("#").append(t).append(" ").append(ans).append("\n");
        }
```



---
⚠️ 주의 및 회고
 모든 원소를 고려해야하는 경우가 아니라면 부분집합으로 접근하는것이 맞다( 그리디는 완탐먼저 풀고 생각하자.)
