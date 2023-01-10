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
    public void pre(TreeNode n,ArrayList x)
    {

        if(n!=null)
        {
           
            // x.add(n.val);

            pre(n.left,x);
            x.add("L");
            x.add(Integer.toString(n.val));
            // x.add("R"); 
            pre(n.right,x);
                        x.add("R"); 

           
        }
        else{
            return;
        }
    }

    ArrayList<String> a = new ArrayList<String>();
    ArrayList<String> b = new ArrayList<String>(); 
    public boolean isSameTree(TreeNode p, TreeNode q) {

        pre(p,a);
        pre(q,b);
        if(a.size()==b.size()){
        for(int i=0;i<a.size();i++)
        {
            System.out.println(a.get(i)+" "+b.get(i)+" "+a.get(i).equals(b.get(i)));
            if(a.get(i).equals(b.get(i))==false)
            return false;
            
        }
        return true;
        }
        return false;
    }
}