# Дополнительное практическое задание по модулю 5
from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = list()
        self.videos = list()
        self.current_user = None

    def log_in(self, nickname, password):
        for us in self.users:
            if isinstance(us, User):
                if us.nickname == nickname and us.password == hash(password):
                    self.current_user = us
                    #print(f"User {nickname} is logged in")
                    return
        print(f"User {nickname} is not found")

    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        if user in self:
            print(f"Пользователь {nickname} уже существует")
        else:
            self.users.append(user)
            #print(f"{nickname} is registered")
            self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None
        print("User is logged out")

    def add(self, *video):
        for v in video:
            if v not in self:
                self.videos.append(v)

    def get_videos(self, search_word):
        video_list = []
        for v in self.videos:
            if isinstance(v, Video):
                if str(search_word).lower() in str(v.title).lower():
                    video_list.append(v.title)
        return video_list

    def watch_video(self, video_title):
        for v in self.videos:
            if v.title == video_title:
                if self.current_user is None:
                    print("Войдите в аккаунт, чтобы смотреть видео")
                    return
                else:
                    if self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                        return
                    for i in range(v.time_now, v.duration + 1):
                        print(i, end=" ")
                        sleep(0)
                    print("Конец видео")
                    return

    def __contains__(self, item):
        if isinstance(item, User):
            return any(item.nickname == obj.nickname for obj in self.users)
        if isinstance(item, Video):
            return any(item.title == obj.title for obj in self.videos)





ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Лучший язык программирования 2024 года', 200)
# Добавление видео
ur.add(v1, v2, v3)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')


# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
ur.log_in("dyma", "1234")