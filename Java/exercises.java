import java.util.Arrays;
import edu.princeton.cs.algs4.StdOut;

public class exercises {
    public static void main(String[] args) {
        int a = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);
        int c = Integer.parseInt(args[2]);
        StdOut.println(equal(a, b, c));

        double x = Double.parseDouble(args[3]);
        double y = Double.parseDouble(args[4]);
        StdOut.println(fragment(x, y));
        myprint();

        int[][] arr = { { 1, 2, 3, 4 }, { 5, 6, 7, 8 }, { 9, 10, 11, 12 } };
        StdOut.println(Arrays.deepToString(transpose(arr)));
        StdOut.println(lg(10000000));

        int[] arr1 = { 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 4, 5, 4, 3, 1, 2, 3, 0, 6, 1 };
        StdOut.println(arr1.length);
        StdOut.println(Arrays.toString(histogram(arr1, 10)));
        StdOut.println(exR1(6));
        // System.out.println("Hello Worlds");
    }

    public static String equal(int a, int b, int c) {
        if (a == b && a == c) {
            return "equal";
        }
        return "not equal";
    }

    public static boolean fragment(double x, double y) {
        if (0 < x && x < 1 && 0 < y && y < 1) {
            return true;
        }

        return false;
    }

    public static void myprint() {
        int f = 0;
        int g = 1;
        for (int i = 0; i <= 15; i++) {
            int[] arr = { f, g };
            StdOut.println(Arrays.toString(arr));
            f = f + g;
            g = f - g;
        }

        double t = 9.0;
        while (Math.abs(t - 9.0 / t) > .001)
            t = (9.0 / t + t) / 2.0;
        StdOut.printf("%.5f\n", t);

        int sum = 0;
        for (int i = 1; i < 1000; i++)
            for (int j = 0; j < i; j++)
                sum++;
        StdOut.println(sum);

        // int sum1 = 0;
        // for (int i = 1; i < 1000; i *= 2)
        //     for (int j = 0; j < N; j++)
        //         sum1++;
        // StdOut.println(sum1);
    }
    
    public static int[][] transpose(int[][] arr) {
        int row = arr.length;
        int column = arr[0].length;
        int[][] nArr = new int[column][row];

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                nArr[j][i] = arr[i][j];
            }
        }

        return nArr;
    }

    public static int lg(int N) {
        int ret = 0;
        while (N > 0) {
            N /= 2;
            ret++;
        }

        return ret - 1;
    }

    public static int[] histogram(int[] a, int M) {
        int[] nA = new int[M];
        for (int i = 0; i < M; i++) {
            nA[i] = count(a, i);
        }
        return nA;
    }

    public static int count(int[] a, int k) {
        int count = 0;
        for (int i = 0; i < a.length; i++) {
            if (a[i] == k) {
                count += 1;
            }
        }
        return count;
    }

    public static String exR1(int n) {
       if (n <= 0) return "";
       return exR1(n-3) + n + exR1(n-2) + n;
    }
}
