import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        // 나누어 떨어지는 값을 저장할 리스트
        List<Integer> list = new ArrayList<>();
        
        // 배열을 순회하면서 나누어 떨어지는 값 찾기
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] % divisor == 0) {
                list.add(arr[i]);
            }
        }
        
        // 나누어 떨어지는 값이 없다면 -1 반환
        if (list.isEmpty()) {
            return new int[] {-1};
        }

        // 리스트를 배열로 변환하고 오름차순 정렬
        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        Arrays.sort(answer);
        
        return answer;
    }
}
