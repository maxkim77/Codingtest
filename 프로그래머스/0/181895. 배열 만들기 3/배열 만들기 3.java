import java.util.*;
class Solution {
    public ArrayList<Integer> solution(int[] arr, int[][] intervals) {
        ArrayList<Integer> answer = new ArrayList<>();
        int sub1[]=Arrays.copyOfRange(arr,intervals[0][0],intervals[0][1]+1);
        for(int num1:sub1){
            answer.add(num1);
        }
        int sub2[]=Arrays.copyOfRange(arr,intervals[1][0],intervals[1][1]+1);
        for(int num2:sub2){
            answer.add(num2);
        }
        return answer;
    }
}