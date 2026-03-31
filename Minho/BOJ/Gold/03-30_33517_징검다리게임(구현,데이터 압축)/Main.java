import java.util.*;
import java.io.*;
// 조합으로 풀자 
//7개 

//25c7
public class Main {

	static int[] dr = { 0, 0, 1, -1 };
	static int[] dc = { 1, -1, 0, 0 };
	static int n;
	static int m;
	static int SIZE = 25;
	static int map[][];
	static int ans = 0;
	static int[] combs = new int[7];
	
	static void comb(int lv, int start, int som) {

		if (lv >= 7) {
			if (som < 4)
				return;
			//연결성 체크
			if(isConnected())++ans;
			
			return ;
		}

		for (int i = start; i < SIZE; ++i) {

			combs[lv] = i;
			int somUp = som;
			if (map[i / 5][i % 5] == 'S')
				somUp += 1;
			comb(lv + 1, i + 1, somUp);
		}
	}
	static boolean isConnected() {
        Queue<Integer> q = new LinkedList<>();
        boolean[] visited = new boolean[7];
        
        q.add(combs[0]);
        visited[0] = true;
        int count = 1; 

        while (!q.isEmpty()) {
            int curr = q.poll();
            int r = curr / 5;
            int c = curr % 5;

            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];

                if (nr < 0 || nc < 0 || nr >= 5 || nc >= 5) continue;

                for (int i = 0; i < 7; i++) {
                    if (!visited[i] && combs[i] == (nr * 5 + nc)) {
                        visited[i] = true;
                        q.add(combs[i]);
                        count++;
                    }
                }
            }
        }

        return count == 7;
    }
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		map = new int[5][5];
		for (int i = 0; i < 5; ++i) {
			String line = br.readLine();
			for (int j = 0; j < 5; ++j) {
				map[i][j] = line.charAt(j);
			}
		}
		comb(0, 0, 0);

		System.out.print(ans);
	}
}