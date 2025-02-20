""" Given an input string `s` and a pattern `p`, implement regular expression matching with support for '.' and '*' where:

'.' matches any single character.
'*' matches zero or more of the preceding element.

The match should be complete (pattern exhausts string and vice versa), not partial. """

def simple_regex_match(s :str, p :str) -> bool:

    # define a match function, taking a string and a pattern of equal length:
    ## iterate over string and pattern
    ## at each index, if pattern char isn't "*" and isn't the string char, return False
    ## return True

    def match_singles(
            s_idx :int,
            p_idx :int,
            match_len :int
        ) -> bool:
        """ Takes a string and a pattern of equal length """
        for i in range(match_len):
            if p[p_idx+i] != "." and p[p_idx+i] != s[s_idx+i]:
                return False
        return True

    # iterate over pattern, opening the first group
    # wherever "*" occurs, mark the beginning and end of the group,
    #   and the ends and beginnings of the groups before and after it
    # save group list entries in the format [type, "pattern", start, end+1]
    #   where type 0 can be simple-matched and type 1 is special ("x*")
    # close the final group

    groups = [[0, "", 0, None]]
    n = len(p)
    for i in range(n):
        if p[i] == "*":
            if groups[-1][2] == i - 1:
                groups.pop(-1)
            else:
                groups[-1][1] = p[groups[-1][2] : i-1]
                groups[-1][3] = i - 1

            groups += [[1, p[i-1 : i+1], i-1, i+1], [0, "", i+1, None]]
        
        if i == n - 1:
            if groups[-1][2] > i:
                groups.pop(-1)
            else:
                groups[-1][1] = p[groups[-1][2] : n]
                groups[-1][3] = n

    # NOTE: Idx 3 of each group listing is never used, and is
    # in any case implied by start idx + subpattern length.
    # Start idx is itself only used by the group list construction logic,
    # and always with exclusive reference to the last group added.
    # Both could be lost, and [-1][2] replaced with a single tracking var.

    # iterate over list of groups
    g, ng = 0, len(groups)
    j, nj = 0, len(s)
    while g < ng:
        # if the string is exhausted before the pattern, it isn't a full match
        if j >= nj:
            return False

        # if group type 0 (not special), check that the first `len(group)` chars of `s` match group[1]
        if groups[g][0] == 0:
            group_len = groups[g][3] - groups[g][2]
            if group_len <= nj - j and match_singles(j, groups[g][2], group_len):
                # g += 1
                j += group_len
            else:
                return False
        # otherwise, if group type 1, initiate special check
        else:
            # set special check start to cur group no
            # iterate over groups until a type-0 group is found and set special check end to the group before it
            backfill = []
            queue_head = 0
            while g < ng and groups[g][0] == 1:
                backfill.append(g)
                g += 1
            queue_len = len(backfill)

            k = j
            if g < ng:
                # now, iterate over `s` until the range from `idx` to `idx + len(group)` matches the type-0 group
                # save the start and end indexes
                group_len = groups[g][3] - groups[g][2]
                found = False
                while j < nj - group_len + 1:
                    if match_singles(j, groups[g][2], group_len):
                        found = True
                    elif found:
                        break
                    j += 1
                if found:
                    j -= 1
                else:
                    return False
                nk = j
                j += group_len
            else:
                nk = j = nj

            # iterate over the special check groups
            while queue_head < queue_len:
                if k >= nk:
                    break

                fill_p = groups[backfill[queue_head]][2]

                # for each group:
                # iterate over s from the special check's start index
                while k < nk:
                    # check that char of s matches the group
                    if not match_singles(k, fill_p, 1):
                        fill_found = False
                        # if it doesn't, but it does match one of the remaining
                        # type 1 groups, move to that group
                        while queue_head < queue_len - 1:
                            queue_head += 1
                            fill_p = groups[backfill[queue_head]][2]
                            if match_singles(k, fill_p, 1):
                                fill_found = True
                                break
                        if queue_head == queue_len - 1 and not fill_found:
                            return False
                    else:
                        k += 1
                
                ########## note the start index and move to that group
                ######## if it doesn't, and doesn't match any remaining type 1 group in the special check group,
                ########## return False

                queue_head += 1

                ###### set check to normal again and move to the next group after the type 0 group
        
        g += 1
    
    # if the pattern was exhausted before the string, it isn't a full match
    if j < nj:
        return False
    
    return True