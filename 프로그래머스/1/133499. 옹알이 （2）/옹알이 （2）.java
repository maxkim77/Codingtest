class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] babble = {"aya","ye","woo","ma"};
        for(String word : babbling){
            String temp = word;
            for(String b:babble){
                if(temp.contains(b+b)){
                    temp="invalid";
                    break;
                }
                temp=temp.replace(b, " ");
            }
            if(temp.trim().isEmpty()){
                answer++;
            }
        }
        return answer;
    }
}