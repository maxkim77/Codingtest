class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = {};
        int even = 0;
        int odd = 0;
        for(int num:num_list){
            if(num%2==0){even++;}
            else        {odd++;}
        }
        answer = new int[]{even,odd};
        return answer;
    }
}