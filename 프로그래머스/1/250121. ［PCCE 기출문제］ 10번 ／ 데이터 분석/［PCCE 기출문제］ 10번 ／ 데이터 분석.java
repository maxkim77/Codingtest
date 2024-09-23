import java.util.*;
class Solution {
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        ArrayList<int[]> answer = new ArrayList<>();
        HashMap<String,Integer> colIdx = new HashMap<>();
        
        colIdx.put("code",0);
        colIdx.put("date",1);
        colIdx.put("maximum",2);
        colIdx.put("remain",3);
        for(int i=0;i<data.length;i++){
            if(data[i][colIdx.get(ext)]<val_ext){
                answer.add(data[i]);
            }
        }
        answer.sort(Comparator.comparingInt(a->a[colIdx.get(sort_by)]));
        
        return answer.toArray(new int[answer.size()][]);
    }
}