import java.util.*;
class Solution {
    public int[] solution(String[] park, String[] routes) {
        //시작위치
        int startX=0;
        int startY=0;
        
        for(int i=0;i<park.length;i++){
            for(int j=0;j<park[i].length();j++){
                if(park[i].charAt(j)=='S'){
                    startX=i;
                    startY=j;
                    break;
                }
            }
        }
        
        //좌표
        int[] dx = {0,0,1,-1};
        int[] dy = {1,-1,0,0};
        
        //동서남북 위치 hashMap;
        HashMap<String, Integer> directionMap=new HashMap<>();
        
        directionMap.put("E",0);
        directionMap.put("W",1);
        directionMap.put("S",2);
        directionMap.put("N",3);
        
        //현재위치 좌표
        int x = startX;
        int y = startY;
        // 길찾기
        for(String route:routes){
            String[] parts =route.split(" ");
            String direction = parts[0];
            int distance = Integer.parseInt(parts[1]);
            int dirIndex = directionMap.get(direction);
            int newX = x;
            int newY = y;
            boolean canMove = true;
            
            for(int i=0;i<distance;i++){
                newX += dx[dirIndex];
                newY += dy[dirIndex];
                if(newX<0||newY<0||newX>=park.length||newY>=park[0].length() || park[newX].charAt(newY)=='X'){
                    canMove=false;
                    continue;
                }
            }
            if(canMove){
                x=newX;
                y=newY;
            }
            
        }
        return new int[]{x,y};
    }
}