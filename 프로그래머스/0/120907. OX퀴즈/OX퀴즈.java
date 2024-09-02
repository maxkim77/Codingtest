class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];
        String[] s = new String[quiz.length];
        for(int i=0;i<quiz.length;i++){
            s=quiz[i].split(" ");
            if(s[1].equals("-")){
                if(Integer.parseInt(s[0])-Integer.parseInt(s[2])== Integer.parseInt(s[4])){
                    answer[i]="O";
                }else {
                    answer[i]="X";
                }
            }
            if(s[1].equals("+")){
                if(Integer.parseInt(s[0])+Integer.parseInt(s[2])== Integer.parseInt(s[4])){
                    answer[i]="O";
                }else{
                    answer[i]="X";
                }
            }
        }
        return answer;
    }
}