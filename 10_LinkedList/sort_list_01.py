# LeetCode 148: Sort List - Bottom-up Merge Sort (Iterative)

from typing import Optional, Tuple


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    # 1) 長さを数える
    n = 0
    cur = head
    while cur:
        n += 1
        cur = cur.next

    dummy = ListNode(0, head)
    size = 1  # マージ対象ブロックの長さ

    # 2) ブロック長を倍々に拡大しながら全体をマージ
    while size < n:
        prev = dummy  # マージ結果を連結していく末尾（tail）を指す
        cur = dummy.next  # 今ラウンドの走査開始ノード

        while cur:
            # 左ブロックの先頭
            left = cur

            # 右ブロックの先頭（leftの直後 size 個で切断）
            right, next_head = _cut_two(cur, size)

            # right が None の場合、右ブロックが不足 → そのまま末尾に連結して終了
            if not right:
                prev.next = left
                break

            # 右ブロックの後ろも size 個で切断し、次の反復の開始点を得る
            # ※ _cut_two で right と next_head は既に求まっている
            # left と right をマージして、prev の後ろに連結
            merged_head, merged_tail = _merge(left, right)
            prev.next = merged_head
            prev = merged_tail

            # 次の2ブロックへ
            cur = next_head

        size <<= 1  # ブロック長を2倍

    return dummy.next


# cur から size 個進んだところで切断して、右ブロックの先頭とその次の開始点を返す
# 返り値: (right_head, next_head)
def _cut_two(
    cur: Optional[ListNode], size: int
) -> Tuple[Optional[ListNode], Optional[ListNode]]:
    # left: cur .. cur+(size-1)
    left_tail = cur
    for _ in range(size - 1):
        if not left_tail:
            break
        left_tail = left_tail.next
    if not left_tail:
        return None, None  # 右ブロックなし

    # right: left_tail.next .. 右側 size ノード
    right = left_tail.next
    left_tail.next = None  # 左ブロックを切断

    # 右ブロックの末尾まで size-1 進む
    right_tail = right
    for _ in range(size - 1):
        if not right_tail:
            break
        right_tail = right_tail.next

    # 次ラウンドの開始点（rightブロックの次）
    next_head = None
    if right_tail:
        next_head = right_tail.next
        right_tail.next = None  # 右ブロックを切断

    return right, next_head


# 2本の昇順リストをマージして (head, tail) を返す
def _merge(
    a: Optional[ListNode], b: Optional[ListNode]
) -> Tuple[Optional[ListNode], Optional[ListNode]]:
    dummy = ListNode()
    tail = dummy
    p, q = a, b

    while p and q:
        if p.val <= q.val:
            tail.next = p
            p = p.next
        else:
            tail.next = q
            q = q.next
        tail = tail.next

    # 片方の残りを丸ごと繋ぐ
    tail.next = p if p else q

    # tail をリスト末端まで進める（次の連結のために必要）
    while tail.next:
        tail = tail.next

    return dummy.next, tail
