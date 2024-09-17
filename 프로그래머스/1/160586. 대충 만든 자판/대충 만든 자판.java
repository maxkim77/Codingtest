import java.util.*;
class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        Map<Character, Integer> minPressCount = new HashMap<>();
        for(String key:keymap){
            for(int j=0;j<key.length();j++){
                char ch = key.charAt(j);
                minPressCount.put(ch, Math.min(minPressCount.getOrDefault(ch,Integer.MAX_VALUE),j+1));
            }
        }
        int[] result = new int[targets.length];
        
        for(int i=0;i<targets.length;i++){
            String target = targets[i];
            int pressCount = 0;
            
            for(char ch:target.toCharArray()){
                if(!minPressCount.containsKey(ch)){
                    pressCount=-1;
                    break;
                }
                pressCount+= minPressCount.get(ch);
            }
            result[i] = pressCount;
        }
        return result;
    }
}