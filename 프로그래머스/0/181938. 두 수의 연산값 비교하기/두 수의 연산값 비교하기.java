class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        // a + b 두정수를 붙여서 숫자로 만들기 - a
        String case1 = a + "" + b;
        // 2 * a * b 연산하기 - b
        int case2 = 2 * a * b;
        // 두 케이스 비교 후 그대로 출력
        if (Integer.parseInt(case1)> case2) {
            answer = Integer.parseInt(case1);
        }
        else{
            answer = case2;
        }
        return answer;
    }
}