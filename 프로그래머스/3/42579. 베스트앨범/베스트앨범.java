import java.util.*;

class Solution {
    static class Song {
        int idx;
        int play;
        
        Song(int idx, int play) {
            this.idx = idx;
            this.play = play;
        }
    }
    
    public int[] solution(String[] genres, int[] plays) {
        Map<String, List<Song>> genresMap = new HashMap<>();
        Map<String, Integer> counts = new HashMap<>();
        
        for (int i = 0; i < genres.length; i++) {
            genresMap.putIfAbsent(genres[i], new ArrayList<>());
            genresMap.get(genres[i]).add(new Song(i, plays[i]));
            counts.put(genres[i], counts.getOrDefault(genres[i], 0) + plays[i]);
        }
        
        // 장르 정렬
        List<Map.Entry<String, Integer>> genreList = new ArrayList<>(counts.entrySet());
        genreList.sort((a, b) -> b.getValue().compareTo(a.getValue()));
        
        // 노래 두 곡씩
        
        List<Integer> result = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : genreList) {
            List<Song> songs = genresMap.get(entry.getKey());

            songs.sort((a, b) -> b.play - a.play);

            for (int j = 0; j < Math.min(2, songs.size()); j++) {
                result.add(songs.get(j).idx);
            }
        }
        
        return result.stream().mapToInt(i -> i).toArray();
    }
}