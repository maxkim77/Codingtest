class Solution {
    public int solution(int a, int b, int n) {
        int answer = 0;
          while(n>=a){
              int ncoke = (n/a) * b;
              answer += ncoke;
              n=n%a+ncoke;  
          }
         return answer;
    }
}