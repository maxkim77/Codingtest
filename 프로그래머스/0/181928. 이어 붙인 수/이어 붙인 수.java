class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        String odd_num = "";
        String even_num = "";
        for(int i=0;i<num_list.length;i++){
            if(num_list[i]%2==1){
                odd_num+=Integer.toString(num_list[i]);
            }
            else{
                even_num+=Integer.toString(num_list[i]);
            }
        }
        answer=Integer.parseInt(odd_num)+Integer.parseInt(even_num);
        return answer;
    }
}