import java.util.*;
import java.io.*;



public class Main {
    static int[] edge= new int [51];
    static int n ;
    static int m ;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb= new StringBuilder();

        st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());


        //n 개의 노드 n-1  개의 간선 -> 트리 리프노드는 m 개

        //(0)->[1]->[2]->[3]....[n-m-1]->[n-m] ----(n - {m - 1} )()()(n-1)(n-1) / (m-1) 개

        edge[0]= -1;
        edge[1]=  0;

        for(int node = n - (m -1) ;node < n ;++node) {
            edge[node] = n-m;

        }
        for(int i = 1 ; i<= n-m;++i) {
            edge[i]= i-1;
        }
        for(int i = 1 ; i<n;++i) {
            sb.append(edge[i]).append(" ").append(i).append("\n");
        }
        System.out.print(sb);
    }


}
