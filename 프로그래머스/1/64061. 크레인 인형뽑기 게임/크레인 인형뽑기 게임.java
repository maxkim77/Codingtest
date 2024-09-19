import java.util.*;
class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        Stack<Integer> stack = new Stack<>();
        stack.push(0);
        for(int move : moves){
            for(int j=0;j<board.length;j++){
                int doll = board[j][move-1];
                if(doll==0){
                    continue;
                }
                board[j][move-1]=0;
                if(stack.peek()==doll){
                    stack.pop();
                    answer+=2;
                }else{
                    stack.push(doll);
                }
                break;
                
            }
        }
        return answer;
    }
}