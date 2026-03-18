import java.util.*;
import java.io.*;
public class Main {

    static int numNums;
    static int[] nums;

    static int numOpers;
    static int[] opers =new int[4];
    static int[] askiiMap= new int[128];

    static int max = Integer.MIN_VALUE;
    static int min = Integer.MAX_VALUE;
    static public void DoDFS(int lv,int ret) {
        if(lv >= numOpers) {
            min = Math.min(min, ret);
            max = Math.max(max, ret);
            return ;
        }

        for(int i = 0 ; i< 4;++i) {
            if(opers[i]==0) continue ;
            --opers[i];
            int newRet = ret;
            switch(i) {
                case 0: newRet  += nums[lv+1];break;
                case 1: newRet  -= nums[lv+1];break;
                case 2: newRet  *= nums[lv+1];break;
                case 3: newRet  /= nums[lv+1];break;
            }
            DoDFS(lv+1,newRet);
            ++opers[i];
        }

    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder sb = new StringBuilder();
        StringTokenizer st ;
        numNums = Integer.parseInt(br.readLine());
        nums = new int[numNums];
        st = new StringTokenizer(br.readLine());
        for(int i = 0 ;i< numNums ;++i) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for(int i = 0 ;i< 4;++i) {
            opers[i]= Integer.parseInt(st.nextToken());
            numOpers+=opers[i];
        }

        DoDFS(0,nums[0]);
        System.out.print(max +"\n"+ min+"\n");



    }

}
