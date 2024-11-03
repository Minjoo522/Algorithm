import java.util.*;

class Solution {
    private List<List<Integer>> graph = new ArrayList<>();
    
    public int solution(int n, int[][] edge) {
        for (int i = 0; i <= n; i++) { // 이차원리스트 초기화
            graph.add(new ArrayList<>());
        }
        
        for (int[] e : edge) { // 인접 리스트 만들기
            int v = e[0];
            int w = e[1];
            graph.get(v).add(w);
            graph.get(w).add(v);
        }
        
        boolean[] visited = new boolean[n + 1];
        return bfs(n, visited);
    }
    
    private int bfs(int n, boolean[] visited) {
        Queue<int[]> q = new LinkedList<>();
        int answer = 0;
        
        q.add(new int[]{1, 0});
        visited[1] = true;
        int maxDepth = 0;
        
        while (!q.isEmpty()) {
            int[] current = q.poll();
            int v = current[0];
            int depth = current[1];
            
            if (maxDepth == depth) answer++;
            if (maxDepth < depth) {
                maxDepth = depth;
                answer = 1;
            }
            
            for (int i = 0; i < graph.get(v).size(); i++) {
                int w = graph.get(v).get(i); // 인접 정점
                if (!visited[w]) {
                    q.add(new int[]{w, depth + 1});
                    visited[w] = true;
                }
            }
        }
        
        return answer;
    }
}