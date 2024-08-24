import java.util.*;
class Solution {
    public int solution(int[] arr) {
        int count = 0;
        int[] beforeArr = arr.clone();
        
        // arr 가 주어짐 
        // 각 원소에 대해서 값이 50보다 크거나 같은 짝수라면 2로 나누고
        // 50보다 작은 홀수라면 2곱하고 다시 1을 더함
        while (true) {
            int[] change = beforeArr.clone();
            for(int i=0; i< beforeArr.length; i++){
                if(beforeArr[i]%2==0&&beforeArr[i]>=50){
                    change[i]=beforeArr[i]/2;
                }else if(beforeArr[i] %2!=0 && beforeArr[i]<50){
                    change[i]=beforeArr[i]*2+1;
                }
            }
            if(Arrays.equals(beforeArr, change)){
                break;
            } 
            count++;
            beforeArr= change;
        }
        
        return count;
    }
}
