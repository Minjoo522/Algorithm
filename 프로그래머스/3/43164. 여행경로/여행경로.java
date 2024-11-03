import java.util.*;

class Solution {
    private boolean[] visited;
    private List<String> result = new ArrayList<>();
    
    public String[] solution(String[][] tickets) {
        // 완전탐색(dfs) + 백트래킹 + 정렬
        visited = new boolean[tickets.length];
        
        dfs(0, "ICN", "ICN", tickets);
        Collections.sort(result);
        
        return result.get(0).split(" ");
    }
    
    private void dfs(int idx, String start, String route, String[][] tickets) {
        if (idx == tickets.length) {
            result.add(route);
            return;
        }
        
        for (int i = 0; i < tickets.length; i++) {
            if (tickets[i][0].equals(start) && !visited[i]) {
                visited[i] = true;
                dfs(idx + 1, tickets[i][1], route + " " + tickets[i][1], tickets);
                visited[i] = false;
            }
        }
    }
}