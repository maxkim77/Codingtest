import java.util.*;

class Solution {
    public ArrayList<Integer> solution(int[] arr) {
        ArrayList<Integer> answer = new ArrayList<>();
        for(int a: arr){
            for(int i=0;i<a;i++){
                 answer.add(a);     
            }
        }
        return answer;
    }
}