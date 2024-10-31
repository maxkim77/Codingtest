import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String sNum = sc.next();

        char[] cNum = sNum.toCharArray();
        int sum=0;
        //N의 숫자를 입력받아 String sNum에 저장하기
        for(int i=0;i<N;i++){
            sum += cNum[i] - '0';
        }
        System.out.println(sum);
    }
}