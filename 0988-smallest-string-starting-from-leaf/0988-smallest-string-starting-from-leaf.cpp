/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    string smallestFromLeaf(TreeNode* root) {
        if (!root) return "";
        char ch = (char)('a' + root->val);
        string str = string(1, ch);
        return dfs(root, str);
    }
    string dfs(TreeNode* root, string str) {
        if (!root) return "";
        string str1, str2;
        if (root->left) str1 = dfs(root->left, (char)('a' + root->left->val) + str);
        if (root->right) str2 = dfs(root->right, (char)('a' + root->right->val) + str);
        if (str1.empty() && str2.empty()) return str;
        if (str1.empty()) return str2;
        if (str2.empty()) return str1;
        return str1 < str2 ? str1 : str2;   
    }
};