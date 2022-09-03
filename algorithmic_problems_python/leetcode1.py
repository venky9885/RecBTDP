
# ans = []


class sol:
    def __init__(self) -> None:
        self.ans = []

    def quad(self, lst, ct, sl, tgt):
        global ans

        if(len(sl) == 4 and sum(sl) == tgt):

            print(sl)
            asd = sl.copy()
            # ans.append(sl)
            self.ans.append(asd)
            # Solution.ans.append(sl)
            # ct = 0
            return
        if(len(lst) <= ct):
            return
            # print(ct)
        sl.append(lst[ct])
        self.quad(lst, ct+1, sl, tgt)
        sl.pop()
        self.quad(lst, ct+1, sl, tgt)


t = sol()
sl = []
t.quad([1, 0, -1, 0, -2, 2], 0, sl, 0)
print(t.ans)
'''


class Kth:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k

    def swap(self, f_ind, l_ind):
        self.nums[f_ind], self.nums[l_ind] = self.nums[l_ind], self.nums[f_ind]

    def partion(self, f_ind, l_ind):
        pivot = random.randint(f_ind, l_ind)
        self.swap(pivot, l_ind)
        # firstind = 0
        for i in range(f_ind, l_ind):
            if(self.nums[i] > self.nums[l_ind]):
                self.swap(i, f_ind)
                f_ind += 1
        self.swap(f_ind, l_ind)
        return f_ind

    def kthl(self, f_ind, l_ind):
        pivot = self.partion(f_ind, l_ind)
        if(pivot < self.k):
            return self.kthl(pivot+1, l_ind)
        elif(pivot > self.k):
            return self.kthl(f_ind, pivot-1)
        return self.nums[pivot]


# nums = [3, 2, 1, 5, 6, 4]
# k = 2
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 3
t = Kth(nums, k)
print(t.kthl(0, len(nums)-1))
'''
