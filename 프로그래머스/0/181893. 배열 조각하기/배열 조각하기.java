class Solution {
    public int[] solution(int[] arr, int[] query) {
        int start = 0;
        int end = arr.length - 1;
        
        for (int i = 0; i < query.length; i++) {
            if (i % 2 == 0) {
                end = start + query[i];
            } else {
                start += query[i];
            }
        }

        int[] result = new int[end - start + 1];
        for (int i = start, j = 0; i <= end; i++, j++) {
            result[j] = arr[i];
        }
        return result;
    }
}