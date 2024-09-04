import java.util.*;
class Solution {
    public int solution(int[] sides) {
        int answer = 0;

        Arrays.sort(sides);
        int bLen = sides[1];
        int sLen = sides[0];
        
        int maxLen = bLen+sLen-1;
        int minLen = bLen-sLen+1;
        
        answer= maxLen-minLen+1;
        
        return answer;
    }
}