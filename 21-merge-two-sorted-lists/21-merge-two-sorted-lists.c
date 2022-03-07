/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    if(list1!=NULL && list2!=NULL){     
struct ListNode* final=NULL;
    final=(struct node*)malloc(sizeof(struct ListNode));
    struct ListNode* iter=final;
    while(list1!=NULL && list2!=NULL)
    {
        printf("%d %d\n",list1->val,list2->val);
        struct ListNode* new=NULL;
    new=(struct node*)malloc(sizeof(struct ListNode));
        new->next=NULL;
        final->next=new;
        final=new;
        if(list1->val>=list2->val)
        {
            new->val=list2->val;
            list2=list2->next;
        }
        else{
            new->val=list1->val;
            list1=list1->next;
        }
    }
    while(list1!=NULL)
    {
    struct ListNode* new=NULL;
    new=(struct node*)malloc(sizeof(struct ListNode));
                new->next=NULL;
        final->next=new;
        final=new;
        new->val=list1->val;
        list1=list1->next;
    }
    while(list2!=NULL)
        {
             struct ListNode* new=NULL;
    new=(struct node*)malloc(sizeof(struct ListNode));
        new->next=NULL;
        final->next=new;
        final=new;
        new->val=list2->val;
        list2=list2->next;
    }
    return iter->next;}
    while(list1!=NULL)
    {
        return list1;
    }
    return list2;
    
    
    

    
    
    
}