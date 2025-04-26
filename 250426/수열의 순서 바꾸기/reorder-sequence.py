from typing import List

n = int(input())
sequence = list(map(int, input().split()))

def inc_tail_start(seq: List[int]) -> int:
    i = len(seq) - 1
    while i >= 0:
        if seq[i] != i + 1:
            return i
    return -1

def is_sorted(seq: List[int]) -> bool:
    for i, x in enumerate(seq):
        if x != i + 1:
            return False
    return True

def find_moves(seq: List[int], moves: int) -> int:
    if is_sorted(seq):
        return moves
    
    t = inc_tail_start(seq)
    n = t + 1
    seq = seq[:t+1]
    while not is_sorted(seq):
        x = seq.pop(0)

        if x == n:
            seq.append(x)
            moves += 1
            break
        
        n_idx = seq.index(n)
        insert_idx = n_idx + 1
        while x > seq[insert_idx] and insert_idx < n:
            insert_idx += 1
        if insert_idx == n:
            seq.append(x)
        else:
            seq.insert(insert_idx, x)
        
        moves += 1

    return find_moves(seq, moves)

print(find_moves(sequence, 0))