class Solution {
    public int solution(int n) {
        int answer = 1;
        int slicesPerPizza=6;
        while((slicesPerPizza*answer)%n!=0){
            answer++;
        }
        return answer;
    }
}