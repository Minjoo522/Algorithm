import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        List<Integer> result = new ArrayList<>();
        List<Integer> deleteList = new ArrayList<>();
        for (int i = 0; i < delete_list.length; i++) {
            deleteList.add(delete_list[i]);
        }
        
        for (int i = 0; i < arr.length; i++) {
            if (!deleteList.contains(arr[i])) {
                result.add(arr[i]);
            }
        }
        return result.stream().mapToInt(it -> it).toArray();
    }
}