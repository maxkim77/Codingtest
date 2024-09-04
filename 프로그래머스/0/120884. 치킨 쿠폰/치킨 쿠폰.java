class Solution {
    public int solution(int chicken) {
        int answer = 0;
        //처음 주문한 치킨만큼의 쿠폰 선언
                //while 문 copon(10장이상일때)
        // remain 값 계산
        //  copon에 remain 값 넣기
        int coupon = chicken;
        while(coupon>=10){
            int serviceChicken = coupon/10;
            answer+=serviceChicken;
            coupon = (coupon%10)+serviceChicken;
        }
        return answer;
    }
}