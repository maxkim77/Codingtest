class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        int idx =0;
        while ((idx=myString.indexOf(pat,idx))!=-1){
            idx+=1;
            answer++;
        }
        return answer;
    }
}