# [BOJ] 33517 - 징검다리 게임 (Java)

## 🔗 문제 링크

[백준 33517: 징검다리 게임](https://www.acmicpc.net/problem/33517)

---

## 📊 성능 분석 (Performance)

| 메모리 (Memory) | 시간 (Time) | 언어 (Language) | 코드 길이 (Code Length) |
| :-------------: | :---------: | :-------------: | :---------------------: |
|  **77076 KB**   | **488 ms**  |   **Java 11**   |       **1488 B**        |

## 📌 문제 개요

<h2>문제</h2>
<hr>
<pre>
상혁이는 징검다리 게임을 하고 있다. 이 게임에는 
$N$개의 칸으로 구성된 징검다리가 있으며, 플레이어는 첫 번째 칸에서 출발하여 마지막 칸에 도달하면 게임에서 승리한다.

징검다리의 각 칸은 비어 있거나 곰 또는 지뢰 중 하나가 존재하며, 모든 곰의 체력은
$1$ 이상의 정수이다. 또한 첫 번째 칸과 마지막 칸은 비어 있다. 징검다리 게임의 명령어는 아래와 같다.

</pre>
<ol>
	<li>
		점프 (J): 다음 칸으로 이동한다. 이동한 칸에 곰이나 지뢰가 있다면 플레이어는 패배한다.
	</li>
	<li>
		공격 (A): 다음 칸에 있는 곰의 체력을 $1$ 깎는다. 곰의 체력이  $0$이 되면 다음 칸의 곰은 사라진다. 다음 칸이 빈칸이라면 아무 일도 일어나지 않으며, 다음 칸에 지뢰가 있다면 지뢰가 폭발하여 플레이어는 패배한다.
	</li>
	<li>
		지뢰 제거 (D): 다음 칸에 있는 지뢰를 제거한다. 다음 칸에 지뢰가 없다면 아무 일도 일어나지 않는다.
	</li>
<ol>
<pre>
상혁이는 징검다리 게임에서 승리하기 위해 키 매크로를 개발했다. 키 매크로는 점프(J), 공격(A), 지뢰 제거(D)로 구성된 길이 
$K$의 문자열을 입력받으면 문자열의 첫 번째 명령어부터 차례대로 실행한다. 마지막 명령어를 수행한 이후에는 첫 번째 명령어부터 다시 실행한다. 명령어를 
$10^{100}$회 실행했을 때 마지막 칸에 도달하지 못했다면 플레이어는 패배하며, 키 매크로는 실행 중 게임에서 승리하거나 패배할 경우 즉시 종료된다.
</pre>

징검다리의 상태와 상혁이가 입력한 문자열이 주어졌을 때, 상혁이가 마지막 칸에 도달하여 게임에서 승리할 수 있다면 YES, 승리할 수 없다면 NO를 출력하시오.

</pre>

<hr>
<h2>입력</h2>
 
<pre>
첫 번째 줄에 징검다리의 칸의 개수  $N$이 주어진다. $(3 \leq N \leq 500\,000)$ 

두 번째 줄에 징검다리의 각 칸의 상태를 의미하는 정수 $A_1, A_2, \cdots, A_N$가 공백으로 구분되어 주어진다.
$(-1 \leq A_i \leq 500\,000$; $A_1 = A_N = 0)$ 

</pre>

<hr>
<h2>출력</h2>
<p>상혁이가 마지막 칸에 도달하여 게임에서 승리할 수 있다면 YES, 승리할 수 없다면 NO를 출력한다.</p>
<hr>

<hr>

## 💡 해결 프로세스

1. 명령어의 길이가 길 뿐더러 순환적으로 명령어를 총 10^100번 까지 수행할 수 있습니다. 2중 반복문으로 처리한다는 것은 말이 안됩니다.
2. 이동은 점프할 때만 할 수 있고 그 전까지는 다음 좌표의 지뢰를 제거하거나 몬스터를 공격하는 전처리 과정입니다.
3. 명령어를 분석하여 점프 하기 이전까지의 전처리과정을 하나로 압축해서 저장합니다.
4. 전처리 후 이동가능 여부를 확인한 다음에 이동 가능하다면 이동하고 그렇지 않다면 패배합니다.
5. 징검다리를 검사할 때마다, 다음 번째의 점프의 전처리 과정으로 이동이 가능한지 여부만 판단하기 떄문에 o(N)의 시간만 소요됩니다.
6. 명령어가 순환되기때문에 첫 번째 점프의 압축은 한번만 적용하고 그 다음 부터는 순환을 고려한 압축을 적용해야합니다.

---

## 💻 코드 구조 상세 (Core Logic)

🔍 핵심 로직 ( 좌표 압축 +전처리 적용 후 다음 단계 진행 가능여부 판단)

```Java
		if(numJumps ==0) {
			System.out.print( "NO" );
			return ;
		}
		int[][] memo = new int[numJumps+1][2];
		int j=0; int i = 0;
		int cnt = numJumps + 1; // cycle
		while (cnt > 0 &&numJumps>0) {
			if (commands.charAt(i) == 'J') {
				memo[j][0] = cntA;
				memo[j++][1] = cntD;
				cntA = 0;
				cntD = 0;
				cnt--;
			}
			if (commands.charAt(i) == 'A') {
				cntA++;
			}
			if (commands.charAt(i) == 'D') {
				cntD++;
			}
			++i;
			i = i % commands.length();
		}
		// o(n)
		int nxtIdx = 1;
		int jump = 0;
		boolean win=true;
		while (nxtIdx <n) {
			if (arr[nxtIdx] >=0 && arr[nxtIdx] <= memo[jump][0]) {
				//몬스터때리는 경우 혹은 몬스터가 없는경우(0)
			}
			else if (arr[nxtIdx] < 0 && memo[jump][1]>0 ) {
				//지뢰 제거 가능 여부
			}
			else {
				win = false;
				break;
			}
			jump = 1+ (jump) % (numJumps);
			++nxtIdx;
		}
		System.out.print( win?"YES":"NO" );
```

🔍 세팅

```Java
import java.io.*;
import java.util.*;

public class Main {
	static int n;
	static int m;
	static int[] arr;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		n = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		arr=new int[n];
		for (int i = 0; i < n; ++i) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		m = Integer.parseInt(br.readLine());
		String commands = br.readLine();
		int numJumps = 0;
		int cntA = 0;
		int cntD = 0;
		for (int i = 0; i < commands.length(); ++i) {
			if (commands.charAt(i) == 'J')
				++numJumps;
		}
	}
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
