# Invert Binary Tree

## 문제 설명
Given the root of a binary tree, invert the tree, and return its root.

## 예시

### Example 1:
![image](https://github.com/user-attachments/assets/a8174d6b-a1b9-42fb-8746-53ecd0ebf80f)

### Example 2:
![image](https://github.com/user-attachments/assets/fd3899a2-fa2b-452c-af47-954ff3152ab0)

### Example 3:
![image](https://github.com/user-attachments/assets/0b963716-ce71-46e1-87dc-ac80368741a4)


# 코드

```cpp
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root == nullptr){
            return nullptr;
        }
        
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;

        invertTree(root->left);
        invertTree(root->right);

        return root;
    }
};
```

## 실행 결과
![image](https://github.com/user-attachments/assets/6c8236b5-4a06-4bbd-92e9-af4b3836ba3c)

## 어떻게 풀었는지..
https://www.notion.so/leetcode-Invert-Binary-Tree-128c7561c39780a5a868e11abffa1417?pvs=4
