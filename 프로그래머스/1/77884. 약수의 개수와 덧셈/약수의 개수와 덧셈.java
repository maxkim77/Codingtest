class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        // left~right 약수의 개수가 짝수인 것은 더하고
        // 홀수인 약수는 뺀다.
        for(int i=left;i<=right;i++){
            int divisorCount = 0;
            for(int j=1;j<=i;j++){
                if(i%j==0){
                    divisorCount++;
                }
            }
            if(divisorCount % 2==0){
                answer += i;
            } else {
                answer -= i;
            }
        }

        // 약수이면 count 를 올린다. 
        return answer;
    }
}