import java.util.*;

class Solution {
    public int solution(int n, String control) {
        Map<Character, Integer> controls = Map.of(
            'w', 1,
            's', -1,
            'd', 10,
            'a', -10
        );
        
        int answer = n;
        for (char ch: control.toCharArray()) {
            answer += controls.get(ch); 
        }
        return answer;
    }
}