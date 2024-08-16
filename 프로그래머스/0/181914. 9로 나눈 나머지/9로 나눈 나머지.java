class Solution {
    public int solution(String number) {
        int answer = 0;
         String num[] = number.split("");
        for(String n:num){
            answer += Integer.parseInt(n);
        }
        answer= answer%9;
        return answer;
    }
}