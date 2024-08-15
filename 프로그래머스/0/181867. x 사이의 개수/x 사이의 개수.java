import java.util.*;
class Solution {
    public ArrayList<Integer> solution(String myString) {
        ArrayList<Integer> answer = new ArrayList<>();
        String[] newString = myString.split("x",-1);
        for(String s:newString){
            answer.add(s.length());
        }
        return answer;
    }
}