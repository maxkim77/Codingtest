import java.util.*;

class Solution {
    class Song implements Comparable<Song> {
        int id;
        int play;
        
        Song(int id, int play) {
            this.id = id;
            this.play = play;
        }
        
        @Override
        public int compareTo(Song o) {
            if (this.play == o.play) {
                return this.id - o.id;
            }
            return o.play - this.play;
        }
    }
    public int[] solution(String[] genres, int[] plays) {
        Map<String, Integer> totalMap = new HashMap<>();
        Map<String, List<Song>> songMap = new HashMap<>();
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < genres.length; i++) {
            String genre = genres[i];
            
            totalMap.put(genre, totalMap.getOrDefault(genre, 0 ) + plays[i]);
            songMap.putIfAbsent(genre, new ArrayList<>());
            songMap.get(genre).add(new Song(i, plays[i]));
        }
        List<String> genreList = new ArrayList<>(totalMap.keySet());
        
        genreList.sort((a,b) -> totalMap.get(b) - totalMap.get(a));
        
        for (String genre : genreList) {
            List<Song> songs = songMap.get(genre);
            Collections.sort(songs);
            
            for (int i = 0; i < Math.min(2, songs.size()); i++){
                result.add(songs.get(i).id);
            }
        }
        return result.stream().mapToInt(i->i).toArray();
    }
}