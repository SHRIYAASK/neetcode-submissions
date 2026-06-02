class Solution {
    public boolean hasDuplicate(int[] nums) {
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) { // Start j from i + 1 to avoid self-comparison
                if (nums[i] == nums[j]) {
                    return true; // Duplicate found, return true immediately
                }
            }
        }
        return false; // No duplicates found
    }
}
