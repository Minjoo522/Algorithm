import java.util.*;

class Solution {
    public int[] solution(int[] num_list) {
        int last = num_list[num_list.length - 1];
        int last_b = num_list[num_list.length - 2];
        
        int[] answer = new int[num_list.length + 1];
        for (int i = 0; i < num_list.length; i++) {
            answer[i] = num_list[i];
        }
        
        if (last > last_b) {
            answer[num_list.length] = last - last_b;
        } else {
            answer[num_list.length] = last * 2;
        }
        return answer;
    }
}