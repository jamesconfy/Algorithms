// import java.awt.Color;
import java.io.File;
import java.util.ArrayList;
import java.io.FileNotFoundException;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class myBinary {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File(args[0]);

        Scanner sc = new Scanner(file);
        List<Integer> integers = new ArrayList<>();
        while (sc.hasNext()) {
            if (sc.hasNextInt()) {
                integers.add(sc.nextInt());
            } else {
                sc.next();
            }
        }

        sc.close();
        Collections.sort(integers);
        System.out.println(rank(10, integers));
        System.out.println(integers);
    }

    // public static int rank(int key, int[] a) {
    //     int lo = 0;
    //     int hi = a.length - 1;
    //     while (lo <= hi) {
    //         int mid = lo + (hi - lo) / 2;
    //         if (key < a[mid]) {
    //             hi = mid - 1;
    //         } else if (key > a[mid]) {
    //             lo = mid + 1;
    //         } else {
    //             return mid;
    //         }
    //     }
    //     return -1;
    // }

    public static int rank(int key, List<Integer> integers) {
        return rank(key, integers, 0, integers.size() - 1);
    }

    public static int rank(int key, List<Integer> integers, int lo, int hi) {
        // Index of key in a[], if present, is not smaller than lo and not larger than hi.
        if (lo > hi)
            return -1;
        int mid = lo + (hi - lo) / 2;
        if (key < integers.get(mid))
            return rank(key, integers, lo, mid - 1);
        else if (key > integers.get(mid))
            return rank(key, integers, mid + 1, hi);
        else
            return mid;
    }
}
