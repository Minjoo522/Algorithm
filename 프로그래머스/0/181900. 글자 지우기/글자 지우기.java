import java.util.*;
import java.lang.*;

class Solution {
    public String solution(String my_string, int[] indices) {
        Set<Integer> idxSet = new HashSet<>();
        for (int index: indices) {
            idxSet.add(index);
        }
        
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < my_string.length(); i++) {
            if (!idxSet.contains(i)) {
                result.append(my_string.charAt(i));
            }
        }
        
        return result.toString();
    }
}