/*
100% 반영
뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포
각 배포마다 몇 개의 기능이 배포되는지
Last In First Out
스택에 거꾸로 넣어놓기? 

- 앞의 애가 100이 안되면 뒤 애들도 결국 못함
- 꺼내서 횟수 * speeds가 100을 넘으면 되는거네
*/
import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Stack<Integer> tasks = new Stack<>();
        for (int i = progresses.length - 1; i >= 0; i--) {
            tasks.push(i);
        }
        
        int days = 1;
        int cnt = 0;
        List<Integer> result = new ArrayList<>();
        while (!tasks.isEmpty()) {
            int currIdx = tasks.peek();
            if ((progresses[currIdx] + speeds[currIdx] * days) >= 100) {
                cnt++;
                tasks.pop();
                continue;
            }
            days++;
            if (cnt > 0) {
                result.add(cnt);
                cnt = 0;
            }
        }
        if (cnt > 0) {
            result.add(cnt);
        }
        return result.stream().mapToInt(i -> i).toArray();
    }
}