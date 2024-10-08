import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Solution {

    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{};
    }

    public static void main(String[] args) {
        // Example input handling
        String input = "nums = [2,7,11,15], target = 9";
        List<String> inputList = List.of(input.split(", "));
        int[] arr = getNum(inputList.get(0));
        int target = getNum(inputList.get(1))[0];

        Solution solution = new Solution();
        int[] result = solution.twoSum(arr, target);

        for (int index : result) {
            System.out.print(index + " ");
        }
    }

    private static int[] getNum(String input) {
        List<Integer> arr = new ArrayList<>();
        Pattern pattern = Pattern.compile("\\d+");
        Matcher matcher = pattern.matcher(input);

        while (matcher.find()) {
            arr.add(Integer.parseInt(matcher.group()));
        }

        return arr.stream().mapToInt(i -> i).toArray();
    }
}