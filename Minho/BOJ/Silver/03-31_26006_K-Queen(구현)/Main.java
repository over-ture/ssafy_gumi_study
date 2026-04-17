import java.util.*;
import java.io.*;


//25c7
public class Main {


	static int[] dr = {0, -1,-1,0,1,1,1,0,-1};
	static int[] dc = {0, 0,1,1,1,0,-1,-1,-1};
	static boolean[] blocked = new boolean[9];
	static int n;
	static int k;
	static boolean check = false;
	static boolean checkMate = false;
	static boolean staleMate =false; 
	static int[] king =new int[2];
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		king[0] = Integer.parseInt(st.nextToken())-1;
		king[1] = Integer.parseInt(st.nextToken())-1;
		
		//queens
		int center =0;
		int around = 0;
		
		for(int i = 0 ; i<k;++i ) {
			st = new StringTokenizer(br.readLine());
			int r= Integer.parseInt(st.nextToken())-1;
			int c = Integer.parseInt(st.nextToken())-1;

			for(int d =0;d<9;++d) {
				if(blocked[d]==true)continue;
				
				int nr = king[0] +dr[d];
				int nc = king[1] +dc[d];
				if( nr < 0  || nr>=n  || nc<0 || nc>=n) {
					blocked[d]=true;
					around++;
					continue;
				}
				
				if( nr == r ||
				    nc == c ||
				   (c - r == nc - nr )||
				   (r + c == nr + nc)) {
					if( d==0)
						center++;
					else around++;
					blocked[d]=true;
				}
			}
			
		
		}
		
		
		
		String ans ="";
		
		if(center ==1 && around !=8 )ans ="CHECK";
		else if(center ==1 && around ==8 )ans ="CHECKMATE";
		else if(center ==0 && around ==8 )ans ="STALEMATE";
		else ans ="NONE";
		
		System.out.print(ans);
	}
}