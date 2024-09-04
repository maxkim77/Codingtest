import java.util.*;
class Solution {
    public int solution(String[] spell, String[] dic) {
        int answer = 0;
        
        // spell 배열을 정렬해서 사용
        // spell 배열을 하나의 문자열로 합침
        // dic의 각 단어도 정렬하여 비교
        
        Arrays.sort(spell);
        String target = String.join("",spell);
        
        for(String word:dic){
            char[] wordArr = word.toCharArray();
            Arrays.sort(wordArr);
            String sortedWord = new String(wordArr);
            if(sortedWord.equals(target)){
                return 1;
            }
        }
        return 2;
    }
}