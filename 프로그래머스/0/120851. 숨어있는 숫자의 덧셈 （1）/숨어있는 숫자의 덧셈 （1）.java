class Solution {
    public int solution(String my_string) {
        int answer = 0;
        // 문자열 charAt으로 하나하나 isDigit확인하기 맞으면
        //answer에 더함
        for(int i=0;i<my_string.length();i++){
            if(Character.isDigit(my_string.charAt(i))){
                answer += Character.getNumericValue(my_string.charAt(i));
            }
        }
        
        return answer;
    }
}