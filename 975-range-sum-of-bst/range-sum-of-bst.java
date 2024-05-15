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
    public int rangeSumBST(TreeNode root, int low, int high) {
        if(root == null){
            return 0;
        }
        
        Queue<TreeNode> queue = new LinkedList();
        
        queue.offer(root);
        
        int ans = 0;
        
        while(!queue.isEmpty()){
            TreeNode node = queue.poll();
            
            if(node.val >= low  && node.val <= high){
                ans += node.val;
            }
            
            if(node.left != null && node.val >= low){
                queue.offer(node.left);
            }
            
            if(node.right != null && node.val <= high){
                queue.offer(node.right);
            }
        }
        
        return ans;
        
    }
}