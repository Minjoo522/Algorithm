import java.util.*;
import java.util.*;

class Solution {
    public Set<Integer> perm = new HashSet<>();
    public boolean[] visited;
    
    public int solution(String numbers) {
        visited = new boolean[numbers.length()];
        int result = 0;
        
        for (int r = 1; r <= numbers.length(); r++) {
            permute(numbers, "", r);
        }
        
        for (Integer num: perm) {
            if (isPrime(num)) result += 1;
        }
        
        return result;
    }
    
    private void permute(String numbers, String current, int r) {
        if (current.length() == r) {
            perm.add(Integer.parseInt(current));
            return;
        }
        
        for (int i = 0; i < numbers.length(); i++) {
            if (!visited[i]) {
                visited[i] = true;
                permute(numbers, current + numbers.charAt(i), r);
                visited[i] = false;
            }
        }
    }
    
    private boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            if (n % i == 0) return false;
        }
        
        return true;
    }
}