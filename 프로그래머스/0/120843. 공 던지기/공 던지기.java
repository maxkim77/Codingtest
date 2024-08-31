class Solution {
    public int solution(int[] numbers, int k) {
        int answer = 0;
        answer = numbers[(k*2-2)%numbers.length];
        return answer;
    }
}