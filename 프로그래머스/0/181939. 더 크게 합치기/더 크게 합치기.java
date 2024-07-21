class Solution {
    public int solution(int a, int b) {
        String case1 = Integer.toString(a) + Integer.toString(b);
        String case2 = Integer.toString(b) + Integer.toString(a);
        
        int num1 = Integer.parseInt(case1);
        int num2 = Integer.parseInt(case2);
        
        int answer = Math.max(num1, num2);
        return answer;
    }
}