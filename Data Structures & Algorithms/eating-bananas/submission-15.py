class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search
        #   time :
        #   space:
        
        l, r = 1, max(piles)    # l, r pointers on list: 1 ~ max(piles)
        while l <= r:
            mPile = l + (r - l) // 2

            spentH = 0
            for curPile in piles:
                spentH += math.ceil(curPile / mPile)
            
            if spentH <= h:     ## 먹는 시간이 덜걸려서, pile을 더 먹어야한다
                r = mPile - 1
            else:               ## 먹는 시간이 더걸려서, pile을 덜 먹어야한다
                l = mPile + 1
            
        return l
                
