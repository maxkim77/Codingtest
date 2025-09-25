import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] A;          // 입력 수열
    static int[] lisTail;    // 길이별 최소 끝값
    static int[] lisTailIdx; // 길이별 끝값이 위치한 A의 인덱스
    static int[] prev;       // 각 인덱스의 이전 인덱스(복원용)

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        // 입력
        N = Integer.parseInt(br.readLine().trim());
        A = new int[N];
        lisTail = new int[N];
        lisTailIdx = new int[N];
        prev = new int[N];
        Arrays.fill(prev, -1);

        // 수열 읽기 (여러 줄 입력 가능성 고려)
        StringTokenizer st = new StringTokenizer("");
        for (int i = 0; i < N; i++) {
            while (!st.hasMoreTokens()) {
                st = new StringTokenizer(br.readLine());
            }
            A[i] = Integer.parseInt(st.nextToken());
        }

        // LIS 알고리즘 (O(N log N))
        int length = 0; // LIS 길이
        for (int i = 0; i < N; i++) {
            int pos = lowerBound(lisTail, 0, length, A[i]); // A[i] 들어갈 위치
            lisTail[pos] = A[i];
            lisTailIdx[pos] = i;

            if (pos > 0) prev[i] = lisTailIdx[pos - 1]; // 바로 이전 원소 연결
            if (pos == length) length++;                // 길이 확장
        }

        // 수열 복원
        int[] sequence = new int[length];
        int idx = lisTailIdx[length - 1];
        for (int k = length - 1; k >= 0; k--) {
            sequence[k] = A[idx];
            idx = prev[idx];
        }

        // 출력
        sb.append(length).append('\n');
        for (int i = 0; i < length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(sequence[i]);
        }
        System.out.println(sb);
    }

    /**
     * lowerBound: 정렬된 배열 [from, to) 구간에서 key 이상이 처음 나오는 위치 반환
     */
    static int lowerBound(int[] arr, int from, int to, int key) {
        int l = from, r = to;
        while (l < r) {
            int m = (l + r) >>> 1;
            if (arr[m] < key) l = m + 1;
            else r = m;
        }
        return l;
    }
}
