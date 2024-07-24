class Solution {
    public int solution(int a, int b, int c) {
        int sum = a + b + c;
        if (a != b && b != c && c != a) {
            return sum;
        } else if ((a == b && b != c) || (a != b && b == c) || (a == c && b != c)) {
            return sum * (a * a + b * b + c * c);
        } else {
            return sum * (a * a + b * b + c * c) * (a * a * a + b * b * b + c * c * c);
        }
    }
}
