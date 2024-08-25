class Solution {
    public int[][] solution(int[][] arr) {
        int rows = arr.length;
        int cols = arr[0].length;
        int size = Math.max(rows,cols);
        // 행이 열보다많으면 열이 적은만큼 0을 채우고
        int[][] answer = new int[size][size];
        
        // 열이 행보다 많으면 행이 적은 만큼 0으로 채운다.
        for(int i=0;i<rows;i++){
            for(int j=0; j<cols;j++){
                answer[i][j]=arr[i][j];
            }
        }
        
        return answer;
    }
}