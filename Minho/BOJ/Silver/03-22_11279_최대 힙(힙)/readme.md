# [BOJ] 1021 - 회전하는 큐 (Java)

## 🔗 문제 링크

[백준 1021: 회전하는 큐](https://www.acmicpc.net/problem/1021)

---

## 📊 성능 분석 (Performance)

| 메모리 (Memory) | 시간 (Time) | 언어 (Language) | 코드 길이 (Code Length) |
| :-------------: | :---------: | :-------------: | :---------------------: |
|  **14248 KB**   | **108 ms**  |   **Java 11**   |       **1168 B**        |

## 📌 문제 개요

<h2>문제</h2>
<hr>
<pre>
널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.
</pre>
<ol>
	<li>배열에 자연수 x를 넣는다.</li>
	<li>배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.</li>
</ol>
<pre>
프로그램은 처음에 비어있는 배열에서 시작하게 된다.
</pre>

<hr>
<h2>입력</h2>
<p>첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 입력되는 자연수는 2<sup>31</sup>보다 작다.</p>
<hr>
<h2>출력</h2>
<p>입력에서 0이 주어진 횟수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력하면 된다.</p>
<hr>

## 💡 해결 프로세스

1.  힙 구현하기
2.  삽입 :
<ol>
	<li>우하단에 삽입할 원소를 놓고 부모보다 크다면 값을 swap하고 나의 인덱스를 부모로 바꾼다. </li>
	<li>1번 연산을 반복하다가 부모가 root가 되면 1번 연산 수행 후 무조건 종료한다.</li>
</ol>

3.  삭제 :
<ol>
	<li>root를 일단 출력값으로 저장해놓고 부모,왼쪽자식,오른쪽자식의 값을 비교한다. </li>
	<li>값이 제일 큰 값을 가진 노드의 인덱스인 Biggest를 추출하고 이 인덱스가  왼쪽 혹은 오른쪽 자식 중 하나라면 값을 swap 후, 자신의 인덱스를 Biggest로 바꾼다.</li>
	<li>2의 과정을 반복하다가 Biggest가 부모와 같다면 힙의 정의에 부합하므로 반복을 멈춘다.</li>
</ol>
4.  root는 무조건 1부터 시작해야 2 x p (왼쪽 자식) ,2 x p +1(오른쪽 자식) 공식이 통한다.

---

## 💻 코드 구조 상세 (Core Logic)

🔍 힙 구현

```Java
   //최소 힙의 조건  : parent<= child
class MaxHeap {
	int[] heap;
	int size = 0;

	void resize(int k) {
		heap = new int[k + 1];// 1~k
		size = 0;
	}
	void swap(int idx1, int idx2) {
		int temp = heap[idx1];
		heap[idx1] = heap[idx2];
		heap[idx2] = temp;
	}
	// 부모 자식 맞짱까기
	void push(int x) {
		heap[++size] = x;
		int idx = size;
		// 맨 오른쪽 아래 넣고 부모랑 맞짱까기
		while (idx > 1) {
			int parent = idx / 2;
			if (heap[parent] < heap[idx]) {
				// 부모 부모가 지면
				swap(idx,parent);
				idx = parent;
			}
			else
				break;
		}
	}

	// 우하단 자식 ->top으로 heap[1], 자식들이랑 맞짱까기
	int poll() {
		if (size < 1)
			return -1;
		int ret = heap[1] ;
		heap[1] = heap[size--];
		int parent = 1;
		while (true) {
			int left = parent * 2;
			int right = parent * 2 + 1;
			int idxBiggest = parent;
			// 자식들에게 지는 경우
			if (left <= size && heap[left] > heap[idxBiggest])
				idxBiggest = left;
			if (right <= size && heap[right] > heap[idxBiggest])
				idxBiggest = right;
			// 내가 제일 작네?
			if (parent == idxBiggest)
				break;
			// 부모가 졌으면 (더 크면 스왑)
			swap(parent, idxBiggest);
			parent = idxBiggest;
		}
		return ret;
	}

	int top() {
		if (size == 0)
			return -1;
		return heap[1];
	}

}
```

🔍 세팅(사전 준비)

```Java
 	public class Main {
    static int n;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;// = new StringTokenizer( br.readLine());
        StringBuilder sb = new StringBuilder();
        n = Integer.parseInt(br.readLine());
        MaxHeap heap = new MaxHeap();
        for (int i = 0; i < n; ++i) {
            int now = Integer.parseInt(br.readLine());
            if (now > 0)
                heap.add(now);
            else
                sb.append(heap.poll() + "\n");
        }

        System.out.print(sb + "");

    }
}

```

⚠️ 주의 및 회고
MaxHeap구현 시 왼쪽 자식과 오른쪽자식이 있는지(왼쪽 혹은 오른쪽 자식이 size보다 작거나 같은지 )확인 하기.
