class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> arr;
        for (int i = 0; i < nums.size(); i++){
            for (int j = 0; j < i; j++) {
                if (nums[i] + nums[j] == target) {
                    arr.push_back(j);
                    arr.push_back(i);
                    return arr;
                    break;
                }
            }
        }
        return arr;
    }
};
