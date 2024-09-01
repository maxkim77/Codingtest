import java.util.*;
class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        Arrays.sort(array);
        for(int i = 1;i<array.length;i++){
            if(Math.abs(n-array[0])>Math.abs(n-array[i])){
                int temp = array[0];
                array[0]=array[i];
                array[i]= temp;
            }
        }
        answer = array[0];
        return answer;
    }
}