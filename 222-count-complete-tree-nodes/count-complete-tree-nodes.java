/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int countNodes(TreeNode root) {
        return postOrder(root, 0);
    }
    
    public int postOrder(TreeNode root, int num){
        if(root == null){
            return num;
        }
                
        num = postOrder(root.left, num);
        num += 1;
        num = postOrder(root.right, num);
        
        return num;
    }
}