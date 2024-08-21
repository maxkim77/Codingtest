import java.util.*;
class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        int[] answer;
        int a=slicer[0];
        int b=slicer[1];
        int c=slicer[2];
        if (n==1){
            answer=Arrays.copyOfRange(num_list,0,b+1);
        }else if(n==2){
            answer=Arrays.copyOfRange(num_list,a,num_list.length);
        }else if(n==3){
            answer=Arrays.copyOfRange(num_list,a,b+1);
        }else{
            List<Integer> tempList=new ArrayList<>();
            for(int i=a;i<=b;i+=c){
                tempList.add(num_list[i]);
            }
            answer=tempList.stream().mapToInt(i->i).toArray();
        }
        return answer;
    }
}