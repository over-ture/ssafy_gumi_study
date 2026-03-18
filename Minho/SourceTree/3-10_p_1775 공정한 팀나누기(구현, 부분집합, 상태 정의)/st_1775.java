import java.io.*;
import java.util.*;
public class Main{
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int[][] arr ;
    static int n;
    static int k;
    static int sum =0;
    static int ans = Integer.MAX_VALUE;
    static void dfs(int lv,int diff, int oth ) {

        if(lv>=n) return;
        if(n - oth < k) return ;

        if( oth>= k && n - oth>= k ) {
            ans = Math.min(ans , Math.abs(diff ));
        }

        dfs(lv+1, diff, oth);
        for(int i = 0 ;i< n;++i) {
            diff -= arr[i][lv]+ arr[lv][i];
        }
        dfs(lv+1,   diff, oth + 1);


    }
    public static void main(String[] args) throws IOException {
        // Please write your code here.

        st = new StringTokenizer( br.readLine());
        n = Integer.parseInt(st.nextToken());
        k =  Integer.parseInt(st.nextToken());
        arr = new int[n][n];


        for(int i = 0 ;i<n;++i)
        {
            st =  new StringTokenizer( br.readLine());
            for(int j = 0 ;j<n;++j) {
                arr[i][j] =  Integer.parseInt(st.nextToken());
                sum += arr[i][j];
            }
        }
        dfs(0, sum, 0);
        System.out.print(ans);
    }
}