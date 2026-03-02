
# [BOJ] 2468 - 안전영역 (Java)

## 🔗 문제 링크
[백준 2468번: 안전영역](https://www.acmicpc.net/problem/2468)


---
## 📊 성능 분석 (Performance)

| 메모리 (Memory) | 시간 (Time) | 언어 (Language) | 코드 길이 (Code Length) |
| :---: | :---: | :---: | :---: |
| **18768 KB** | **260 ms** | **Java 11** | **1649 B** |


## 📌 문제 개요
지역의 높이가 N X N 크기의 2차원 배열로 주어집니다. 비가 일정한 높이만큼 내리고 이 높이 이하의 지역은 모두 물에 잠기는 영역이 됩니다. 물에 잠기지 않은 지역을 안전 영역이라고 부르며, 상하좌우로 인접한 안전 영역은 하나의 지역으로 취급합니다.따라서 비가 내리는 높이에 따라 안전영역의 개수가 달라집니다. 나올 수 있는 안전영역의 최대 개수를 구하세요.   


---

## 💡 해결 프로세스
 1. 모든 지역을 2중 루프로 조사하면서 높이가 H 초과이고 VISITED 되지 않은 영역에서 DFS,BFS를 수행합니다.
 2. DFS나 BFS에서는 현재 위치에서 인접 지역을 조사하면서 특정 높이 초과인 영역만 VISITED 처리합니다.
 3. 2중 루프 안에서 그래프 탐색을 마쳣다면 안전 영역 개수를 누적합니다.  
 3. 높이 1부터 최대 높이에 대해서 1~3 과정을 반복하여 최대 영역 개수를 도출합니다.( 부르트포스) 

---

## 💻 코드 구조 상세 (Core Logic)

🔍 비의 강우량 지정 후 조사(부르트포스)
```Java
    static void DoBruteForce() {
		int maxAreas = 0;

		for(int h = 0; h <= 100; ++h) {
		    int currentAreas = DoSimul(h);
		    maxAreas = Math.max(maxAreas, currentAreas);
		}
		System.out.println(maxAreas);
		
	}
```
🔍 각 강우량에 따른 지역 조사(부르트 포스)
```Java
    static public int DoSimul(int height) {
		int ret = 0 ;
		
		for(int k = 0 ;k<n;++k) Arrays.fill(visited[k],false);
		for(int i = 0 ;i< n;++i)
			for(int j =0  ;j< n ;++j) {
				if(visited[i][j]==true) continue;
				if(map[i][j] <= height)continue;
				if(DoDFS(i,j,height) >=1 )++ret;
			}
		return ret; 
		
	}
```
🔍 그래프 조사
```Java
   static public int DoDFS(int nowr , int nowc ,int height) {
		
		int ret = 1;
		visited[nowr][nowc] = true;
		for(int d = 0 ;d< 4;++d)
		{
			int nr= nowr +dr[d];
			int nc = nowc + dc[d];
			if(nr<0|| nr>=n || nc<0 ||nc>=n) continue; 
			if(map[nr][nc]<= height)continue;
			if(visited[nr][nc]) continue;
			ret += DoDFS(nr,nc, height)+1;
		}
		return ret;
	}
```



---
⚠️ 주의 및 회고
 '근거 없는' 이분탐색, 그리디 같은 방법 생각하지 말고 크기도 적절하니 '전수조사부터' 해보자. 
