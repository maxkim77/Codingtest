import java.util.*;
class Solution {
    public String[] solution(String[] players, String[] callings) {
        HashMap<String, Integer> playerIndex = new HashMap<>();
        
        for(int i=0;i<players.length;i++){
            playerIndex.put(players[i],i);
        }
        
        for(String calling :callings){
            int idx = playerIndex.get(calling);
            if(idx>0){
                String temp = players[idx-1];
                players[idx-1] = players[idx];
                players[idx]=temp;
                
                playerIndex.put(players[idx],idx);
                playerIndex.put(players[idx-1],idx-1);
            }
        
        }
        
        
        
        return players;
    }
}