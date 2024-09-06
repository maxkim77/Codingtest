class Solution {
    public int solution(int[] numbers) {
        int answer = -1;
        int sum =0;
        int numberSum=0;
        for(int i=0;i<10;i++){
            sum+=i;
        }
        for(int i=0;i<numbers.length;i++){
            numberSum+=numbers[i];
        }
        answer = sum - numberSum;
        return answer;
    }
}