import java.util.*;
import java.io.*;

public class Main {
	private static final int INF =  1000000  * 16 + 1;
	private static int N;
	private static int[][] W;
	private static int[][] d;
	public static void main(String[] args) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		N = Integer.parseInt(br.readLine().trim());
		W = new int[16][16];
		d = new int[16][1 << 16];
		for (int i = 0; i < N; i++)
		{
			st = new StringTokenizer(br.readLine().trim());
			for (int j = 0; j < N; j++)
			{
				W[i][j] = Integer.parseInt(st.nextToken());
			}
		}	
		System.out.println(tsp(0,1));
	}
	private static int tsp(int c, int v)
	{
		if (v == (1 << N) - 1) 
		{
			return W[c][0] == 0 ? INF : W[c][0];
		}
		if (d[c][v] != 0)
		{
			return d[c][v];
		}
		int min_val = INF;
		for (int i = 0; i < N; i++)
		{
			if ((v & (1 << i)) == 0 && W[c][i] !=0)
			{
				min_val = Math.min(min_val, tsp(i,(v | (1<<i))) + W[c][i]);
			}
		}
		d[c][v] = min_val;
		return d[c][v];
	}
}
