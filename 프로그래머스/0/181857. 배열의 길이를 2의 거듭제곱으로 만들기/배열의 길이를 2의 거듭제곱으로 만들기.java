import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        int length =1;
        while(length<arr.length){
            length *=2;
        }
        return Arrays.copyOf(arr,length);
    }
}