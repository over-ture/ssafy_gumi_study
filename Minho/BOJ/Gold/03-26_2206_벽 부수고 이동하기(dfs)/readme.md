# [BOJ] 2206 - 벽 부수고 이동하기 (Java)

## 🔗 문제 링크

[백준 2206: 벽 부수고 이동하기](https://www.acmicpc.net/problem/2206)

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
 <p>
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.
</p>
<hr>
<h2>출력</h2>
<p> 첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.</p>
<hr>

<hr>

## 💡 해결 프로세스

1. 괄호쌍문제와 유사하게 현재 stack의 top과 현재 관찰 중인 문자가 괄호쌍을 만족한다면, stack을 팝하고 넘어간다. continue
2. top과 괄호쌍을 이루지 않는다면 stack에 현재 문자를 적재한다.
3. 문자를 적재하면서 ,현재 괄호쌍이 몇 층으로 겹쳐있는지(스택의 사이즈)를 기록한다. [([([) (])])]-> 3층 적재
4. 과정을 마친 후 스택이 비어있지 않다면 괄호쌍을 만들 수 없느 경우이므로 -1을 출력한다.

---

## 💻 코드 구조 상세 (Core Logic)

🔍 괄호 쌍 쌓기 -> 문자를 쌓을 때마다, 스택사이즈 (몇 겹인지) 기록

```Java

for (char c : line) {
			if (!stack.isEmpty()) {
				char top = stack.peek();

				if ((top == '(' && c == ')') || (top == ')' && c == '(')) {
					stack.pop();
					continue;
				}
			}
			stack.push(c);
			ans = Math.max(stack.size(), ans);
		}
		if (0 !=  stack.size())
		{
			ans = -1;
		}
		System.out.print(ans);
```

🔍 세팅(사전 준비)

```Java
 public class Main {

	static int n;
	static int m;
	static int[] arr;

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// StringTokenizer st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(br.readLine());
		String str = br.readLine();
		Deque<Character> line = new ArrayDeque<Character>();
		for (int i = 0; i < str.length(); ++i) {
			line.add(str.charAt(i));
		}
		// 앞에서부터 없애는 것이 이득
		int ans = 0;
		if (line.size() % 2 == 1) {
			System.out.print(-1);
			return;
		}
		//...Logic
}

```

⚠️ 주의 및 회고
스택의 괄호쌍 문제와 유사하나 규칙을 발견하지 못하고 2중 for 문으로 접근하면 시간초과 난다. (((((((((((((......))))))))))))) while문안에서 계속 반복문 돌리면 10만 \*10만이어서 매우 효율이 안좋다.
