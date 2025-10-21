from django.db import models

# | Поле                                               | Назначение                                                    |
# | -------------------------------------------------- | ------------------------------------------------------------- |
# | `CharField(max_length=...)`                        | Строка фиксированной длины (обязательно указать `max_length`) |
# | `TextField()`                                      | Длинный текст без ограничения по длине                        |
# | `IntegerField()`                                   | Целое число                                                   |
# | `PositiveIntegerField()`                           | Положительное целое число                                     |
# | `FloatField()`                                     | Число с плавающей точкой                                      |
# | `DecimalField(max_digits=..., decimal_places=...)` | Десятичное число с точной точкой (для денег)                  |
# | `BooleanField()`                                   | Логическое значение `True/False`                              |
# | `DateField(auto_now_add=True/auto_now=True)`       | Дата                                                          |
# | `TimeField(auto_now_add=True/auto_now=True)`       | Время                                                         |
# | `DateTimeField(auto_now_add=True/auto_now=True)`   | Дата и время                                                  |
# | `EmailField()`                                     | Строка с валидацией email                                     |
# | `URLField()`                                       | Строка с валидацией URL                                       |
# | `SlugField()`                                      | Строка для URL-путей (обычно латиница, тире)                  |
# | `UUIDField()`                                      | Уникальный идентификатор UUID                                 |
# | `JSONField()`                                      | Хранение JSON-данных                                          |
# | `FileField(upload_to='...')`                       | Загрузка файла                                                |
# | `ImageField(upload_to='...')`                      | Загрузка изображения (нужна Pillow)                           |


# | Поле                                  | Назначение                                       |
# | ------------------------------------- | ------------------------------------------------ |
# | `ForeignKey(Model, on_delete=...)`    | Связь "многие к одному" (обязателен `on_delete`) |
# | `OneToOneField(Model, on_delete=...)` | Связь "один к одному"                            |
# | `ManyToManyField(Model)`              | Связь "многие ко многим"                         |


# | Аргумент               | Назначение                           |
# | ---------------------- | ------------------------------------ |
# | `null=True`            | Поле может быть `NULL` в базе данных |
# | `blank=True`           | Поле может быть пустым в формах      |
# | `default=...`          | Значение по умолчанию                |
# | `unique=True`          | Уникальное значение                  |
# | `choices=[(..., ...)]` | Ограниченный список значений         |
# | `verbose_name="..."`   | Название поля в админке              |
# | `help_text="..."`      | Подсказка в админке                  |



class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    bio = models.CharField(max_length=100, default="Биография пока не заполнена")  # default применён здесь
    created_at = models.DateTimeField(auto_now_add=True)  # убран default

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

    
class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='articles')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author_name} on {self.article.title}"
