class Solution {
    public int solution(int slice, int n) {
        // 필요한 최소 피자 판 수 계산
        int answer = (n + slice -1) / slice;
        return answer;
    }
}
// 16/4=4
