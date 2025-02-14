def find_longest_palindrome(s: str) -> str:
    s_prime = "#" + "#".join(s) + "#"
    n = len(s_prime)
    prime_radii = [0] * n
    center = radius = 0

    for i in range(n):
        mirror = center * 2 - i

        if i < radius:
            prime_radii[i] = min(radius - 1, prime_radii[mirror])
        
        while(i + 1 + prime_radii[i] < n
              and i - 1 - prime_radii[i] >= 0
              and s_prime[i + 1 + prime_radii[i]]
                == s_prime[i - 1 - prime_radii[i]]):
            prime_radii[i] += 1

        if i + prime_radii[i] > radius:
            center = i
            radius = i + prime_radii[i]
    
    max_length = max(prime_radii)
    center_index = prime_radii.index(max_length)
    start_index = (center_index - max_length) // 2

    return s[start_index : start_index + max_length]