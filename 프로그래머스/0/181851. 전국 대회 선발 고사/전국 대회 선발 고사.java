import java.util.*;

class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        Map<Integer, Integer> ranks = new HashMap<>();
        for (int i = 0; i < rank.length; i++) {
            ranks.put(rank[i], i);
        }
        
        int[] result = new int[3];
        int idx = 0;

        for (int i = 1; i < rank.length + 1; i++) {
            if (idx >= 3) {
                break;
            }
            if (attendance[ranks.get(i)]) {
                result[idx++] = ranks.get(i);
            }
        }
        
        return 10000 * result[0] + 100 * result[1] + result[2];
    }
}