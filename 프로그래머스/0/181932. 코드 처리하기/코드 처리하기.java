import java.util.*;
import java.lang.StringBuffer;

class Solution {
    public String solution(String code) {
        StringBuffer sb = new StringBuffer();
        List<Integer> modes = List.of(0, 1);
        int currentMode = 0;
        
        for (int i = 0; i < code.length(); i++) {
            char ch = code.charAt(i);
            if (ch == '1') {
                currentMode = modes.get((currentMode + 1) % 2);
                continue;
            }
            if (currentMode == 0 && i % 2 == 0) {
                sb.append(ch);
                continue;
            }
            if (currentMode == 1 && i % 2 != 0) {
                sb.append(ch);
                continue;
            }
        }
        String answer = sb.toString();
        
        return answer.equals("") ? "EMPTY" : answer;
    }
}