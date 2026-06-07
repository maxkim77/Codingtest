import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        HashMap<String, Integer> map = new HashMap<>();
        
        for (String[] cloth : clothes) {
            map.put(cloth[1], map.getOrDefault(cloth[1], 0) + 1);
        }
        int answer = 1;
        
        for (int count : map.values()) {
            answer *= (count + 1);
        }
        return answer - 1;
    }
}