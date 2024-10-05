class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        for (int[] query: queries) {
            int first = arr[query[0]];
            int second = arr[query[1]];
            arr[query[0]] = second;
            arr[query[1]] = first;
        }
        return arr;
    }
}