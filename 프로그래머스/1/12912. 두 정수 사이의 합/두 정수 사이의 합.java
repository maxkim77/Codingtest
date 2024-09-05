class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        int max = Math.max(a,b);
        int min = Math.min(a,b);
        // 숫자 최솟값 최댓값찾기 min max
        // min부터 max 까지 더하기
        for(int i=min;i<max+1;i++){
            answer+=i;
        }
        return answer;
    }
}