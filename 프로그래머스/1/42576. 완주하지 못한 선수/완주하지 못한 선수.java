import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String result = "";
        Map<String, Integer> participants = new HashMap<>();
        
        for (String p : participant) {
            participants.put(p, participants.getOrDefault(p, 0) + 1);
        }
        
        for (String c : completion) {
            participants.put(c, participants.get(c) - 1);
        }

        for (Map.Entry<String, Integer> entry : participants.entrySet()) {
            if (entry.getValue() > 0) {
                result = entry.getKey();
                break;
            }
        }
        return result;
    }
}