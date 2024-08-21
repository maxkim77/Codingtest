import java.util.*;
class Solution {
    public int[] solution(int[] arr) {
        // 2가 모두 포함된 가장 작은 연속된 부분배열
        // Arrays.asList(arr)
        // 먼저 2가 포함된 INDEX를 찾음
        // MIN INDEX == START 이고
        // MAX INDEX == END 임
        int min = 100000, max=0;
        for (int i=0;i<arr.length;i++){
            if(arr[i]==2){
                min=Math.min(min,i);
                max=Math.max(max,i);
            }
        }
        if(min<=max){
            return Arrays.copyOfRange(arr,min,max+1);
        }else{
            return new int[]{-1};
        }
    }
}