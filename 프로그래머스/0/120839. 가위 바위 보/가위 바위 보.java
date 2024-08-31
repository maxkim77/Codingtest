import java.util.HashMap;

class Solution {
    public String solution(String rsp) {
        String answer = "";
        HashMap<String,String> game= new HashMap<>();
        game.put("2","0");
        game.put("0","5");
        game.put("5","2");
        
        String[] splitRsp = rsp.split("");
        for(String s:splitRsp){
             answer += game.get(s);  
        }
        return answer;
    }
}