class Solution {
    public String solution(String new_id) {
        String answer = "";
        String step1 = new_id.toLowerCase();
        
        char[] step1Arr=step1.toCharArray();
        
        StringBuilder step2 = new StringBuilder();
        
        for(char c: step1Arr){
            if((c>='a'&&c<='z') || (c>='0'&&c<='9') || c=='-' || c== '_' || c=='.'){
                step2.append(c);
            }
        }
        
        String step3 = step2.toString().replace("..",".");
        while(step3.contains("..")){
            step3=step3.replace("..",".");
        }
        
        String step4=step3;
        if(step4.length()>0){
            if(step4.charAt(0)=='.'){
                step4 = step4.substring(1,step4.length());
            }
            if(step4.length()>0){
                if(step4.charAt(step4.length()-1)=='.'){
                    step4=step4.substring(0,step4.length()-1);
                }
            }
        }    
        String step5= step4;
        if(step5.equals("")){
            step5="a";
        }
        
        String step6=step5;
        if(step6.length()>=16){
            step6 = step6.substring(0,15);
        }
        if(step6.charAt(step6.length()-1)=='.'){
            step6=step6.substring(0,step6.length()-1);
        }
        
        StringBuilder step7 = new StringBuilder(step6);
        
        if(step7.length()<=2){
            char last = step7.charAt(step7.length()-1);
            while(step7.length()<3){
                step7.append(last);
            }
        }
        
        answer = String.valueOf(step7);
            
            
        
        return answer;
    }
}