import java.io.*;
import java.util.*;
public class Main {
    static long [][] map ;
    static long[] r ;
    static long[] c ;
    static long diag1;
    static long diag2;
    static int n ;
    public static void main(String[] args)throws Exception {

        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw= new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st ;

        n = Integer.parseInt(br.readLine());
        //밸런스 스톤을 입력받을 격자맵
        map = new long[n][n];
        // '각' 열 안의 원소들의 합 ,'각' 행안의 원소들의 합, '각' 대각선 안의 원소들의 합을 저장할 배열과 변수
        r =new long[n];
        c= new long[n];
        int posR=0;
        int posC=0;
        for(int i = 0 ;i< n ;++i ) {
            st= new StringTokenizer(br.readLine());
            for(int j = 0 ;j<n;++j) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if(map[i][j]==0) {
                    posR = i; posC = j; //값이 0인 곳은 밸런스 스톤입니다.
                }
                // i 행 j 열 원소의 값은 'i행 배열' 'j열 배열'
                // i==j라면 위에서 아래로 가는 대각선 변수
                // i+j == n-1 이라면 아래에서 위에가는 대각선 변수에
                // '누적합'을 적용합니다.
                r[i]+=map[i][j];
                c[j]+=map[i][j];
                if(i==j) diag1 += map[i][j];
                if(i+j == n-1) diag2 += map[i][j];
            }
        }
        long sum = 0 ;
        long ans = -1;
        /*assume(추측) 과정입니다.*/
        for(int i = 0 ;i< n ;++i ) {
            if(i != posR) { sum = r[i]; break;}
        }
        //밸런스 스통을 포함하지 않는 '선 위'의 모든 원소합은 같아야 합니다.
        // (* 임의의 선 위의 원소합을 저장해 놓습니다.*)

        /*pre - test*/
        // '임의의 합'과 '밸런스 스톤이 놓인 행의 합의 차이'를 스톤의 값으로 '(임의)지정' 합니다.
        ans = sum - r[posR];
        // '벨런스 스톤이 위치해 있는 선분'에 밸런스 스톤값을 적용해보고  모든 선분 위 합들이 같은지 테스트 합니다.
        c[posC]+=ans;r[posR]+= ans ;
        for(int i=1;i<n;++i) {
            if(r[i] != r[i-1]) ans = -1 ;
            if(c[i] != c[i-1]) ans = -1 ;
        }
        //벨런스 스톤이 대각 선 위에 있는 경우, 대각선 까지 체크
        // (사실 벨런스 스톤이 대각선 위에 없을때도 고려해야하지만 정답으로 처리됨)
        if( posR == posC  &&  diag1+ans != sum  ) ans = -1;
        if( posR + posC == n-1 &&  diag2+ans != sum  ) ans = -1;
        System.out.print(ans);
    }
}
