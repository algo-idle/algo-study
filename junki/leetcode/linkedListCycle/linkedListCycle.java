public class Solution {
    public boolean hasCycle(ListNode head) {
        if(head == null){
            return false;
        }
        ListNode pre, now;
        pre = now = head;
        while(now != null && now.next != null){
            pre = pre.next;
            now = now.next.next;
            if(pre == now){
                return true;
            }
        }
        return false;
    }
}