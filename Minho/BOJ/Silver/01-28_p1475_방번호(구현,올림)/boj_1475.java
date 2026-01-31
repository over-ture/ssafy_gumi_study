import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

    static String ans = "";

    static BufferedReader br;
    static BufferedWriter bw;
    static StringBuilder sb;
    static int n=0;
    static int[] arr=new int [26];


    public static void main(String args[]) throws Exception
    {



        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter (new OutputStreamWriter (System.out));
        sb = new StringBuilder (new StringBuilder());

        int arr[] = new int[10];

        String line = br.readLine();

        //9와 6은 동일한 숫자로 취급하므로 필요한 번호의 빈도수를 셀 때 9는 6으로 취급한다.
        for(int i=0;i<line.length();++i)
        {
            if(line.charAt(i) == '9')
            {
                ++arr[6];
            }
            else {
                ++arr[line.charAt(i)-'0'];
            }
        }
        //올림 포인트 : (6,6),(6,6),(6,6)(6,x) 1세트에 6이 2개들어 가므로 상품의 최소 요구량은 2로 나눈 값을 올린 값과 같다.
        arr[6]= (arr[6] -1 +2)/2;
        int ans = 0 ;
        //최소 몇세트가 필요한지를 구하기위해  적어도 각 숫자의 요구량 중 가장 큰 값 만큼이 필요하다.
        for(int i  =0;i<9;++i) {
            ans=Math.max(arr[i], ans);
        }


        bw.write(ans +"\n");
        bw.flush();
        bw.close();
        br.close();

    }
}