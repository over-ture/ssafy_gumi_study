import java.util.*;
import java.io.*;
public class Main {

    static char[] laby;
    static int n = 0;
    static int m = 0;
    static int[] dr = {0,0,1,-1};
    static int[] dc = {1,-1,0,0};
    static int[] dist;
    static int bfs(int pos) {

        Queue <Integer> que = new ArrayDeque();
        dist[pos]=1;
        que.add(pos);
        while(!que.isEmpty()) {
            int now= que.poll();
            if(now ==n*m-1) {
                return dist[now];
            }

            for(int k=0;k<4;++k) {

                // 평탄화 해제 ->좌표
                //행: 위치를 열의 크기로 나눈 몫 (행: 길이가 'm'인 선분이 몇 개인가?)
                //열: 위치를 열의 크기로 나눈 나머지(열: 길이가 'm'인 선분을 제외한 나머지 열의 크기 )
                int nr = (now/m) + dr[k];
                int nc = (now%m) + dc[k];

                /*좌표 -> 평탄화*/
                int next = nr *m +nc;
                /*oob 테스트*/
                if(nr<0|| nr >= n || nc<0||nc>=m ) continue;
                /*다음에 이동할 위치가 0이라면 미로이다.*/
                /*다음에 방문할 위치가 벽이라면 넘어간다.*/
                /*다음에 방문할 위치에 이미 방문한 전적이 있다면 넘어간다.(처음 방문했을 떄 기록한 값이 이미 최소 거리일 것)*/
                if(laby[next] =='0'||  dist[next]<=dist[now]+1 )continue;
                dist[next]=dist[now]+1;
                que.add(next);
            }
        }
        //도달 못하는 경우
        return -1;
    }
    public static void main(String[] args)throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line ;
        StringTokenizer st= new StringTokenizer( br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        laby = new char[n*m];
        dist = new int [n*m];
        Arrays.fill(dist, Integer.MAX_VALUE);
        for(int i = 0 ;i< n;++i) {
            line = br.readLine();
            for(int j =0  ;j< m ;++j) {
                //평탄화를 수행합니다.
                // 2차원 배열은 각 행이 주소로 관리되기 때문에 캐시지역성(지역)의 효과를 누리기 힘들다.
                //실제로 물리적으로 관리하기 위해서 0~ m*n -1 ->[0][0] ~ [n-1][m-1]로 대응
                laby[i * m + j ] = line.charAt(j);
            }
        }
        System.out.print(bfs(0));





    }
}
