class Solution {
    public String solution(int age) {
        String answer = "";
        int num=age;
        int length=(int) Math.log10(num)+1;
        int[] digits = new int[length];
        for(int i=length-1;i>=0;i--){
            digits[i]=num%10;
            num/=10;
        }
        for(int d:digits){
             answer = answer + (char) (d+97);
        }
        return answer;
    }
}