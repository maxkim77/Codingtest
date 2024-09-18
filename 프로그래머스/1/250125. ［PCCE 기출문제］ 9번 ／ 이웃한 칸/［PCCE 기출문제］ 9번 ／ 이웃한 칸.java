class Solution {
    public int solution(String[][] board, int h, int w) {
        int answer = 0;
        //1. make variable n and store length of board in it
        int n = board.length;
        //2. make variable count for storing the numbers of the colored section.
        int count =0;
        //3. create integer lists dh, dw for storing the change of h and w
        int[] dh = {0,1,-1,0};
        int[] dw = {1,0,0,-1};
        String color = board[h][w];
        //4. using loof
        for(int i=0;i<=3;i++){
            int h_check = h+dh[i];
            int w_check = w+dw[i];
            if(h_check>=0 && h_check<n && w_check>=0 && w_check<n){
                if(board[h_check][w_check].equals(color)){
                    count++;
                }
            }
        }
        return count;
    }
}