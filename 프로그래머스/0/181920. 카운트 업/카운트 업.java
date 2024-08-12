import java.util.*;

class Solution {
    public List solution(int start_num, int end_num) {
        List<Integer> answer = new ArrayList<>();
        for(int i=start_num;i<end_num+1;i++){
            answer.add(i);
        }
        return answer;
    }
}