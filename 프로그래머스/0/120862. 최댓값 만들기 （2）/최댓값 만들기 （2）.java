import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        Arrays.sort(numbers);  // 배열을 오름차순으로 정렬합니다.
        int n = numbers.length;
        
        // 가장 작은 두 수의 곱과 가장 큰 두 수의 곱 중 더 큰 값을 반환합니다.
        return Math.max(numbers[0] * numbers[1], numbers[n - 1] * numbers[n - 2]);
    }
}
