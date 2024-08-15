import java.util.*;
class Solution {
    public ArrayList<Integer> solution(int n) {
        ArrayList<Integer> answer = new ArrayList<>();
        answer.add(n);
        while(n!=1){
        if(n%2==0){
            n=n/2;
            answer.add(n);
        }else if(n%2!=0){
            n=3*n+1;
            answer.add(n);
        }else if(n==1){
            answer.add(n);
            break;
        }
        }
        return answer;
    }
}