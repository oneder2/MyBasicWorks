import json


class GameStats():
    """追踪游戏的统计信息"""
    
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # 游戏在刚启动时处于活动状态
        self.game_active = False

        # 任何时刻不得重置最高分
        try:
            with open("high_score.json", encoding = "utf-8") as fp:
                self.high_score = json.load(fp)
        except FileNotFoundError:
            with open("high_score.json", mode = "w") as fp:
                json.dump(0, fp)
                self.high_score = json.load(fp)


    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

