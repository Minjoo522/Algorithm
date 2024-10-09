import java.util.*;

class Solution {
    public String[] solution(String my_string) {
        List<String> result = new ArrayList<>();
        
        for (int i = 0; i < my_string.length(); i++) {
            result.add(my_string.substring(i));
        }
        
        Collections.sort(result);

        return result.stream().toArray(String[]::new);
    }
}