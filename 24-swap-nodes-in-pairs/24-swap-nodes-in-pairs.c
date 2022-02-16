#include<stdlib.h>

struct ListNode* swapPairs(struct ListNode* head){
    int n=0;
    struct ListNode * temp=NULL;
    temp=(struct ListNode*)malloc(sizeof(struct ListNode));
    temp=head;
    int i=0,x;
    while(temp!=NULL && temp->next!=NULL)
     {if(i%2==0){
        x=temp->val;
     temp->val=temp->next->val;
        temp->next->val=x;}
        temp=temp->next->next;
      i+=2;
   }
return head;
}