import java.util.*;

class Solution {
    public int solution(int[] nums) {
        Set<Integer> uniquePokemons = new HashSet<>();
        for (int num: nums) {
            uniquePokemons.add(num);
        }
        int maxSelectable = nums.length / 2;
        return Math.min(uniquePokemons.size(), maxSelectable);
    }
}