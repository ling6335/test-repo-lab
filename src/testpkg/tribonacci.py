def tribonacci(n: int) -> int:
    """Calculates the n-th tribonacci number.

    Here, the tribonacci sequence is defined as follows:
    - tribonacci(0) = 0
    - tribonacci(1) = 1
    - tribonacci(2) = 1
    - tribonacci(n) = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
    """
    trib_history = [0, 1, 1, 0]
    if n < 3:
        return trib_history[n]
    for _ in range(n-2):
        trib_history[3] = sum(trib_history[:3])
        trib_history[:3] = trib_history[1:]
    return trib_history[3]
