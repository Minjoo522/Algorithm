import java.util.*;

class Solution {
    public String solution(int[] numLog) {
        StringBuilder sb = new StringBuilder();
        Map<Integer, String> controls = Map.of(
            1, "w",
            -1, "s",
            10, "d",
            -10, "a"
        );
        
        for (int i = 1; i < numLog.length; i++) {
            sb.append(controls.get(numLog[i] - numLog[i - 1]));
        }
        return sb.toString();
    }
}