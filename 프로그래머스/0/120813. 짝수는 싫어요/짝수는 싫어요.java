import java.util.*;
class Solution {
    public ArrayList solution(int n) {
        ArrayList<Integer> answer = new ArrayList<>();
        for(int i=0;i<n+1;i++){
          if(i%2!=0) answer.add(i);   
        }
        return answer;
    }
}