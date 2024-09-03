class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        int[] answer = {0,0};
        for(int i=0;i<keyinput.length;i++){
            switch(keyinput[i]){
                case "up": answer[1]++;
                    break;
                case "down": answer[1]--;
                    break;
                case "left": answer[0]--;
                    break;
                case "right": answer[0]++;
                    break;
            }
            if(Math.abs(answer[0])>board[0]/2){
                answer[0] +=(answer[0]>0) ? -1:1;
            }
            if(Math.abs(answer[1])>board[1]/2){
                answer[1] +=(answer[1]>0) ? -1:1;
            }
            
        }
        return answer;
    }
}