class Solution {
    public int solution(int[] wallet, int[] bill) {
        int answer = 0;
        int minbill = Math.min(bill[0],bill[1]);
        int maxbill = Math.max(bill[0],bill[1]);
        int minwallet = Math.min(wallet[0],wallet[1]);
        int maxwallet = Math.max(wallet[0],wallet[1]);
        while(minbill>minwallet||maxbill>maxwallet){
            if(bill[0]>bill[1]){
                bill[0]=bill[0]/2;
            }else{
                bill[1]=bill[1]/2;
            }
            minbill = Math.min(bill[0],bill[1]);
            maxbill = Math.max(bill[0],bill[1]);
            answer++;
        }
        return answer;
    }
}