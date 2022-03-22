/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* mergeNodes(struct ListNode* head){
    struct ListNode* temp=head;
    struct ListNode* fin[1000000];
    int prev=0;
    int k=0;
    int curr=0;
    while(temp!=NULL)
    {
        if(temp->val==0 && curr==0)
        {
            curr=1;
        }
        if(temp->val==0 && curr==1)
        {
            fin[k]=prev;
            k+=1;
            prev=0;
            curr=0;
        }
        prev+=temp->val;
        temp=temp->next;
    }
    temp=head;
    struct ListNode* temp2=head;
    int i=1;
    while(i<k)
    {
        head->val=fin[i];
        i+=1;
        temp2=head;
        head=head->next;
    }
    temp2->next=NULL;
    // head=NULL;
    return temp;
}