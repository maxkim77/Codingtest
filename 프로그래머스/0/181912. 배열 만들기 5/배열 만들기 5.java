import java.util.*;
class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        List<Integer> result = new ArrayList<>();
        
        for(String str:intStrs){
            int a = Integer.parseInt(str.substring(s,s+l));
            if(a>k){
                result.add(a);
            }
        }
        return result.stream().mapToInt(i->i).toArray();
    }
}