import java.util.*;
class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        Arrays.fill(answer,-1);
        for(int idx=0; idx<queries.length;idx++){
            int s = queries[idx][0];
            int e = queries[idx][1];
            int k = queries[idx][2];
            int minGreaterValue = Integer.MAX_VALUE;
            for(int j=s;j<=e;j++){
                if(arr[j]>k && arr[j]<minGreaterValue){
                    minGreaterValue = arr[j];
                }
            }
            if(minGreaterValue != Integer.MAX_VALUE){
                answer[idx]=minGreaterValue;
            }
            
        }
        return answer;
    }
}