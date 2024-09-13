import java.util.HashMap;
class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        // 해쉬로 name yearning 할당
        HashMap<String, Integer> yearningMap = new HashMap<>();
        for(int i=0;i<name.length;i++){
            yearningMap.put(name[i],yearning[i]);
        }
        // photo에서 각 반복문을 더한뒤 해당값들을 더함
        int[] answer = new int[photo.length];
        for(int i=0;i<photo.length;i++){
        int score = 0;
            for(String person : photo[i]){
                if(yearningMap.containsKey(person)){
                    score+=yearningMap.get(person);
                }
            }
            answer[i]=score;
        }
        //해당 사진의 추억점수를 배열에 저장
        return answer;
    }
}