class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        double sum=0;
        int cnt=0;
        for(int i = 0; i<numbers.length;i++){
            sum += numbers[i];
            cnt++;
        }
        answer = sum/cnt;
        return answer;
    }
}