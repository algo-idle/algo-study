# 3sum
|시간 제한|메모리 제한|
|:--:|:--:|
|1초|128MB|

## 문제
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

## 문제 설명


## 입력
```
```

## 출력
```
```

## 코드
```java
public static List<List<Integer>> threeSum(int[] nums) {
    Arrays.sort(nums);
    Set<List<Integer>> result = new HashSet<>();


    for (int i = 0; i < nums.length - 2; i++) {
        int left = i + 1;
        int right =  nums.length - 1;

        while(left < right){
            int sum = nums[i] + nums[left] + nums[right];

            if (sum == 0) {
                result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                left++;
                right--;
            } else if (sum < 0) {
                left++;
            } else {
                right--;
            }
        }
    }

    return new ArrayList<> (result);
}
```

## 채점 결과!
[img.png](img.png)