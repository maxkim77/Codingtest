import java.util.*;
class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        int[] paint = new int[n];
        
        Arrays.fill(paint,1);
        
        for(int i: section){
            paint[i-1] = 0;
        }
        
        int i = 0;
        while(i<n){
            if(paint[i]==0){
                answer++;
                i+=m;
            }else{
                i++;
            }
        }
        
        return answer;
    }
}