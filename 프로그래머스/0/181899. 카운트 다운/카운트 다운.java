class Solution {
    public int[] solution(int start_num, int end_num) {
        int[] answer = new int[start_num-end_num+1];
        int index = 0;
        int i = start_num;
        while (i>=end_num) {
            answer[index++] = i;
            i--;
        }
        return answer;
    }
}

