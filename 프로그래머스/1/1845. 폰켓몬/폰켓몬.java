import java.util.*;
class Solution {
    public int solution(int[] nums) {
        int max=nums.length/2;
        HashSet<Integer> hashSet = new HashSet<>();
        for(int n:nums){
            hashSet.add(n);
        }
        if(max>=hashSet.size()){
            return hashSet.size();
        } else{
        return max;
    
        }
    }
}