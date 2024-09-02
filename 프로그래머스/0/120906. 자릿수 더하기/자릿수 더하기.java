class Solution {
    public int solution(int n) {
        int answer = 0;
        int len = (int)Math.log10(n)+1;
        for(int i=0;i<len;i++){
            answer+=n%10;
            n/=10;
        }
        return answer;
    }
}