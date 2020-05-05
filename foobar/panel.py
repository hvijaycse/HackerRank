def Solution( area):
    ans = []
    while area:
        small = int( area**(0.5))
        temp_area = small*small
        ans.append( temp_area)
        area = area - temp_area
    return ans
        