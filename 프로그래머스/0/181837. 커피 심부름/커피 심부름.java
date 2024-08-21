import java.util.*;
class Solution {
    public int solution(String[] order) {
        int answer = 0;
       List<String> ame = Arrays.asList("hotamericano", "americanohot", "iceamericano", "americanoice", "americano", "anything");
        List<String> latte = Arrays.asList("icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot");
        
        for(String item:order){
            if(ame.contains(item)){
                answer+=4500;
            }else{
                answer+=5000;
            }
        }
        return answer;
    }
}