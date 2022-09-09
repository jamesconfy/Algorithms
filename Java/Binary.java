// import java.util.Arrays;
import edu.princeton.cs.algs4.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class Binary {
    public static int rank(int key, List<Integer> a) {
        int lo = 0;
        int hi = a.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (key < a.get(mid))
                hi = mid - 1;
            else if (key > a.get(mid))
                lo = mid + 1;
            else
                return mid;

        }

        return -1;
    }

    public static void main(String[] args) throws FileNotFoundException {
        File file = new File(args[0]);

        Scanner sc = new Scanner(file);
        List<Integer> whitelist = new ArrayList<>();
        while (sc.hasNext()) {
            if (sc.hasNextInt()) {
                whitelist.add(sc.nextInt());
            } else {
                sc.next();
            }
        }

        //        scanner.close();
        sc.close();
        Collections.sort(whitelist);
        StdOut.println(whitelist);
        // while (!StdIn.isEmpty()) {
        //     int key = StdIn.readInt();
        //     if (rank(key, whitelist) == -1)
        //         StdOut.println(key);
        // }
        int result = rank(Integer.parseInt(args[1]), whitelist);
        StdOut.println(result);
    }
}
