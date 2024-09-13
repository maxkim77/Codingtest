class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        // 2진법으로 변환 해서 배열저장
        for(int i=0;i<n;i++){
            String binaryString = Integer.toBinaryString(arr1[i]|arr2[i]);
            binaryString = String.format("%"+n+"s",binaryString);
            binaryString = binaryString.replace('1','#').replace('0',' ');
            answer[i] = binaryString;
        }
        // 각 배열의 요소 끼리 더해서 2는 1로 변환
        // 각요소들을 #으로 변환 출력
        return answer;
    }
}