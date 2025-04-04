import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dsa_cat_module_python",  # Замените!  Уникальное имя.
    version="0.0.0",  # Начальная версия
    author="dsa_cat",  # Ваше имя
    license="MPL-2.0",  # Краткое название лицензии
    license_files = ["LICENSE"],
    author_email="dsa.kirov@yandex.ru",
    description="This is a module for a wide variety of tasks.",  # Краткое описание
    long_description=long_description,  # Длинное описание из README.md
    long_description_content_type="text/markdown",  # Тип контента README.md
    url="https://github.com/dsacat/dsa_cat_module_python/tree/main",  # URL вашего репозитория
    packages=setuptools.find_packages(), # Автоматически находит пакеты
    python_requires='>=3.6', # Минимальная версия Python, которую поддерживает ваш пакет
)