import java.util.*;
import java.io.*;

public class Main {

    static int[] start = new int[2];
    static int[] end = new int[2];
    static int C ;
    static int R ;
    static char[][] map;
    static boolean[][] vis ;
    static int []dr = {0,0,1,-1};
    static int []dc = {1,-1,0,0};
    static int ans = Integer.MAX_VALUE;
    static int[][][] memo;
    public static void dfs(int r, int c, int numMirrors,int dir) {
        if(dir != -1) {
            if(memo[r][c][dir] <= numMirrors )return;
            memo[r][c][dir] = numMirrors;
            if(r==end[0] && c==end[1] ) {
                ans = Math.min( ans , numMirrors);
                return ;
            }
        }


        for(int i =0 ; i< 4 ;++i) {
            int nxtR = r+dr[i];
            int nxtC = c+dc[i];
            if(0> nxtR || nxtR >= R  || 0> nxtC || nxtC >= C)continue;
            if(vis[nxtR ][nxtC]==true )continue ;
            if(map[nxtR ][nxtC]=='*')continue;
            int extra = (dir==i || dir==-1 )?0:1;
            vis[nxtR][nxtC]=true;
            memo[r][c][i] =Math.min(memo[r][c][i],numMirrors + extra);
            dfs(nxtR ,nxtC,memo[r][c][i]  ,i);
            vis[nxtR ][nxtC]=false;
        }

    }
    public static void main(String[] args) throws Exception {


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer( br.readLine());
        C = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        map = new char[R][C];
        vis  = new boolean [R][C];
        memo = new int [R][C][4];

        start[0]=-1;
        end[0]=-1;
        for(int r = 0 ;r<R;++r) {
            String line = br.readLine();
            for(int c = 0 ;c<C;++c) {
                Arrays.fill( memo[r][c],Integer.MAX_VALUE);
                map[r][c] = line.charAt(c);
                if(map[r][c] != 'C')continue;
                if(start[0]==-1)
                {
                    start[0]= r; start[1]=c;
                }
                else {
                    end[0]= r; end[1]=c;
                }

            }
        }
        dfs(start[0],start[1],0,-1);




        System.out.print(ans+"");


    }
}