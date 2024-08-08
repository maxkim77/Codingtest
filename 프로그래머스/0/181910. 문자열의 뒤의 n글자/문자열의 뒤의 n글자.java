class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        int start = my_string.length() - n;
        answer = my_string.substring(start, my_string.length());
        return answer;
    }
}