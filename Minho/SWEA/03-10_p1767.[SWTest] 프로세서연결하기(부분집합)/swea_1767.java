import java.util.*;
import java.io.*;

public class Solution {
    static int[][] map = new int[13][13];
    static int n;
    static int[] dr = {0, 0, 1, -1};
    static int[] dc = {1, -1, 0, 0};
    static int[][] processors;
    static int numProcessors;
    static int ans ;
    static int maxConnected;
    //전선이 외부와 맞닿을 수 있을 때만 호출합니다.
    static  int reset(int r, int c,int dir, int val) {
        int acc= 0, nr= r, nc =c;
        while(true) {
            nr += dr[dir]; nc += dc[dir];
            if(nr<0 || nr>=n || nc<0 ||nc>=n) return acc;
            map[nr][nc]=val; ++acc;
        }

    }
    //외부와 연결될 수 있는지 확인하는 함수입니다.
    public static boolean isConnectable(int r, int c, int dir)
    {
        int nr = r; int nc = c;
        while(true) {
            nr += dr[dir]; nc += dc[dir];
            if(nr<0 || nr>=n || nc<0 ||nc>=n) return true;
            if(map[nr][nc]>=1) return false;
        }
    }
    //'부분집합'에 대한 경우의 수를 모두 조사하는 백트래킹 함수입니다. (연결을 못하면 안해도 되므로 부분집합+ BRUTE FROCE)
    // 배열에 순서를 기록하고 나중에 처리하는것이 아니라 바로 전선 개수화 연결된 코어 개수를 기록, O(4^12)
    // lv이 numProcessors  와같아지는 시점 전까지는  아쉽게도 가지치기가 안된다.(코어가 최대한 많이 연결해야 되는 경우를 고려해야한다.)
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
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
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
        System.out.print(sb);
    }
}