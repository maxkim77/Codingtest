import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        // 문자를 저장할 변수를 생성
        String answer = "";
        char c;
        
        // 반복문 생성
        for(int i=0;i<a.length();i++){
        // charAt 문자열에서 문자 하나만 가져오는 함수 
        c = a.charAt(i);
            if(Character.isUpperCase(c)){
                answer += Character.toLowerCase(c); 
            }
            else {
                answer += Character.toUpperCase(c);
            }
        // 문자열 비교 후 대소문 자 변환
        }
        
        // 출력
        System.out.println(answer);        
    }
}