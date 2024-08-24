class Solution {
    public String solution(int q, int r, String code) {
        StringBuilder answer = new StringBuilder();
        // q, r code 
        for(int i=0;i<code.length();i++)
        {
            if(i%q==r){
                answer.append(code.charAt(i));
            }    
        }        
        return answer.toString();
    }
}