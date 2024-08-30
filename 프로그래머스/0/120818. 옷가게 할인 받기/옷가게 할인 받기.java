// 코드는 위에서 아래로 움직이니깐 높은 값부터 비교해야함
class Solution {
    public int solution(int price) {
        double answer = 0;
        if(price>=500000)       {answer= price*0.80;}
        else if(price>=300000)  {answer= price*0.90;}
        else if(price>=100000)  {answer=price*0.95;}
        else                    {answer=price;}
        return (int) answer;
    }
}