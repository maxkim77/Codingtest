class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int numerator = numer1*denom2 + numer2*denom1;
        int dominator = denom1 * denom2;
        int gcd = gcd(numerator,dominator);
        
        numerator /= gcd;
        dominator /= gcd;
        
         int[] answer = {numerator,dominator};
        return answer;
    }
        private int gcd(int a, int b){
            while(b!=0){
            int temp=b;
            b=a%b;
            a=temp;   
            }
            return a;  
    }
}