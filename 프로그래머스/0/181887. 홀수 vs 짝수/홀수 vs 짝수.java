class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int odd_num =0;
        int even_num = 0;
        int i = 0;
        while(i<num_list.length){
            if(i%2==0){
                even_num += num_list[i];
            }else{
                odd_num +=num_list[i];
            }
            i++;
        }
        if(even_num>odd_num){
            answer=even_num;
        }else{
            answer=odd_num;
        }
        return answer;
    }
}