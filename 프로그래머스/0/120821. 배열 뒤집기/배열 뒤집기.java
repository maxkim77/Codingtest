class Solution {
    public int[] solution(int[] num_list) {
        int len=num_list.length;
        int[] answer = new int[len];
        for(int i=0;i<len;i++){
           answer[i]=num_list[len-1-i];
        }
        return answer;
    }
}
//num_list 자체에 하면 이미 할당된게 중복할당되기 때문에 새로운 배열 answer에 할당한다.