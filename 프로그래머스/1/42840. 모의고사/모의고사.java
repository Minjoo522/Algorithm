import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] first = {1, 2, 3, 4, 5};
        int[] second = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] third = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int[] scores = new int[3];
        
        for (int i = 0; i < answers.length; i++) {
            if (first[i % first.length] == answers[i]) scores[0]++;
            if (second[i % second.length] == answers[i]) scores[1]++;
            if (third[i % third.length] == answers[i]) scores[2]++;
        }
        
        int max = Math.max(scores[0], Math.max(scores[1], scores[2]));
        List<Integer> result = new ArrayList<>();
        
        for (int i = 0; i < 3; i++) {
            if (scores[i] == max) {
                result.add(i + 1);
            }
        }
        
        return result.stream().mapToInt(i -> i).toArray();
    }
}