class Solution {
    public int[] solution(int money) {
        int[] answer = {};
        int iceAme=5500;
        int cups = 0;
        int rem = 0;
        
        cups = (int) Math.floor((double)money/iceAme);
        rem = money % iceAme;
        
        answer = new int[]{cups,rem};
        
        return answer;
    }
}