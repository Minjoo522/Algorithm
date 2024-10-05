class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        
        for (int i = 0; i < queries.length; i++) {
            int min = Integer.MAX_VALUE;
            int s = queries[i][0], e = queries[i][1], k = queries[i][2];
            
            for (int j = s; j <= e; j++) {
                if (arr[j] > k) {
                    min = Math.min(arr[j], min);
                }
            }
            answer[i] = min == Integer.MAX_VALUE ? -1 : min;
        }
        return answer;
    }
}