import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String line = br.readLine();
        String bomb = br.readLine();
        int bombSize = bomb.length();

        
        char[] stack = new char[line.length()];
        int nowTop = 0;

        for (int i = 0; i < line.length(); i++) {
            // 1. 무조건 스택에 넣는다
            stack[nowTop++] = line.charAt(i);

            // 2. 스택의 길이가 폭발 문자열 길이 이상일 때만 검사
            if (nowTop >= bombSize) {
                boolean isBomb = true;

                // 스택의 Top 부분과 폭발 문자열을 비교
                for (int j = 0; j < bombSize; j++) {
                    if (stack[nowTop - bombSize + j] != bomb.charAt(j)) {
                        isBomb = false;
                        break;
                    }
                }

                // 3. 폭발 문자열이면 포인터만 내린다
                if (isBomb) {
                    nowTop -= bombSize;
                }
            }
        }

        // 결과 출력
        if (nowTop == 0) {
            System.out.print("FRULA");
        } else {
            for (int i = 0; i < nowTop; ++i) {
                sb.append(stack[i]);
            }
            System.out.print(sb);
        }
    }
}