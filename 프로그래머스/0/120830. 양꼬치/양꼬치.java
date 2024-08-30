class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        // n*12000+2000*(k-n/10);
        
        answer = n*12000+2000*(k-n/10);
        // 총 얼마를 지불하는지
        return answer;
    }
}