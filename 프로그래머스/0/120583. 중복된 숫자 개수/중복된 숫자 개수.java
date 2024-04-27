class Solution {
    public int solution(int[] array, int n) {
        int answer = 0; // n의 개수를 세기 위한 변수 초기화
        for (int num : array) { // 배열 array의 각 원소에 대해
            if (num == n) { // 해당 원소가 n과 같으면
                answer++; // answer 값을 1 증가
            }
        }
        return answer; // n의 개수를 반환
    }
}
