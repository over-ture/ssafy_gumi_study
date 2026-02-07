import java.util.*;
import java.io.*;


public class Main {


    static int[] dx=  {1,-1,0,0,1,-1,1,-1};
    static int[] dy = {0,0,-1,1,1,1,-1,-1};




    static boolean isOOB(int c,int r){
        return r<0 || r>=8 || c<0 || c>=8;
    }


    public static void main(String[] args)throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter ( new OutputStreamWriter(System.out));
        StringTokenizer st ;


        // dx, dy에 대한 인덱스를 저장 (입력값과 dx,dy 방향을 매칭시켜주는 작업)// 딕셔너리
        HashMap<String,Integer> dirs = new HashMap<>();
        dirs.put("R", 0);
        dirs.put("L", 1);
        dirs.put("B", 2);
        dirs.put("T", 3);
        dirs.put("RT", 4);
        dirs.put("LT", 5);
        dirs.put("RB", 6);
        dirs.put("LB", 7);
        int['1' ~ '8' -'1'][ ('a'~'h') -'a'] -> [0~7] [0~7]

        //킹의 위치를 인덱스로 변환
        st = new StringTokenizer(br.readLine());
        String posKing = st.nextToken();
        int nowC =  posKing.charAt(0)-'A';
        int nowR =  posKing.charAt(1)-'1';

        //돌의 위치를 인덱스로 변환
        String posRock = st.nextToken();
        int rockC =  posRock.charAt(0)-'A';
        int rockR =  posRock.charAt(1)-'1';

        //킹의 이동명령 횟수를 입력받는다.
        int N =Integer.parseInt(st.nextToken());

        // 테스트(검증) -> 수행
        while(N-- > 0 ) {
            int nowDir =  dirs.get(br.readLine());

            //사전 테스트 방식 //킹부터  OOBTest 범위 벗어나는지 확인  (1. OOB테스트)
            if(isOOB(nowC + dx[nowDir] , nowR + dy[nowDir] ))continue;


            //TEST FOR ROCK
            if(rockR == nowR + dy[nowDir] && rockC == nowC + dx[nowDir]) {

                //(2. OOB테스트)
                //돌이 범위를 벗어나는 조건 -> 킹에 의해 옮겨진다. -> 범위를 벗어난다.
                if(isOOB(rockC+ dx[nowDir] ,rockR+ dy[nowDir] ))continue;

                rockR+=dy[nowDir] ;
                rockC +=dx[nowDir];
            }

            //CONTINUE (명령어가 씹히지 않으면 킹은 무조건 움직인다 (BASE)
            nowR += dy[nowDir];
            nowC += dx[nowDir];
        }
        //주위 //(로우에 대해서 괄호를 안치면 오답이다.앞에서부터 계산되서 문자열 연산이 되어버리기 때문 )
        System.out.print((char)(nowC+'A') +""+ (nowR+1)+"\n");
        System.out.print((char)(rockC+'A') +""+( rockR+1) );
        bw.flush();
        bw.close();
    }
}