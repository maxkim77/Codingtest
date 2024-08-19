class Solution {
    public String solution(String my_string, int s, int e) {
        StringBuffer answer = new StringBuffer();
        StringBuffer sb = new StringBuffer(my_string);
        answer.append(sb.subSequence(0,s));
        answer.append(new StringBuffer(sb.subSequence(s,e+1)).reverse());
        answer.append(sb.subSequence(e+1,my_string.length()));
        return answer.toString();
    }
}