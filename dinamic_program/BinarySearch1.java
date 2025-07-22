import java.util.List;

public class BinarySearch1 {
    public static String binarySearch(List<Integer> elems, int elem) {
        int low = 0, high = elems.size() - 1;

        while (low <= high) {
            int mid = (low + high) / 2;

            if (elems.get(mid) == elem) {
                return "Encontrado en la posición " + mid;
            } else if (elems.get(mid) < elem) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return "No encontrado";
    }

    public static void main(String[] args) {
        List<Integer> elems = List.of(4, 5, 6, 7, 8, 9, 89);
        System.out.println(binarySearch(elems, 4));  // Encontrado en la posición 0
        System.out.println(binarySearch(elems, 89)); // Encontrado en la posición 6
        System.out.println(binarySearch(elems, 7)); // No encontrado
    }
}