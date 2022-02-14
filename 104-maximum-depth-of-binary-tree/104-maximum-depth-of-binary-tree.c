int maxDepth(struct TreeNode* root){
    if(root==NULL)
        return 0;
    int a=maxDepth(root->right);
    int b=maxDepth(root->left);
    return 1+(a>b?a:b);
}