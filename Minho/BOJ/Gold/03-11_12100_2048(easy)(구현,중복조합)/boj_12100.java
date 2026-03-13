import java.io.*;
import java.util.*;

class Main {
    static int n = 100;
    static long[][] origin;
    static long[][] simul;
    static long[][] temp;
    static int k = 5;
    static int order[] = new int[5];
    static int[] dr = { 0, 1, 0, -1 };// 왼쪽 -> 반시계방향으로
    static int[] dc = { -1,0, 1, 0 };
    static long ans = 0;

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

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(br.readLine());
        origin = new long[n][n];
        simul = new long[n][n];
        temp = new long[n][n];
        for (int i = 0; i < n; ++i) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; ++j) {
                origin[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        perm_r(0);
        System.out.print(ans);


    }

}