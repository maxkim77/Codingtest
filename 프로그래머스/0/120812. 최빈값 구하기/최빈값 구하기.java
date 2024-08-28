import java.util.*;

        // 최빈값 빈도수 구하기
        // 가장 빈도수 찾기
        // 최빈값 원소찾기
        // 최빈값이 여러개면 -1       

class Solution {
    public int solution(int[] array) {
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        int maxFrequency=0;
        int result=-1;
        for(int num:array){
            int frequency = frequencyMap.getOrDefault(num,0) +1;
            frequencyMap.put(num,frequency);
            if(frequency>maxFrequency){
                maxFrequency=frequency;
                result=num;
            }else if(frequency==maxFrequency&&result!=num){
                result=-1;
            }
        }
        return result;
    }
}