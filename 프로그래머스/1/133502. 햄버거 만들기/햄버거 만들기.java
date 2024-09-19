import java.util.*;

class Solution {
    public int solution(int[] ingredient) {
        int answer = 0;
        Stack<Integer> inStack = new Stack<>();
        for(int in:ingredient){
            inStack.push(in);
            if(inStack.size()>=4){
            int len =inStack.size();
            if(inStack.get(len-4)==1
               &&inStack.get(len-3)==2
               &&inStack.get(len-2)==3
              &&inStack.get(len-1)==1){
                answer++;
                inStack.pop();
                inStack.pop();
                inStack.pop();
                inStack.pop();
            }
            }
        }
        
        return answer;
    }
}