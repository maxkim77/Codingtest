import java.util.*;

class Solution {
    public List solution(int[] arr, int k) {
        List<Integer> answer = new ArrayList<>();
        for (int i=0;i<arr.length;i++){
            if(answer.size()==k){
                break;
            }
            if(!answer.contains(arr[i])){
                answer.add(arr[i]);
            }
        }
        while(answer.size()<k){
            answer.add(-1);
        }
        return answer;
    }
}