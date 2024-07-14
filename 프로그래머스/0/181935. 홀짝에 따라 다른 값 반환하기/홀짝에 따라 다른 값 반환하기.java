// n 이 홀 수라면 n이하의 홀수 정수 합
// 7 = 1357 =16
// 10 = 246810
// 4 16 36 
// if 홀수 { 홀수의합 }
// else {짝수 양의 정수의 제곱}
class Solution {
    public int solution(int n) {
        int i = 0;
        int answer = 0;
        
        if (n % 2 == 1) {
            for (i=1; i<=n; i+=2){
                answer += i;
                }
        }
        else {
            for (i=2; i<=n; i+=2){
                answer += i*i;
            }
        }
        
        return answer;
    }
}