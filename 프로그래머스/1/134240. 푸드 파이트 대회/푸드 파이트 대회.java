class Solution {
    public String solution(int[] food) {
        String straight = "";
        String reverse = "";
        String answer = "";

        for(int i=1;i<food.length;i++){
            int count = food[i]/2;
            for(int j=0;j<count;j++){
                straight+=i;
            }    
        }
        for(int k=straight.length()-1;k>=0;k--){
            reverse += straight.charAt(k);
        }
        answer = straight + "0" + reverse;
        return answer;
    }
}