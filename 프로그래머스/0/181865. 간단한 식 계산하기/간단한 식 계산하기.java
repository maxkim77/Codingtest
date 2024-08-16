import java.util.*;
class Solution {
    public int solution(String binomial) {
        int answer = 0;
        String arr[]=binomial.split(" ");
        int num1=Integer.parseInt(arr[0]);
        int num2=Integer.parseInt(arr[2]);
        String opt=arr[1];
        if(opt.equals("+")){
            answer=num1+num2;
        }else if(opt.equals("-")){
            answer=num1-num2;
        }else if(opt.equals("*")){
            answer=num1*num2;
        }
        return answer;
    }
}