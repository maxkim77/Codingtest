import java.util.*;
class Solution {
    public ArrayList<Integer> solution(String my_string) {
        ArrayList<Integer> answer = new ArrayList<>();
        for(int i=0;i<my_string.length();i++){
            if(Character.isDigit(my_string.charAt(i))){
                answer.add(Character.getNumericValue(my_string.charAt(i)));
            }
        }
        Collections.sort(answer);
    
        
        
        return answer;
    }
}