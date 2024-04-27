class Solution {
    public int solution(int[] array, int height) {
        int answer = 0; // 머쓱이보다 키가 큰 사람의 수를 저장할 변수
        for (int h : array) { // 배열의 각 원소에 대해 반복
            if (h > height) { // 해당 원소의 키가 머쓱이의 키보다 클 경우
                answer++; // answer를 1 증가
            }
        }
        return answer; // 결과 반환
    }
}
