class Solution {
    public String solution(String code) {
        String answer = "";
        int mode = 0;
        // code[idx] 1이면 0으로 바꿈
        for(int idx=0;idx<code.length();idx++){
            char currentChar=code.charAt(idx);
            if (currentChar=='1') mode= 1-mode;
            else if (idx%2==mode) answer += currentChar;
        
        }
        // 그게 아니라면 code[idx]가 1이 아니면 idx 가 짝수일 때 ret 추가
        // 그게 아니라면 code[idx]가 1이아니면 idx가 짝수일때 ret 추가
        return "".equals(answer) ? "EMPTY" : answer;
    }
}