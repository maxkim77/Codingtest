import java.util.*;
class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = {};
        // 알아볼수 없는 번호는 0
        // 알아볼 수 없는 번호가 일치한다면 최고점수 일치하지 않는다면 최저점수
        // lotos 반복문 winnum이 일치한
        int matchCount=0;
        int zeroCount=0;
        
        Set<Integer> winSet = new HashSet<>();
        for(int num:win_nums){
            winSet.add(num);
        }
        
        for(int num:lottos){
            if(num==0){
                zeroCount++;
            }else if(winSet.contains(num)){
                matchCount++;
            }
        }
        int maxRank=getRank(matchCount+zeroCount);
        int minRank=getRank(matchCount);
        return new int[]{maxRank,minRank};
    }
        private int getRank(int count){
            switch(count){
                case 6: return 1;
                case 5: return 2;
                case 4: return 3;
                case 3: return 4;
                case 2: return 5;
                default: return 6;
            }
        }
}