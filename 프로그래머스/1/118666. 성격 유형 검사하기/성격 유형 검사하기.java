import java.util.*;

class Solution {
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        
        // 성격 유형 배열
        char[] mbti_type = {'R','T','C','F','J','M','A','N'};
        
        // 성격 유형 점수를 저장할 해시맵
        HashMap<Character, Integer> mbti = new HashMap<>();
        
        // 초기화
        for(char c : mbti_type){
            mbti.put(c, 0);
        }
        
        // 점수 계산
        for(int i = 0; i < survey.length; i++){
            char[] c = survey[i].toCharArray();
            if(choices[i] > 4){ // 동의 선택
                int currentValue = mbti.get(c[1]);
                mbti.put(c[1], currentValue + (choices[i] - 4));
            } else if(choices[i] < 4){ // 비동의 선택
                int[] value = {0, 3, 2, 1}; // 1, 2, 3번 선택지 점수
                int currentValue = mbti.get(c[0]);
                mbti.put(c[0], currentValue + value[choices[i]]);
            }
        }
      
        // 성격 유형 결정
        for(int i = 0; i < mbti_type.length; i += 2){
            if(mbti.get(mbti_type[i]) > mbti.get(mbti_type[i + 1])){
                answer += mbti_type[i];
            } else if(mbti.get(mbti_type[i]) < mbti.get(mbti_type[i + 1])){
                answer += mbti_type[i + 1];
            } else {
                answer += mbti_type[i]; // 점수가 같으면 사전순
            }
        }
        
        return answer;
    }
}
