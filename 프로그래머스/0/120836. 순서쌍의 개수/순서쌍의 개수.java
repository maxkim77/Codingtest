class Solution {
    public int solution(int n) {
        int answer = 0;
        for(int i=1;i<=n/2+1;i++){
            for(int j=n/2+1;j>=1;j--){
                if(i*j==n){answer++;}
            }
        }
        return answer;
    }
}