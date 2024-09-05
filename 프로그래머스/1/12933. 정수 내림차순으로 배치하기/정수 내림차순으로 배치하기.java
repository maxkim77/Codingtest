import java.util.*;

class Solution {
    public long solution(long n) {
        /*
        숫자를 문자열로 변환
        문자열을 char로 변환
        char배열을 정렬
        정렬된배열을 뒤집음
        문자열을 다시 long 타입의 숫자로변환
        */
        long answer = 0;
        String stringN=Long.toString(n);
        char[] charArray=stringN.toCharArray();
        Arrays.sort(charArray);
        StringBuilder sb= new StringBuilder(new String(charArray));
        sb.reverse();
        
        return Long.parseLong(sb.toString());
    }
}