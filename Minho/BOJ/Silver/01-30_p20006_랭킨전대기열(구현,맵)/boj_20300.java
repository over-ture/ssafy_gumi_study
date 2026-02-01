import java.io.*;

import java.util.*;


public class Main {

    static String ans = "";

    static BufferedReader br;
    static BufferedWriter bw;
    static StringBuilder sb;
    static StringTokenizer st;


    public static void main(String args[]) throws Exception
    {
        //300*300

        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter (new OutputStreamWriter (System.out));
        sb = new StringBuilder (new StringBuilder());

        st = new StringTokenizer(br.readLine());

        int n,m;
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        //LinkedHashMap은 기존 Hash맵과 달리 insert한 키값의 순서(넣은 순서를 보장) 반복문 수행 시 넣은 순서대로 순회

        //방관리 //키 : 방장의 이름 값: 방장이 관리하는 방(가변 길이 배열(닉네임으로 관리)
        HashMap < String, ArrayList<String> > map = new LinkedHashMap();
        //레벨 캐싱// 키: 닉네임 값: 레벨
        HashMap < String, Integer> players =  new LinkedHashMap();



        for(int i=0;i<n;++i)
        {
            String str = br.readLine();
            String[] info = str.split(" ");
            //현재 조사중인 멤버 파싱 후 캐싱
            players.put(info[1], Integer.parseInt(info[0]));

            //방을 만들어야 하는지 혹은 방에 참여할 수 있는지
            boolean canEnter=false;
            for( String key : map.keySet()) {

                //방의 인원 수 조건에 안맞으면 다음방 순회
                if( map.get(key).size() >= m )continue;
                //방장의 레벨 조건에 해당하지 않으면 다음방 순회
                if(!( 10>= Math.abs(players.get(key)- Integer.parseInt(info[0]))) )continue;

                canEnter = true;
                map.get(key).add(info[1]);
                break;
            }
            //방에 못들어가면 방을 판다.
            if(false ==canEnter)
            {
                map.put(info[1], new ArrayList<String>() );
                map.get(info[1]).add(info[1]);
            }

        }
        for( String key : map.keySet()){

            int size=map.get(key).size();
            if(m==size)
                System.out.print("Started!\n");
            else
                System.out.print("Waiting!\n");
            Collections.sort(map.get(key));
            for(int i=0 ;i<map.get(key).size();++i) {
                System.out.print(players.get(map.get(key).get(i)) );
                System.out.print(" ");
                System.out.print(map.get(key).get(i));
                System.out.print("\n");
            }

        }





        br.close();

    }
}