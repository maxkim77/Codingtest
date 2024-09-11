import java.util.*;
class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        Map<Character,Integer> lastIndex = new HashMap<>();
        // 이미 있는 배열 설정
        // 그리고 이미 있는 배열에 있으면 
        // 해당 인덱스를 찾음 2번째 인덱스 위치와 첫번째 인덱스의 위치를 뺌
        for(int i=0;i<s.length();i++){
            char currentChar = s.charAt(i);
            if(lastIndex.containsKey(currentChar)){
                answer[i] = i - lastIndex.get(currentChar);
            } else {
                answer[i] = -1;
            }
            lastIndex.put(currentChar, i);
        }
        return answer;
    }
}