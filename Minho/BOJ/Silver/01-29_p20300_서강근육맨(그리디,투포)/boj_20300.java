import java.io.*;
import java.util.*;
public class Main {

    static String ans = "";

    static BufferedReader br;
    static BufferedWriter bw;
    static StringBuilder sb;
    static StringTokenizer st;
    static int n=0;
    static int[] arr=new int [26];


    public static void main(String args[]) throws Exception
    {



        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter (new OutputStreamWriter (System.out));
        sb = new StringBuilder (new StringBuilder());


        //(1,2,3,4,5,6,7,8,9)  =>
        // 후보 (+최댓값 9): 9+8=17 || 9+7=16 || ... 9+1 = 10  ==> 10 이 후보 중 최솟값
        // 다음 후보(+최댓값 +8)  8+7 =16 ||....|| 8+2 = 10이 후보 중 최솟값
        //최소 합의 후보를 구하기위해 범위를 줄여나가는 그리디 방법
        //정렬 후 양끝의 값을 더한 값들 확인다고 다시 양끝의 범위를 줄여서 최소 요구량(최댓값을 찾는다)
        //그리디 +투포인터

        int n = Integer.parseInt(br.readLine());
        long arr[] = new long[n];

        String line = br.readLine();
        st =new StringTokenizer(line);

        for(int i = 0 ;i< n;++i)
        {
            arr[i]= Long.parseLong(st.nextToken());
        }


        Arrays.sort(arr);
        long ans=  arr[n-1] ;

        int st = 0 ;
        int en = (0 == n%2)? n-1 : n-2;//크기 1일때도 통과

        while(st<en)
        {
            ans = Math.max(ans , arr[st]+arr[en]);
            ++st;
            --en;

        }

        bw.write(ans +"\n");
        bw.flush();
        bw.close();
        br.close();

    }
}