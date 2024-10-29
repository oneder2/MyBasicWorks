class star:
    def __init__(self, name, movie):
        self.name = name
        self.movie = movie
    
    def __str__(self) -> str:
        return self.name + "是我的偶像，我非常喜欢他的电影" + self.movie

    def __del__(self):
        print("我不喜欢" + self.name + "了")

    def change_name(self, name):
        self.name = name
    
    def change_movie(self, movie):
        self.movie = movie
    
    def playing(self):
        print(self.name + "出演了" + self.movie + "，煞是动人")


def period(obj, name, movie):
    obj.playing()

# 明星和电影名列表
names = []
movies = []

for i in range(2):
    names.append(input("type in name"))
    movies.append(input("type in movies"))

# 批量创建对象
objs = []
obj_amount = 2
for i in range(obj_amount):
    obj = star(names[i], movies[i])
    objs.append("obj" + str(i))

for i in range(len(names)):
    period(objs[i], names[i], movies[i])





# zxc = star("周星驰", "Kongfu")
# print(zxc.name)
# print(zxc.movie)
# zxc.change_name("周星星")
# print(zxc.name)
# zxc.change_movie("赌圣")
# print(zxc.movie)

# print(zxc)
# del zxc