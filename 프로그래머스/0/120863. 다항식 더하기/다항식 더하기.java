class Solution {     
    public String solution(String polynomial) {         
        int xNum = 0; 
        int num = 0;         
        for(String s : polynomial.split(" ")) {             
            if(s.contains("x")) {
                xNum += s.equals("x") ? 1 : Integer.parseInt(s.replaceAll("x", ""));
            } else if(!s.equals("+")) {
                num += Integer.parseInt(s);
            }
        }         
        return (xNum != 0 ? (xNum > 1 ? xNum + "x" : "x") : "") +
               (num != 0 ? (xNum != 0 ? " + " : "") + num : (xNum == 0 ? "0" : ""));
    } 
}
