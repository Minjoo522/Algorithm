import java.util.*;
import java.lang.StringBuffer;

class Solution {
    public String solution(String code) {
        StringBuffer sb = new StringBuffer();
        int mode = 0;
        
        for (int i = 0; i < code.length(); i++) {
            char ch = code.charAt(i);
            if (ch == '1') {
                mode = mode == 0 ? 1 : 0;
                continue;
            }
            if (i % 2 == mode) {
                sb.append(ch);
            }
        }
        String answer = sb.toString();
        
        return answer.equals("") ? "EMPTY" : answer;
    }
}