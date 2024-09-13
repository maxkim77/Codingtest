import java.util.Arrays;
import java.util.PriorityQueue;
class Solution {
    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];
        PriorityQueue<Integer> hall = new PriorityQueue<>();
        
        for(int i=0;i<score.length;i++){
            hall.offer(score[i]);
            if(hall.size()>k){
                hall.poll();
            }
            answer[i] = hall.peek();
        }
        return answer;
    }
}