
# [BOJ] 1063 - 킹 (Java)

## 🔗 문제 링크
[백준 2578번: 빙고](https://www.acmicpc.net/problem/1063)


---
## 📊 성능 분석 (Performance)

| 메모리 (Memory) | 시간 (Time) | 언어 (Language) | 코드 길이 (Code Length) |
| :---: | :---: | :---: | :---: |
| **16100 KB** | **128 ms** | **Java 11** | **1,747 B** |


## 📌 문제 개요
8x8 체스판 위에서 킹과 돌의 상호작용을 구현하는 시뮬레이션 문제입니다. 킹의 이동 경로에 돌이 있을 경우 돌까지 함께 밀어내야 하는 로직이 핵심입니다.



---

## 💡 주요 설계 (Algorithm Design)

### 1. 빠른 위치 탐색 (`Pair[] cache`)
사회자가 숫자를 부를 때마다 5x5 배열을 전체 탐색하는 것은 비효율적입니다. 
- **해결**: 숫자의 위치(r, c)를 미리 `cache` 배열에 저장하여, 숫자가 불리는 즉시 **O(1)** 의 시간 복잡도로 좌표를 찾아냅니다.
- `cache[숫자] = new Pair(row, col)`
---

## 💡 주요 설계 (Algorithm Design)
### 1. 방향 데이터 매칭 (Direction Mapping)
- 입력으로 들어오는 문자열 명령(R, LT 등)을 배열 인덱스로 변환하기 위해 HashMap을 활용했습니다.

- 배열 기반 방향 벡터 (dx, dy): 8방향 이동을 미리 정의하여 코드의 가독성을 높였습니다.

- 해시맵(딕셔너리) 활용: dirs.put("R", 0);와 같이 입력값과 방향 벡터를 매칭했습니다.

### 2. 좌표 변환 (Coordinate Conversion)
- 체스판의 문자열 좌표(A1 ~ H8)를 배열 인덱스(0 ~ 7)로 변환하는 로직을 적용했습니다.

- Column: charAt(0) - 'A' → [0 ~ 7]

- Row: charAt(1) - '1' → [0 ~ 7]

### 3. 검증 후 실행 (Test Before Move)
- 이 코드는 사전 테스트 방식을 채택하여 안정성을 높였습니다.

- 1. 킹의 OOB(Out Of Bound) 테스트: 킹이 이동할 위치가 판의 밖(isOOB)인지 먼저 확인 후 범위를 벗어나면 명령(킹과 돌의 이동)을 무효화합니다.

- 2. 돌과의 충돌 및 연쇄 이동 테스트: * 1 번의 검증 후, 킹이 이동할 곳에 돌이 있다면, **'미래의 돌의 위치'에 대해 isOOB 테스트 후**  돌도 같은 방향으로 이동시킵니다.

- 이때 돌이 판 밖으로 나간다면 명령에 의한 돌과 킹의 이동을 무효화합니다.

- 최종 이동: 모든 테스트를 통과했을 때만 킹과 돌의 좌표를 갱신합니다.

---

## 💻 코드 구조 상세 (Core Logic)
🔍 OOB(Out Of Bounds) 체크 함수
Java
static boolean isOOB(int c, int r){
    // r, c가 0보다 작거나 8보다 크거나 같은 경우 범위 이탈로 판단
    return r < 0 || r >= 8 || c < 0 || c >= 8;
}

---

## 📝 코드 주석 가이드
Java
while(N-- > 0 ) {
    int nowDir = dirs.get(br.readLine());

    // 1단계: 킹이 범위를 벗어나는지 사전 테스트
    if(isOOB(nowC + dx[nowDir], nowR + dy[nowDir])) continue;

    // 2단계: 킹의 다음 위치에 돌이 있는 경우
    if(rockR == nowR + dy[nowDir] && rockC == nowC + dx[nowDir]) {
        // 돌이 킹에 의해 밀려날 때 판 밖으로 나가는지 확인
        if(isOOB(rockC + dx[nowDir], rockR + dy[nowDir])) continue;

        // 돌 이동 확정
        rockR += dy[nowDir];
        rockC += dx[nowDir];
    }

    // 3단계: 명령이 유효하므로 킹 이동 확정
    nowR += dy[nowDir];
    nowC += dx[nowDir];
}
---

⚠️ 주의 및 회고
문자열 연산 주의: 좌표를 다시 체스판 형식으로 출력할 때 (char)(nowC + 'A') + "" + (nowR + 1)와 같이 처리했습니다.

이유: 빈 문자열("")을 넣지 않거나 괄호 처리가 미흡하면 숫자가 먼저 계산되어 문자가 아닌 아스키코드 합산값이 출력될 수 있기 때문입니다.

효율성: HashMap을 통해 O(1)의 속도로 방향 인덱스를 찾아내어 빈번한 이동 명령을 효율적으로 처리했습니다.
