// This program calculates the maximum number of people in any city after a series of operations that add people to ranges of cities.
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // Read N (number of cities) and K (number of operations)
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int k = sc.nextInt();
        
        // Difference array to store changes
        long[] diff = new long[n + 2];
        // Process updates
        for (int i = 0; i < k; i++) {
            int start = sc.nextInt();
            int end = sc.nextInt();
            long value = sc.nextLong();
            
            // Mark the start of the range
            diff[start] += value;
            // Mark the end of the range (one index past the end)
            if (end + 1 <= n) {
                diff[end + 1] -= value;
            }
        }
        // Sweep through the array to find the peak value
        long maxVal = 0;
        long currentSum = 0;
        for (int i = 1; i <= n; i++) {
            currentSum += diff[i];
            if (currentSum > maxVal) {
                maxVal = currentSum;
            }
        }
        
        System.out.println(maxVal);
        sc.close();
    }
}

//System.out.println('A'+1); output:66