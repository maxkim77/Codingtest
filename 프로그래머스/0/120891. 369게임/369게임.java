class Solution {
    public int solution(int order) {
        int answer = 0;
        int len = (int) Math.log10(order)+1;
        int game[] = new int[len];
        for(int i=0;i<len;i++){
            game[i]=order%10;
            if(game[i]==3 || game[i] ==6 || game[i]==9){
                answer++;
            }
            order = order/10;
        }
        
        return answer;
    }
}