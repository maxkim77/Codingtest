class Solution {
    public int solution(long num) {
        int answer = 0;
        
        // 입력값이 1인 경우 즉시 0 반환
        if (num == 1) {
            return 0;
        }
        
        // 최대 500번 반복을 위한 루프
        while (num != 1) {
            // 짝수일 때
            if (num % 2 == 0) {
                num /= 2;
            }
            // 홀수일 때
            else {
                num = num * 3 + 1;
            }
            
            // 연산 횟수 증가
            answer++;
            
            // 500번 반복해도 1이 되지 않으면 -1 반환
            if (answer >= 500) {
                return -1;
            }
        }
        
        // 최종 결과 반환
        return answer;
    }
}
