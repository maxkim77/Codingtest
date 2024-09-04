class Solution {
    public int solution(int chicken) {
        int answer = 0;
        int service = chicken/10;
        int sRemain = chicken%10;
        int coupon = (sRemain + service)/10;
        answer = service+ coupon;
        return answer;
    }
}