import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        long t = Long.parseLong(st.nextToken());

        int[] friends = new int[n + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < n + 1; i++) {
            friends[i] = Integer.parseInt(st.nextToken());
        }

        Map<Integer, Integer> visited = new HashMap<>();
        int currentIdx = 1;
        int steps = 0;

        while (steps < t) {
            if (visited.containsKey(currentIdx)) {
                int cycleStart = visited.get(currentIdx);
                int cycleLength = steps - cycleStart;

                long remainingSteps = (t - steps) % cycleLength;

                for (int i = 0; i < remainingSteps; i++) {
                    currentIdx = friends[currentIdx];
                }

                System.out.println(currentIdx);
                return;
            }

            visited.put(currentIdx, steps);
            currentIdx = friends[currentIdx];
            steps++;
        }

        System.out.println(currentIdx);
    }
}