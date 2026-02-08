import java.util.*;
import java.io.*;


public class Main {


  
    static int[] memo = new int[5005];
    //상태 정의 MEMO란 무엇인가?
    //MEMO[상태] = 상태에 따른 값 저장
    //이전 상태를 활용하여 현재상태를 만들 수 있는가?

    //MEMO[배달해야할 설탕의 무개] = 해당 설탕을 담기 위한 최소 봉지의 개수

    //이전에 구해놓은 "설탕의 무개"를 이미 최소 개수의 봉지로 포장해 놓았다면??
    //     memo[x(이전에 구해 놓은 설탕의 무게) +3 ]-> 무개가 x+3이라면 +1(3kg)봉지 추가
    //	   memo[x(이전에 구해 놓은 설탕의 무게) +5 ]-> 무개가 x+5이라면 +1(5kg)봉지 추가

    //->반대로 ---k '미만'의 모든 설탕의 무게에 대하여 최소 포장 횟수를 구해놓았다면 .
    //후보 1 : memo[k-3], 후보 2: memo[k-5] -> 봉지는 3kg, 5kg 용량만 쓸 수 없고 용량을 "꽉" 채워야함

    //이미 포장 완료된 상태에서 5kg 혹은 3kg을 더 추가한다고 생각...
    //이미 묶어 놓은 데이터 셋|
    // 1| 2| 3| 4| 5| 6| 7| 8| 9|10|11|13|14|
    //------------------------------------------------
    // 0| 0| 1| 0| 1|  |  |  |  |  |  |  |  |
    //	|  |  |  |  |  |  |  |  |  |  |  |  |
    //
    public static void main(String[] args)throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter ( new OutputStreamWriter(System.out));
        Arrays.fill(memo, Integer.MAX_VALUE);
        int N = Integer.parseInt(br.readLine());
        memo[0]=0;

        for(int i = 0 ;i< 5001;++i) {
            if( i>=3 && memo[i-3]!= Integer.MAX_VALUE)
                memo[i] = Math.min(memo[i-3]+1 , memo[i]);
            if( i>=5 && memo[i-5]!= Integer.MAX_VALUE )
                memo[i] = Math.min(memo[i-5]+1 , memo[i]);
        }
        if( memo[N]==Integer.MAX_VALUE)
            memo[N] = -1;
        bw.write(memo[N]+"");
        bw.flush();
        bw.close();
    }
}