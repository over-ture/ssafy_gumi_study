# [BOJ] 1941 - 소문난 칠공주 (Java)

## 🔗 문제 링크

[백준 1941: 소문난 칠공주](https://www.acmicpc.net/problem/1941)

---

## 📊 성능 분석 (Performance)

| 메모리 (Memory) | 시간 (Time) | 언어 (Language) | 코드 길이 (Code Length) |
| :-------------: | :---------: | :-------------: | :---------------------: |
|  **66812 KB**   | **292 ms**  |   **Java 11**   |       **1845 B**        |

## 📌 문제 개요

<h2>문제</h2>
<hr>
<pre>
총 25명의 여학생들로 이루어진 여학생반은 5×5의 정사각형 격자 형태로 자리가 배치되었고, 얼마 지나지 않아 이다솜과 임도연이라는 두 학생이 두각을 나타내며 다른 학생들을 휘어잡기 시작했다. 곧 모든 여학생이 ‘이다솜파’와 ‘임도연파’의 두 파로 갈라지게 되었으며, 얼마 지나지 않아 ‘임도연파’가 세력을 확장시키며 ‘이다솜파’를 위협하기 시작했다.

위기의식을 느낀 ‘이다솜파’의 학생들은 과감히 현재의 체제를 포기하고, ‘소문난 칠공주’를 결성하는 것이 유일한 생존 수단임을 깨달았다. ‘소문난 칠공주’는 다음과 같은 규칙을 만족해야 한다.

</pre>
<ol>
<li>이름이 이름인 만큼, 7명의 여학생들로 구성되어야 한다.</li>
<li>강한 결속력을 위해, 7명의 자리는 서로 가로나 세로로 반드시 인접해 있어야 한다.</li>
<li>화합과 번영을 위해, 반드시 ‘이다솜파’의 학생들로만 구성될 필요는 없다.</li>
<li>그러나 생존을 위해, ‘이다솜파’가 반드시 우위를 점해야 한다. 따라서 7명의 학생 중 ‘이다솜파’의 학생이 적어도 4명 이상은 반드시 포함되어 있어야 한다.</li>
</ol>

<pre>
여학생반의 자리 배치도가 주어졌을 때, ‘소문난 칠공주’를 결성할 수 있는 모든 경우의 수를 구하는 프로그램을 작성하시오.
</pre>

<hr>
<h2>입력</h2>
 
<P>'S'(이다‘솜’파의 학생을 나타냄) 또는 'Y'(임도‘연’파의 학생을 나타냄)을 값으로 갖는 5*5 행렬이 공백 없이 첫째 줄부터 다섯 줄에 걸쳐 주어진다.</P>

<hr>
<h2>출력</h2>
<p> 첫째 줄에 ‘소문난 칠공주’를 결성할 수 있는 모든 경우의 수를 출력한다.</p>
<hr>

<hr>

## 💡 해결 프로세스

1. 25C7은 연산량이 별로 많지 않습니다 . 조합으로 25개중에 7개의 위치를 선별한 후 bfs돌려서 뽑은 7개의 공간이 인접하는지 확인하는 과정을 거칩니다.
2. bfs로 연결성을 확인한다. 방문체크로 모두 연결되었는지 count로 확인합니다.
3. 연결성이 7개면 해당 조합을 답으로 인정하고 1추가합니다.

---

## 💻 코드 구조 상세 (Core Logic)

🔍 조합함수

```Java
static void comb(int lv, int start, int som) {

		if (lv >= 7) {
			if (som < 4)
				return;
			//연결성 체크
			if(isConnected())++ans;

			return ;
		}

		for (int i = start; i < SIZE; ++i) {

			combs[lv] = i;
			int somUp = som;
			if (map[i / 5][i % 5] == 'S')
				somUp += 1;
			comb(lv + 1, i + 1, somUp);
		}
	}
```

🔍 bfs로 연결성을 확인한다. 방문체크로 모두 연결되었는지 count로 확인

```Java
static boolean isConnected() {
        Queue<Integer> q = new LinkedList<>();
        boolean[] visited = new boolean[7];

        q.add(combs[0]);
        visited[0] = true;
        int count = 1;

        while (!q.isEmpty()) {
            int curr = q.poll();
            int r = curr / 5;
            int c = curr % 5;

            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];

                if (nr < 0 || nc < 0 || nr >= 5 || nc >= 5) continue;

                for (int i = 0; i < 7; i++) {
                    if (!visited[i] && combs[i] == (nr * 5 + nc)) {
                        visited[i] = true;
                        q.add(combs[i]);
                        count++;
                    }
                }
            }
        }

        return count == 7;
    }
```

🔍 세팅(사전 준비)

```Java
 public class Main {

	static int[] dr = { 0, 0, 1, -1 };
	static int[] dc = { 1, -1, 0, 0 };
	static int n;
	static int m;
	static int SIZE = 25;
	static int map[][];
	static int ans = 0;
	static int[] combs = new int[7];

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		map = new int[5][5];
		for (int i = 0; i < 5; ++i) {
			String line = br.readLine();
			for (int j = 0; j < 5; ++j) {
				map[i][j] = line.charAt(j);
			}
		}
		comb(0, 0, 0);

		System.out.print(ans);
		//...Logic
}

```

⚠️ 주의 및 회고
조합으로 풀면 생각보다 시간을 많이 먹지 않으므로 조합으로 풀고 bfs로 연결성을 확인하면 좋습니다.
