import java.util.*;

public class Main {
    static int N, M, K;
    static int[][] D;

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        K = sc.nextInt();

        D = new int[202][202];
        for (int i = 0; i <= 200; i++) {
            for (int j = 0; j <= i; j++) {
                if (j == 0 || j == i) {
                    D[i][j] = 1;
                } else {
                    D[i][j] = D[i - 1][j - 1] + D[i - 1][j];
                    if (D[i][j] > 1000000000) D[i][j] = 1000000001;
                }
            }
        }

        if (D[N + M][M] < K) {
            System.out.println("-1");
        } else {
            while (!(N == 0 && M == 0)) {
                // 경계 처리
                if (N == 0) {          // a가 더 이상 없으면 z만
                    System.out.print("z");
                    M--;
                    continue;
                }
                if (M == 0) {          // z가 더 이상 없으면 a만
                    System.out.print("a");
                    N--;
                    continue;
                }

                // 맨 앞에 'a'를 두는 경우의 수: C(N+M-1, M)
                if (D[N - 1 + M][M] >= K) {
                    System.out.print("a");
                    N--;
                } else {
                    System.out.print("z");
                    K = K - D[N - 1 + M][M];
                    M--;
                }
            }
        }
    }
}
