import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String doc = br.readLine();
        String word = br.readLine();

        int count = 0;
        int i = 0;

        while (i <= doc.length() - word.length()) {
            if (doc.startsWith(word, i)) {
                count++;
                i += word.length();
            } else {
                i++;
            }
        }

        System.out.println(count);
    }
}
