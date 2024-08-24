import java.util.*;
class Solution {
    public int[] solution(int[] arr) {
        ArrayList<Integer> stk = new ArrayList<>();
        
        int[] answer = {};
        for(int i=0;i<arr.length;i++){
            if(stk.size()==0) stk.add(arr[i]);
            else if(stk.get(stk.size()-1)==arr[i]) stk.remove(stk.size()-1);
            else if(stk.get(stk.size()-1)!=arr[i]) stk.add(arr[i]);
            
        }
        if(stk.size()==0) return new int[] {-1};
        return stk.stream().mapToInt(x->x).toArray();
    }
}