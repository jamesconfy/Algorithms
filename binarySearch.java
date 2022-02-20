class binarySearch {
    public static void main (String[] args) {
        int a[] = {1, 2, 3, 4, 5, 7, 8, 9, 10, 15, 16, 19, 22};
        int val = 8;
        System.out.print(myBinarySearch(a, val));
    }
    static int myBinarySearch(int arr[], int val){
        int start = 0;
        int end = arr.length - 1;
        while(start <= end) {
            int mid = start + end / 2;
            if (arr[mid] == val) {
                return mid + 1;
            }
            else if (arr[mid] < val) {
                start = mid + 1;
            }
            else {
                end = mid - 1;
            }
        }
        return -1;
    }
}