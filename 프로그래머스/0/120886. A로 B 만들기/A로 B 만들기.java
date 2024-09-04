import java.util.Arrays;
class Solution {
    public int solution(String before, String after) {
        int answer = 0;
        char[] beforeArr=before.toCharArray();
        char[] afterArr = after.toCharArray();
        Arrays.sort(beforeArr);
        Arrays.sort(afterArr);
        
        if(Arrays.equals(beforeArr, afterArr)){
            return 1;
        }else{
            return 0;
        }
    }
}