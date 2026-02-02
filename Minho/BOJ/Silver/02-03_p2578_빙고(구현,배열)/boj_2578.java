import java.util.*;
import java.io.*;


class Pair{

    int x,y;
    public Pair(int y,int x){
        this.x = x;
        this.y = y;
    }
}
public class Main {

    //빙고 숫자를 저장합니다.
    static int[][] bingo = new int[5][5];

    //각 행에 몇 개의 숫자가 체크되었는지 기록합니다.
    static int[] row = new  int[5];

    // 각 열에 몇 개의 숫자가 체크되었는지 기록합니다.
    static int[] col = new int[5];

    //위로 올라가는 대각선에 몇 개의 원소가 체크되었는지 기록합니다.
    static int crossU = 0;

    //아래로 내려가는 대각선에 몇 개의 원소가 체크되었는지 기록합니다.
    static int crossD = 0;
    static Pair[] cache = new Pair[26];

    static boolean check() {

        //각 행 또는 열에 원소 5개가 체크되었다면 빙고입니다.
        //후보는 5개의 행 , 5개의 열 각 대각선입니다.
        //각 후보에 대해서 5개의 원소가 모두 체크되었는지 테스트합니다.
        int ans =0;
        boolean  ret =false;
        for(int i = 0 ;i< 5;++i) if(5==row[i])++ans;
        for(int i = 0 ;i< 5;++i) if(5==col[i])++ans;
        if(5 == crossU)	++ans ;
        if(5 == crossD) ++ans;

        //3 개 이상의 빙고가 완성되면 TRUE를 반환합니다.
        ret = (3<= ans) ;
        return ret;
    }
    public static void main(String[] args)throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter ( new OutputStreamWriter(System.out));
        StringTokenizer st ;
        //빙고판을 숫자로 채웁니다(입력)
        for(int i = 0; i < 5 ; ++i) {
            st = new StringTokenizer(br.readLine()); //한 줄 읽어서
            for(int j = 0 ; j < 5;++j) {
                bingo[i][j] = Integer.parseInt(st.nextToken()); //파싱 후 할당
                cache[bingo[i][j]] = new Pair(i,j);
            }
        }



        for(int i = 0; i < 5 ; ++i) {
            //사회자의 외치는 숫자들을 한 줄 단위로 읽습니다.
            st = new StringTokenizer(br.readLine());
            for(int j = 0 ; j < 5;++j) {
                //사회자가 부른 숫자들 한 줄을 하나씩 파싱합니다.
                int nowNo = Integer.parseInt(st.nextToken());

                //사회자가 부른 숫자를 빙고판에서 찾습니다. 해당 숫자의 위치는 cache에 기록되어 있습니다.
                int r = cache[nowNo].y;
                int c = cache[nowNo].x;
                //r 행 c열 을 체크합니다.
                ++row[r];
                ++col[c];
                //아래 대각선은  r==c 를 만족
                if(r == c) ++crossD;
                //위로 올라가는 대각선은 합이 항상 상수로 일정합니다.
                if( (5 - 1)==r+c )++crossU;
                //숫자 하나 부르면 매번 빙고인지 테스트합니다.
                if(check()) {
                    bw.write(1 + i*5 +j+"" );
                    bw.flush();
                    bw.close();
                    br.close();
                    return;
                }
            }

        }

    }
}