# [BOJ] 2206 - 벽부수고 이동하기 (Java)

## 🔗 문제 링크

[백준 2206: 벽부수고 이동하기](https://www.acmicpc.net/problem/2206)

---

## 📊 성능 분석 (Performance)

| 메모리 (Memory) | 시간 (Time) | 언어 (Language) | 코드 길이 (Code Length) |
| :-------------: | :---------: | :-------------: | :---------------------: |
|  **115456 KB**  | **672 ms**  |   **Java 11**   |       **1603 B**        |

## 📌 문제 개요

<h2>문제</h2>
<hr>
<pre>
N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

</pre>

<hr>
<h2>입력</h2>
 
<P>첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.</P>

<hr>
<h2>출력</h2>
<p> 첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.</p>
<hr>
<h2>제한</h2>
<p>
1<=N <= 200,000 
</p>
<p>
S는 '(' 또는 ')'로 이루어져 있다.
</p>
<hr>

## 💡 해결 프로세스

1. 목표까지의 최단거리를 구하는 것이기때문에 BFS로 접근합니다 .
2. 상태 정의가 중요합니다. 벽을 한번 뚫을 수 있기때문에 BFS에서의 현재 상태를 위치 뿐만이 아니라 벽뚫 찬스를 상태로 포함해서 표현하고 큐에 넣어야 합니다.
3. 벽을 뚫을 수 있을 떄와 뚫을 수 없을 때를 분기하여 다음 상태를 Q에 넣으면서 최단 거리를 구해나갑니다.
4. vis[nr][nc][updatethrough]는 방문상태입니다. updatethrough도 함께 고려해서 다음 상태(다음 최단 거리)를 고려해야 합니다 .

---

## 💻 코드 구조 상세 (Core Logic)

🔍 bfs + 상태 기록

```Java

fArrayDeque<int[]> q = new ArrayDeque<>();
		q.add(new int[] { 0, 0, 1, 1 });// r,c,break,len;
		while (!q.isEmpty()) {
			int[] now = q.poll();

			int r = now[0];
			int c = now[1];
			int through = now[2];
			int len = now[3];
			if (r == n - 1 && c == m - 1) {
				ans = len;
				break;
			}

			for (int i = 0; i < 4; ++i) {
				int nr = r + dr[i];
				int nc = c + dc[i];
				if (nr < 0 || nr >= n || nc < 0 || nc >= m)
					continue;
				if (vis[nr][nc][through] == true)
					continue;
				if (through == 0 && arr[nr][nc] == 1)
					continue;
				int updatethrough =through;
				if (through == 1 && arr[nr][nc] == 1) {
					updatethrough-=1;
				}
				q.add(new int[] { nr, nc, updatethrough, len + 1 });
				vis[nr][nc][updatethrough] = true;
			}
		}

		if (ans == Integer.MAX_VALUE)
			ans = -1;
		System.out.print(ans);
```

🔍 세팅(사전 준비)

```Java
 public class Main {

	static int n;
	static int m;
	static int[][] arr;
	static int[] dr = { 0, 0, 1, -1 };
	static int[] dc = { 1, -1, 0, 0 };
	static int ans = Integer.MAX_VALUE;
	static boolean[][][] vis;
	static int dist[][];

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		arr = new int[n][m];
		vis = new boolean[n][m][2];
		for (int i = 0; i < n; ++i) {
			String line = br.readLine();
			for (int j = 0; j < m; ++j) {
				arr[i][j] = line.charAt(j) - '0';
			}
		}
		//...Logic
}

```

⚠️ 주의 및 회고
위치뿐만이 아니라 추가적인 상태를 고려해야한다,
