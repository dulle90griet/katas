def trap_water(height: list[int]) -> int:
        trapped = 0
        hmap = {}

        for i, h in enumerate(height):
            if h > 0:
                if h not in hmap:
                    hmap[h] = [i, i, 1]
                else:
                    hmap[h][1] = i
                    hmap[h][2] += 1
        
        hlist = sorted(list(hmap.keys()), reverse=True)
        if not hlist:
            return 0

        hlist.append(0)
        for i in range(len(hlist) - 1):
            hmap[hlist[i]].append(hlist[i] - hlist[i+1])
        
        for i, h in enumerate(hlist):
            if hmap[h][2] > 1:
                trapped += (hmap[h][1] - hmap[h][0] - hmap[h][2] + 1) * hmap[h][3]

            if i == len(hlist) - 2:
                break

            hmap[hlist[i+1]][2] += hmap[h][2]

            if hmap[h][0] < hmap[hlist[i+1]][0]:
                hmap[hlist[i+1]][0] = hmap[h][0]
            if hmap[h][1] > hmap[hlist[i+1]][1]:
                hmap[hlist[i+1]][1] = hmap[h][1]
        
        return trapped
