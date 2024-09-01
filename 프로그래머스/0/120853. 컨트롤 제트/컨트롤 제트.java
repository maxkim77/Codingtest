class Solution {
    public int solution(String s) {
        int answer = 0;
        String array[] = {};
        array = s.split(" ");
        for(int i=0;i<array.length;i++){
            if(array[i].equals("Z")){
                answer -= Integer.parseInt(array[i-1]);
                continue;
            }
            answer += Integer.parseInt(array[i]);
        }
        
        
        return answer;
    }
}