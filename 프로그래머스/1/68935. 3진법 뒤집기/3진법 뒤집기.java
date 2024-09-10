import java.util.*;
class Solution {
    public int solution(int n) {
        int answer = 0;
        int share=n;
        
        List<Integer> num = new ArrayList<>();
        while(share!=0){
            num.add(share%3);
            share=share/3;
        }
        int cnt = num.size()-1;
        for(int i:num) {
            answer += (int) (i*Math.pow(3,cnt--));
        }
        
        return answer;
    }
}