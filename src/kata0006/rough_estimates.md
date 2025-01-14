# CodeKata.com Kata 03: How Big? How Fast?

Available here: http://codekata.com/kata/kata03-how-big-how-fast/

> Rough estimation is a useful talent to possess. As you’re coding away, you may suddenly need to work out approximately how big a data structure will be, or how fast some loop will run. The faster you can do this, the less the coding flow will be disturbed.
> 
> So this is a simple kata: a series of questions, each asking for a rough answer. Try to work each out in your head.

## How Big?

### Task 01

> Roughly how many binary digits (bit) are required for the unsigned representation of:
>
> - 1,000
> - 1,000,000
> - 1,000,000,000
> - 1,000,000,000,000
> - 8,000,000,000,000

1. 1,000: 10 bits
2. 1,000,000: 20 bits
3. 1,000,000,000: 30 bits
4. 1,000,000,000,000: 40 bits
5. 8,000,000,000,000: 43 bits

(Reasoning: 1,000 is almost 1,024, or 2^10. Most subsequent steps multiply by 1,000, or approx. ×2^10 - so adding 10 bits each time. The final step multiplies by 8, or ×2^3.)

### Task 02

> My town has approximately 20,000 residences. How much space is required to store the names, addresses, and a phone number for all of these (if we store them as characters)?

- 4,000,000 bytes, i.e. a bit less than 4MB, if using UTF16. In UTF8, approx. 2MB.

(Reasoning: 2 bytes to a 16-bit UTF16 character. Approx. 100 chars for name, address, phone: 25 + 65 + 15.)

### Task 03

> I’m storing 1,000,000 integers in a binary tree. Roughly how many nodes and levels can I expect the tree to have? Roughly how much space will it occupy on a 32-bit architecture?

- 1,000,000 nodes, of which approx. 500,000 leaf nodes
- 20 levels
- approx. 8MB total space occupied

(Reasoning: 4 bytes per int gives 4MB for the integers. 4 bytes per pointer for the branch nodes, assumed to be approx. half of all nodes but each to have two branches, then doubles the size. If the leaf nodes also store pointers to NULL values, this should rise to 12MB.)

## How Fast?

### Task 04

> My copy of Meyer’s Object Oriented Software Construction has about 1,200 body pages. Assuming no flow control or protocol overhead, about how long would it take to send it over an async 56k baud modem line?

- ~~2 minutes~~ 14 minutes

(Reasoning: Assume 350 words per page average. 12 * 3.5 is 42. 1,200 * 350 is 420,000. In UTF-16, that's 840,000 bytes. 56k bits/second is 7k bytes/second. 840/7 gives 120 seconds. _EDIT: Need also to account for word length! Say 7 chars avg per word gives 840 seconds, or 14 minutes._)

### Task 05

> My binary search algorithm takes about 4.5mS to search a 10,000 entry array, and about 6mS to search 100,000 elements. How long would I expect it to take to search 10,000,000 elements (assuming I have sufficient memory to prevent paging).

- ~~171 milliseconds~~ 7.9 milliseconds

(Reasoning: from 10,000 to 100,000 is 90,000 elements; to 1,000,000, another 900,000; to 10,000,000, another 9,000,000. The first took an extra 1.5ms, so to get to 10,000,000 should take a further 15 + 150 ms. _EDIT: But, wait, binary search time complexity is O(log2(n)), not O(n)! log2(10,000) is between 13 and 14; log2(100,000) is between 16 and 17. 4.5 / 14 is about 0.3. 6 / 17 is closer to 0.35. log2(10,000,000) gives between 23 and 24; 24 * 0.33 is 7.2 + 0.72 = 7.92ms._)

### Task 06

> Unix passwords are stored using a one-way hash function: the original string is converted to the ‘encrypted’ password string, which cannot be converted back to the original string. One way to attack the password file is to generate all possible cleartext passwords, applying the password hash to each in turn and checking to see if the result matches the password you’re trying to crack. If the hashes match, then the string you used to generate the hash is the original password (or at least, it’s as good as the original password as far as logging in is concerned). In our particular system, passwords can be up to 16 characters long, and there are 96 possible characters at each position. If it takes 1mS to generate the password hash, is this a viable approach to attacking a password?

- No

(Reasoning: The number of possible combinations of 96 characters over 16 places is 96^16 - approximate that as 100^16, or 1E32. For any given number, n^1 + n^2 + ... + n^(x-1) is approximately equal to n^x / (n-1), so to account for passwords of 1-15 characters in length we'd add 1E32 / 99, or 1E30, giving 1.01E32 total - not in the end a significant increase at this scale and level of accuracy. At 1000 passwords a second, this would take 1E29 seconds, or - approximating 60 as 50, and 24 as 25 - 2E27 minutes (* 2 / 100), which is 4E25 hours (* 2 / 100), which is 16E23 or 1.6E24 days (* 4 / 100). Divide that very roughly by 300 and we're still in the realm of 0.5E21 or 5E22 years, many times longer than the Earth has existed at approx. 4.5E9 years.)
