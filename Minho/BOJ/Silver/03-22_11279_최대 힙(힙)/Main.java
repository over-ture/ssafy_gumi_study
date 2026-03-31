import java.util.*;
import java.io.*;

class MaxHeap {
    long[] arr = new long[200001];
    int size = 0;

    long poll() {
        if (size <= 0)
            return 0;
        long ret = arr[1];
        arr[1] = arr[size--];
        int now = 1;
        while (now * 2 <= size) {
            int left = now * 2;
            int right = now * 2 + 1;
            int target = left;

            if (right <= size && arr[right] > arr[left]) {
                target = right;
            }
            if (arr[now] >= arr[target])
                break;

            long tmp = arr[now];
            arr[now] = arr[target];
            arr[target] = tmp;
            now = target;
        }

        return ret;

    }

    void add(long element) {

        if (size > 200000)
            return;
        arr[++size] = element;
        int idx = size;

        int parent = idx / 2;

        while (idx > 1 && arr[parent] < arr[idx]) {
            // swap
            long tmp = arr[parent];
            arr[parent] = arr[idx];
            arr[idx] = tmp;
            // update idx
            idx = parent;
        }
    }

    int len() {
        return size;
    }

    long top() {
        if (size <= 0)
            return 0;
        return arr[1];
    }
}

public class Main {
    static int n;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;// = new StringTokenizer( br.readLine());
        StringBuilder sb = new StringBuilder();
        n = Integer.parseInt(br.readLine());
        MaxHeap heap = new MaxHeap();
        for (int i = 0; i < n; ++i) {
            int now = Integer.parseInt(br.readLine());
            if (now > 0)
                heap.add(now);
            else
                sb.append(heap.poll() + "\n");
        }

        System.out.print(sb + "");

    }
}
