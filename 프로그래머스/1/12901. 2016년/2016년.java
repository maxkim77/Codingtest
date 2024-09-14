class Solution {
    public String solution(int a, int b) {
        //날짜의 요일을 담은 배열
        String[] day = {"FRI", "SAT", "SUN","MON","TUE","WED","THU"};
        int[] month = {31,29,31,30,31,30,31,31,30,31,30,31};
        int answer =0;
        for(int i=0;i<a-1;i++){
            answer+=month[i];
        }
        answer += b - 1;
        return day[answer%7];
    }
}