class Solution {
    public int solution(int num, int k) {
        int answer = 0;
        int len = (int) Math.log10(num)+1;
         int array[] = new int[len];
        for(int i=0;i<len;i++){
            array[len-i-1]=num%10;
            num /=10;
        }
        for(int j=0;j<len;j++){
            if(array[j]==k){
                answer= j+1;
                break;
            }else{
                answer=-1;
            }
        }
        return answer;
    }
}