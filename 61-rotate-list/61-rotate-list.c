/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* rotateRight(struct ListNode* head, int k){
    struct ListNode* temp=head;
    int len=0;
    while(temp!=NULL)
    {
        temp=temp->next;
        len+=1;
    }
    if(len==0)
    return 0;
    k=k%len;
    len-=k;
    len-=1;
    printf("%d\n",len);
    // temp=head;
    
    temp=head;
    
    struct ListNode* temp2=head;
    struct ListNode* ke=head;
    
    while(temp2->next!=NULL)
    {
        temp2=temp2->next;
    }
    temp2->next=head;
    int y=0;
    while(true)
    {
        ke=temp->next;
        if(y==len)
        {
            temp->next=NULL;
    break;}
        temp=temp->next;
        y+=1;
            
    }
return ke;
}