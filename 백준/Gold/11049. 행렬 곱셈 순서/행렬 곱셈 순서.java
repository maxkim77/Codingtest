import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine().trim());

        int[] r = new int[N + 1]; // 행
        int[] c = new int[N + 1]; // 열

        for (int i = 1; i <= N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            r[i] = Integer.parseInt(st.nextToken());
            c[i] = Integer.parseInt(st.nextToken());
        }

        // dp[s][e]: s~e번째 행렬을 곱하는 최소 곱셈 연산 수
        int[][] dp = new int[N + 1][N + 1];

        // 구간 길이 len = 2..N
        for (int len = 2; len <= N; len++) {
            for (int s = 1; s + len - 1 <= N; s++) {
                int e = s + len - 1;
                int best = Integer.MAX_VALUE;

                for (int k = s; k < e; k++) {
                    // (s..k) 와 (k+1..e) 를 곱할 때 드는 추가 비용: r[s] * c[k] * c[e]
                    long cost = (long) dp[s][k] + dp[k + 1][e] + (long) r[s] * c[k] * c[e];
                    if (cost < best) best = (int) cost; // 문제 보장 범위 내
                }
                dp[s][e] = best;
            }
        }

        System.out.println(dp[1][N]);
    }
}
