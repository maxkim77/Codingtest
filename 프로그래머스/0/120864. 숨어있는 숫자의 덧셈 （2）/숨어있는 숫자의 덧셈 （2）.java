class Solution {
    public int solution(String my_string) {
        int answer = 0;
        String[] string = my_string.split("[a-zA-Z]");
        for(String i:string){
            if(!i.isEmpty()){
                answer+=Integer.parseInt(i);
            }
        }
        return answer;
    }
}