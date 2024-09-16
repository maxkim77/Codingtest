class Solution {
    public int solution(String s) {
        int answer = 0;
        int count = 0;
        int i = 0;
        while(i<s.length()){
            char x = s.charAt(i);
            int xCount = 0;
            int otherCount = 0;
            while(i<s.length()){
                if(s.charAt(i)==x){
                    xCount++;
                }else{
                    otherCount++;
                }
                i++;
                if(xCount==otherCount){
                    break;
                }
            }
            count++;
        }
        return count;
    }
}