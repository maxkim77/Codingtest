import java.util.*;
class Solution {
    public String[] solution(String myStr) {
        String[] answer = {};
        myStr = myStr.replace("a"," ");
        myStr = myStr.replace("b"," ");
        myStr = myStr.replace("c"," ");
        
        String[] temp = myStr.split(" ");
        ArrayList<String> list = new ArrayList<>();
        for (String str: temp){
            if(!str.isEmpty()){
                list.add(str);
            }
        }
        if (list.isEmpty()){
            return new String[]{"EMPTY"};
        }
        return list.toArray(new String[list.size()]);
    }
        
}