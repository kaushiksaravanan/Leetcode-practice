/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
struct ListNode *temp1=head;
struct ListNode *temp2=head;
    while (temp2!=NULL && temp2->next!=NULL )
    {  temp2=temp2->next->next;
         temp1=temp1->next;
     if(temp2==temp1)
     {
         return true;
     }
    }
    return false;
    

}