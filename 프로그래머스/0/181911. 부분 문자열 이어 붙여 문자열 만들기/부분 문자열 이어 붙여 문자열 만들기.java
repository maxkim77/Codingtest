class Solution {
    public String solution(String[] my_strings, int[][] parts) {
        String answer = "";
        // mystring 반복문
        for(int i=0;i<my_strings.length;i++){
            int s = parts[i][0];
            int l = parts[i][1];
            answer += my_strings[i].substring(s,l+1);
        }
// 각 parts에서 요소 2개 변수에 저장
// 서브스트링으로 부분 문자열 추출
// 부분문자열 저장
        return answer;
    }
}