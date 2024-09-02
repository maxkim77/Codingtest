class Solution {
    public int solution(String my_string) {
        String token[] = my_string.split(" ");
        int answer = Integer.parseInt(token[0]);
        for(int i=1;i<token.length;i+=2){
            String operator = token[i];
            int nextNumber = Integer.parseInt(token[i+1]);
        
        if(operator.equals("+")){
            answer += nextNumber;
        }else if(operator.equals("-")){
            answer -= nextNumber;
        }
        }
        return answer;
    }
}