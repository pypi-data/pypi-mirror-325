import random
from typing import Dict

class Pool:
    def __init__(self, total_draws: int, target_expected: float, tolerance: float = 1e-5):
        """
        初始化抽奖池
        :param total_draws: 总抽奖次数，保证在 total_draws 次内必中奖
        :param target_expected: 目标数学期望抽奖次数
        :param tolerance: 二分法查找基础概率的容差
        """
        self.total_draws = total_draws
        self.target_expected = target_expected
        self.p = self._find_base_probability(tolerance)
        self.current_draw = 0

    def _expected_draws(self, p: float):
        """
        计算给定 p 下的数学期望抽奖次数。
        每次抽奖 i 的中奖概率为 i * p，若前 i-1 次都没中。
        第 total_draws 次若前面都没中，则必中奖。
        :param p: 基础中奖概率
        :return: 数学期望抽奖次数
        """
        exp = 0.0
        prob_no_win = 1.0
        for i in range(1, self.total_draws):
            win_prob = min(i * p, 1.0)  # 当前这次抽奖的中奖概率，保证不超过 1
            this_prob = prob_no_win * win_prob  # 中奖的事件（前 i-1 次都没中）
            exp += i * this_prob
            prob_no_win *= (1 - win_prob)
        exp += self.total_draws * prob_no_win  # 第 total_draws 次必中奖
        return exp

    def _find_base_probability(self, tolerance):
        """
        使用二分法在 [0, 1/total_draws] 中寻找合适的 p，使得数学期望接近 target_expected。
        :param tolerance: 容差
        :return: 基础中奖概率 p
        """
        lo = 0.0
        hi = 1.0 / self.total_draws
        while hi - lo > tolerance:
            mid = (lo + hi) / 2
            exp_val = self._expected_draws(mid)
            if exp_val > self.target_expected:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2

    def reset(self):
        """重置抽奖次数"""
        self.current_draw = 0

    def draw(self):
        """
        模拟一次抽奖。如果中奖，则返回 True，否则返回 False。
        抽奖概率依次增大，且在 total_draws 次时必中奖。
        :return: 是否中奖
        """
        self.current_draw += 1
        if self.current_draw >= self.total_draws:
            self.reset()
            return True

        chance = min(self.current_draw * self.p, 1.0)  # 计算当前抽奖的中奖概率，保证不超过 1
        if random.random() < chance:
            self.reset()
            return True
        return False

class PoolManager:
    def __init__(self, pools: Dict[int, Pool] = None, /, default_total_draws: int = 0) -> None:
        """池管理器，管理多个抽奖池
        :param pools: 抽奖池字典，键为池 ID，值为 Pool 对象
        """
        self.pools: Dict[int, Pool] = pools if pools is not None else {}
        self.total_draws = default_total_draws
        self.current_draw = 0
        self.null_return = -1
        self.sort()
        
    def draw(self) -> int:
        """从所有抽奖池中随机抽取一个池，并进行一次抽奖"""
        self.current_draw += 1
        for pool_id, pool in self.pools.items():
            if pool.draw():
                return pool_id
        return self.null_return

    def add(self, pool_id: int = None, *, total_draws: int = None, target_expected: float = 0.0, tolerance: float = 1e-5) -> None:
        """添加一个抽奖池"""
        pool_id = len(self.pools) if pool_id is None else pool_id
        total = self.total_draws if total_draws is None else total_draws
        self.pools[pool_id] = Pool(total, target_expected, tolerance)
        self.sort()
    
    def add_pool(self, pool: Pool) -> None:
        """添加一个抽奖池"""
        pool_id = len(self.pools)
        self.pools[pool_id] = pool
        self.sort()
    
    def sort(self) -> None:
        """按照抽奖次数排序"""
        self.pools = dict(sorted(self.pools.items(), key=lambda x: x[1].total_draws, reverse=True))
    
    def reset(self) -> None:
        """重置所有抽奖池"""
        for pool in self.pools.values():
            pool.reset()