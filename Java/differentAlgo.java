// import java.io.*;
import java.util.Arrays;

public class differentAlgo {
    public static void main(String[] args) {
        int[] a = { 4, 5, 12, 15, 10, 11, 13 };
        int[][] r = { { 1, 2, 3, 4, 5 }, { 6, 7, 8, 9, 10 } };
        int[][] p = r;
        System.out.println(Arrays.toString(reverse(a)));
        System.out.println(average(a));
        System.out.println(max(a));
        System.out.println(Arrays.toString(reverse(copy(a))));
        System.out.println(Arrays.deepToString(manipulate(r, p)));
        System.out.println(sqrt(a[5]));
        System.out.println(isPrime(a[1]));
        System.out.println(H(a[6]));
        System.out.println(hypotenuse(5, 5));
        // int w = (int) (Math.random() * 10) + 1;
        // System.out.println(w);
    }

    public static double average(int[] a) {
        double sum = 0.0;
        for (int i = 0; i < a.length; i++) {
            sum += a[i];
        }
        return sum / a.length;
    }
    
    public static int[] reverse(int[] a) {
        int N = a.length;
        for (int i = 0; i < N / 2; i++) {
            int temp = a[i];
            a[i] = a[N - 1 - i];
            a[N - i - 1] = temp;
        }
        return a;
    }
    
    public static int max(int[] a) {
        int max = 0;
        for (int i = 0; i < a.length; i++) {
            if (a[i] > max)
                max = a[i];
        }
        return max;
    }

    public static int[] copy(int[] a) {
        int[] b = Arrays.copyOf(a, a.length);
        return b;
    }

    public static int[][] manipulate(int[][] a, int[][] b) {
        int N = a.length;
        // int M = a[0].length;
        // int[][] c = new int[N][M];
        int[][] c = new int[N][N];
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++) { // Compute dot product of row i and column j.        
                for (int k = 0; k < N; k++)
                    c[i][j] += a[i][k] * b[k][j];
            }
        return c;
    }
    
    public static int abs(int value) {
        if (value < 0) {
            return -value;
        }
        return value;
    }


    public static boolean isPrime(int N) {
        if (N < 2)
            return false;
        for (int i = 2; i * i <= N; i++)
            if (N % i == 0)
                return false;
        return true;
    }
    
    public static double sqrt(double c) {
        if (c < 0)
            return Double.NaN;
        double err = 1e-15;
        double t = c;
        while (Math.abs(t - c / t) > err * t)
            t = (c / t + t) / 2.0;
        return t;
    }
    
    public static double hypotenuse(double a, double b) {
        return Math.sqrt(a * a + b * b);
    }

    public static double hypotenuse() {
        return hypotenuse(0.0, 0.0);
    }

    // public static double hypotenuse(double a) {
    //     return hypotenuse(a, 0.0);
    // }

    public static double hypotenuse(double b) {
        return hypotenuse(0.0, b);
    }

    public static double H(int N) {
        double sum = 0.0;
        for (int i = 1; i <= N; i++)
            sum += 1.0 / i;
        return sum;
    }
}
