import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Deque<Integer> bridge = new ArrayDeque<>(); 
        int currWeight = 0;
        int idx = 0;
        int cnt = 0;

        for (int i = 0; i < bridge_length; i++) {
            bridge.add(0);
        }
        
        while (idx < truck_weights.length) {
            cnt++;
            currWeight -= bridge.pollFirst();

            if (currWeight + truck_weights[idx] <= weight) {
                currWeight += truck_weights[idx];
                bridge.addLast(truck_weights[idx++]);
                continue;
            }
            bridge.addLast(0);
        }
        cnt += bridge_length; // 마지막 트럭이 다리를 건너는 시간
        return cnt;
    }
}