class Solution {
    public int solution(int n) {
        int answer = 0;
        int factorial = 1;
        int facnum = 1;
        while(n>=factorial){
            factorial=factorial*facnum;
            if(factorial==n){
                answer=facnum;
                break;
            }else if(factorial>n){
                answer=facnum-1;
                break;
            }else{
                facnum++;
            }
        }
        return answer;
    }
}