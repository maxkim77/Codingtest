class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        int len = arr.length;
        int sum = 0;
        for(int i=0;i<len;i++){
           sum += arr[i];  
        }
        answer = (double) sum/len;
        return answer;
    }
}