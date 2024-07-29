import java.util.ArrayList;
import java.util.List;
class Solution {
    public List<Integer> solution(int[] num_list) {
        List<Integer> answer = new ArrayList<>();
        
        int last_num = num_list[num_list.length-1];
        int previous_num = num_list[num_list.length-2];
        for(int i=0;i<num_list.length; i++){
            answer.add(num_list[i]);
        }if(last_num>previous_num){
            answer.add(last_num-previous_num);
        }else{
            answer.add(last_num*2);
        } // 마지막원소에서 그전 원소를 뺀값
        // 마지막 원소가 더 작으면 마지막원소를 두배한 값을 추가해서 return 
        return answer;
    }
}