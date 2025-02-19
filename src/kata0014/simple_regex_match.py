""" Given an input string `s` and a pattern `p`, implement regular expression matching with support for '.' and '*' where:

'.' matches any single character.
'*' matches zero or more of the preceding element.

The match should be complete (pattern exhausts string), not partial. """

def simple_regex_match(s :str, p :str) -> bool:

    # define a match function, taking a string and a pattern of equal length:
    ## iterate over string and pattern
    ## at each index, if pattern char isn't "*" and isn't the string char, return False
    ## return True

    def match_singles(sub_s :str, sub_p :str) -> bool:
        """ Takes a string and a pattern of equal length """
        for i in len(sub_p):
            if sub_p[i] != "." and sub_p[i] != sub_s[i]:
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

    # iterate over list of groups
    ### if group type 0 (not special), check that the first `len(group)` chars of `s` match group[1]
    ##### set the start and end indexes according to the positions in `s`, and the start index of the next group
    ### otherwise, if group type 1, initiate special check
    ##### set special check start to cur group no
    ##### iterate over groups until a type-0 group is found and set special check end to the group before it
    ##### now, iterate over `s` until the range from `idx` to `idx + len(group)` matches the type-0 group
    ##### save its start and end indexes
    ##### iterate over the special check groups
    ##### for each group:
    ######## iterate over s from the group's start index
    ######## check that char of s matches the group
    ######## if it doesn't, but it does match one of the remaining type 1 groups,
    ########## note the start index and move to that group
    ######## if it doesn't, and doesn't match any remaining type 1 group in the special check group,
    ########## return False
    ###### set check to normal again and move to the next group after the type 0 group