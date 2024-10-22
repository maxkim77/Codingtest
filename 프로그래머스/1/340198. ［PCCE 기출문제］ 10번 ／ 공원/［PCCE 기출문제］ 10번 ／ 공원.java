import java.util.*;

class Solution {
public int solution(int[] mats, String[][] park) {
int answer = -1;

    // 큰 돗자리부터 배치할 수 있도록 내림차순 정렬
    Arrays.sort(mats);
    for (int i = 0; i < mats.length / 2; i++) {
        int temp = mats[i];
        mats[i] = mats[mats.length - 1 - i];
        mats[mats.length - 1 - i] = temp;
    }

    // 큰 돗자리부터 검사
    for (int size : mats) {
        if (canPlace(size, park)) {
            return size;
        }
    }

    return answer;
}

// 주어진 크기의 돗자리를 배치할 수 있는지 검사하는 메서드
private boolean canPlace(int size, String[][] park) {
    int rows = park.length;
    int cols = park[0].length;

    // 가능한 모든 시작점을 순회
    for (int i = 0; i <= rows - size; i++) {
        for (int j = 0; j <= cols - size; j++) {
            if (isValidSpot(i, j, size, park)) {
                return true;
            }
        }
    }
    return false;
}

// 특정 위치에 주어진 크기의 돗자리를 배치할 수 있는지 확인
private boolean isValidSpot(int row, int col, int size, String[][] park) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            if (!park[row + i][col + j].equals("-1")) {
                return false;
            }
        }
    }
    return true;
}


}