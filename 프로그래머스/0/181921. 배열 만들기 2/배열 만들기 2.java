import java.util.*;
class Solution {
    public int[] solution(int l, int r) {
        ArrayList<Integer> answer = new ArrayList<>();
        for(int i=l;i<=r;i++){
            if(String.valueOf(i).matches("[05]+")){
                answer.add(i);
            }
        }
        if(answer.isEmpty()){
            return new int[]{-1};
        }
        int[] answerArray=new int[answer.size()];
        for(int i=0;i<answer.size();i++){
            answerArray[i]=answer.get(i);
        }
        return answerArray;
    }
}