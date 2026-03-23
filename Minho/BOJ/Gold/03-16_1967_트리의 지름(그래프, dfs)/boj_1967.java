import java.util.*;
import java.io.*;

public class Main {

    static int n ;
    static ArrayList<int[]>[] edges;

    public static int[] dijik(int start) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(
                (a, b) ->a[0]- b[0]
        );
        int[] ret = new int[2];
        int[] dist = new int[n+1];
        Arrays.fill(dist,Integer.MAX_VALUE);
        dist[start]= 0 ;
        pq.add(new int[] {0,start});
        while(!pq.isEmpty()) {
            int[] picked = pq.poll();
            int val = picked[0];
            int now = picked[1];
            if(dist[now]< val )continue;;
            if(dist[now] > ret[1] ) {
                ret[1]  =dist[now];
                ret[0] = now;
            }

            for(int i = 0;i <edges[now].size();++i) {
                int[]next = edges[now].get(i);
                int nxtNode=  next[1];
                int len = next[0];
                if(dist[nxtNode] <= val+len )continue;
                dist[nxtNode]  = val +len ;
                pq.add(new int[] {dist[nxtNode], nxtNode});
            }


        }
        return ret ;
    }
    public static void main(String[] args) throws Exception {
        StringTokenizer st ;
        BufferedReader br = new BufferedReader(new InputStreamReader (System.in));

        n = Integer.parseInt( br.readLine());
        edges = new ArrayList [n+1];
        for(int i = 0 ;i< n+1;++i) edges[i]=new ArrayList();
        for(int i = 0 ;i< n-1;++i) {
            st= new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int val = Integer.parseInt(st.nextToken());
            edges[from].add(new int[] {val, to});
            edges[to].add(new int[] {val, from});
        }
        int[] ret=  dijik(1);
        int ans = dijik(ret[0])[1];
        System.out.print(ans);
    }

}
