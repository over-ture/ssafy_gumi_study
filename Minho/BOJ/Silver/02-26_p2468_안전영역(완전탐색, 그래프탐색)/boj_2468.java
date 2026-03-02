import java.util.*;
import java.io.*;
public class Main {

    static int n ;

    static int[][] map ;
    static boolean [][] visited;
    static int[] dr = {0,0,1,-1};
    static int[] dc = {1,-1,0,0};
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
    static void DoBruteForce() {
        int maxAreas = 0;

        for(int h = 0; h <= 100; ++h) {
            int currentAreas = DoSimul(h);
            maxAreas = Math.max(maxAreas, currentAreas);
        }
        System.out.println(maxAreas);

    }
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder sb = new StringBuilder();
        StringTokenizer st ;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());

        map = new int [n][n];
        visited= new boolean[n][n];

        //입력 완료
        for(int i = 0 ;i< n ;++i) {
            st = new StringTokenizer( br.readLine());
            for(int j = 0 ; j< n ; ++j) {
                map[i][j] =Integer.parseInt(st.nextToken());
            }
        }
        DoBruteForce();



    }

}
