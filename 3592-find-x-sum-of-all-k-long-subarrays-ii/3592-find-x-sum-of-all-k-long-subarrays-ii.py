class Solution:
    def findXSum(self, nums, k, x):
        n = len(nums)
        if k == 0 or n == 0:
            return []
        cnt = Counter()
        for i in range(k):
            cnt[nums[i]] += 1

        # Elements are tuples (-freq, -value) so the "best" items sort smallest.
        top = SortedList()
        rest = SortedList()
        top_sum = 0

        def add_to_top(item):
            nonlocal top_sum
            top.add(item)
            top_sum += (-item[0]) * (-item[1])

        def add_to_rest(item):
            rest.add(item)

        def remove_from_top(item):
            nonlocal top_sum
            top.remove(item)
            top_sum -= (-item[0]) * (-item[1])

        def rebalance():
            nonlocal top_sum
            # If too many in top, move worst out.
            while len(top) > x:
                item = top.pop()  # worst in top (last)
                top_sum -= (-item[0]) * (-item[1])
                rest.add(item)
            # If not enough in top, move best from rest in.
            while len(top) < x and rest:
                item = rest.pop(0)
                add_to_top(item)
            # If the best in rest is strictly better than worst in top, swap.
            while rest and top and rest[0] < top[-1]:
                best_rest = rest.pop(0)
                worst_top = top.pop()   # remove worst in top
                top_sum -= (-worst_top[0]) * (-worst_top[1])
                rest.add(worst_top)
                add_to_top(best_rest)

        # initialize sets
        for num, freq in cnt.items():
            rest.add((-freq, -num))
        rebalance()
        result = [top_sum]

        # slide window
        for i in range(k, n):
            left = nums[i - k]
            right = nums[i]

            # remove left (old frequency -> update)
            old_item = (-cnt[left], -left)
            if old_item in top:
                remove_from_top(old_item)
            else:
                rest.discard(old_item)
            cnt[left] -= 1
            if cnt[left] == 0:
                del cnt[left]
            else:
                rest.add((-cnt[left], -left))

            # add right (old frequency removed then new frequency added)
            if right in cnt:
                old_item = (-cnt[right], -right)
                if old_item in top:
                    remove_from_top(old_item)
                else:
                    rest.discard(old_item)
            cnt[right] += 1
            rest.add((-cnt[right], -right))

            # rebalance sets so top holds the x best items
            rebalance()
            result.append(top_sum)

        return result
