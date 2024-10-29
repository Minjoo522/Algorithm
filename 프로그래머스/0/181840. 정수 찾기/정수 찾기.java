import java.util.*;

class Solution {
    public int solution(int[] num_list, int n) {
        Arrays.sort(num_list);
        
        int low = 0;
        int high = num_list.length - 1;
        int mid;
        
        while (low <= high) {
            mid = (low + high) / 2;
            
            if (num_list[mid] == n) {
                return 1;
            } else if (num_list[mid] > n) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return 0;
    }
}