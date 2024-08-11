class Solution {
    public int solution(int n) {
        int count = 0;

        for(int i = 1; i <= n + count; i++) {
            if(i % 3 == 0 || String.valueOf(i).contains("3")) count++;
        }

        return n + count;
    }
}