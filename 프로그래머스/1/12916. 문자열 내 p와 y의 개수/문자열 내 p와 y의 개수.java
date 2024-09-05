class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int len = s.length();
        int p = 0;
        int y = 0;
        s=s.toLowerCase();
        for(int i=0;i<len;i++){
            if(s.charAt(i)=='p'){
                p++;
            }else if(s.charAt(i)=='y'){
                y++;
            }
        }
        if(p==y){
            answer =true;
        }else{
            answer =false;
        }
        return answer;
    }
}