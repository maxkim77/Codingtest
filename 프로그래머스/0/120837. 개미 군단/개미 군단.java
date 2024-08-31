class Solution {
    public int solution(int hp) {
        int answer = 0;
        int cnt=0;
        // 1. 공격력이 높은 개미 부터 나누어 나머지를 구한다
        // 2. 나머지에서 1 반복
        int general = 5;
        int soldier = 3;
        int worker = 1;
        
        cnt+=hp/general;
        hp=hp%general;
        cnt+=hp/soldier;
        hp=hp%soldier;
        cnt+=hp/worker;
        
        answer=cnt;
        
        return answer;
    }
}