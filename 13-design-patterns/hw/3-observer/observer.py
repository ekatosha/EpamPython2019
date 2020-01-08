"""
Observer (Наблюдатель)
Определяет зависимость типа один ко многим между объектами таким образом, что при изменении состояния одного объекта
  все зависящие от него оповещаются об этом событии.
При реализации шаблона «наблюдатель» обычно используются следующие классы:
  Observable — интерфейс, определяющий методы для добавления, удаления и оповещения наблюдателей;
  Observer — интерфейс, с помощью которого наблюдатель получает оповещение;
  ConcreteObservable — конкретный класс, который реализует интерфейс Observable;
  ConcreteObserver — конкретный класс, который реализует интерфейс Observer.
Шаблон «наблюдатель» применяется в тех случаях, когда система обладает следующими свойствами:
  * существует, как минимум, один объект, рассылающий сообщения;
  * имеется не менее одного получателя сообщений, причём их количество и состав могут изменяться
    во время работы приложения;
  * нет надобности очень сильно связывать взаимодействующие объекты, что полезно для повторного использования.
Данный шаблон часто применяют в ситуациях, в которых отправителя сообщений не интересует,
  что делают получатели с предоставленной им информацией.
"""

from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Абстрактный наблюдатель
    """

    @abstractmethod
    def update(self, message: str) -> None:
        """
        Получение нового сообщения
        """
        pass


class Observable(ABC):
    """
    Абстрактный наблюдаемый
    """

    def __init__(self) -> None:
        pass  # инициализация списка наблюдателей

    def subscribe(self, observer: Observer) -> None:
        """
        Регистрация нового наблюдателя на подписку
        """
        pass

    def unsubscribe(self, observer: Observer) -> None:
        """
        Регистрация нового наблюдателя на подписку
        """
        pass

    def publish_video(self, video: str) -> None:
        """
        Передача сообщения всем наблюдателям, подписанным на события
        данного объекта наблюдаемого класса
        """
        pass


class YoutubeChannel(Observable):

    def __init__(self, channel_name, chanel_owner):
        self.observers = list()
        self.channel_name = channel_name
        self.chanel_owner = chanel_owner
        self.playlists = {}

    def subscribe(self, user):
        self.observers.append(user)

    def unsubscribe(self, user) -> None:
        """
        Регистрация нового наблюдателя на подписку
        """
        if observer in self.observers:
            self.observers.remove(user)

    def publish_video(self, video):
        for observer in self.observers:
            print(f'Dear {observer}, there is a new video on "{self.channel_name}" channel: {video}')

    def publish_playlist(self, playlist):
        for key, value in playlist.items():
            for observer in self.observers:
                print(f'Dear {observer}, there is new playlist on "{self.channel_name}" channel: {key}')
        self.playlists.update(playlist)


class MyTubeUser(Observer):

    def __init__(self, _name):
        self.name = _name

    def __str__(self):
        return self.name

    def update(self, message: str) -> None:
        """
        Получение очередной новости
        """
        print(f'{self.name} узнал следующее: {message}')


if __name__ == '__main__':
    matt = MyTubeUser('Matt')
    john = MyTubeUser('John')
    erica = MyTubeUser('Erica')
    dogs_life = YoutubeChannel('All about dogs', matt)
    dogs_life.subscribe(john)
    dogs_life.subscribe(erica)
    dogs_nutrition_videos = ['What do dogs eat?', 'Which Pedigree pack to choose?']
    dogs_nutrition_playlist = {'Dogs nutrition': dogs_nutrition_videos}
    for video in dogs_nutrition_videos:
        dogs_life.publish_video(video)
    dogs_life.publish_playlist(dogs_nutrition_playlist)