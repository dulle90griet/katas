# CodeKata.com Kata 03: How Big? How Fast?

> Rough estimation is a useful talent to possess. As you’re coding away, you may suddenly need to work out approximately how big a data structure will be, or how fast some loop will run. The faster you can do this, the less the coding flow will be disturbed.
> 
> So this is a simple kata: a series of questions, each asking for a rough answer. Try to work each out in your head.

## How Big?

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

> My town has approximately 20,000 residences. How much space is required to store the names, addresses, and a phone number for all of these (if we store them as characters)?

- 4,000,000 bytes, i.e. a bit less than 4MB.

(Reasoning: 2 bytes to a 16-bit UTF16 character. Approx. 100 chars for name, address, phone: 25 + 65 + 15.)

> I’m storing 1,000,000 integers in a binary tree. Roughly how many nodes and levels can I expect the tree to have? Roughly how much space will it occupy on a 32-bit architecture?

- 1,000,000 nodes, of which approx. 500,000 leaf nodes
- 20 levels
- approx. 8MB total space occupied

(Reasoning: 4 bytes per int gives 4MB for the integers. 4 bytes per pointer for the branch nodes, assumed to be approx. half of all nodes but each to have two branches, then doubles the size. If the leaf nodes also store pointers to NULL values, this should rise to 12MB.)


