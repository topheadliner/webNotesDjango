# django project
При создании проекта на Django, первый шаг это создание виртуального окружения командой

  python3 -m venv venvName
  
Активируем виртуалку и установим фреймворк дженго:
  
  source venvName/bin/activate
  
  pip3 install Django

Теперь создаем директорий нашего нового проекта в дженго, добавляем модели и создаем суперадмина:
  
  django-admin startproject projectName
  
  cd projectName
  
  ./manage.py migrate
  
  ./manage.py createsuperuser

Мы готовы создавать свой веб-проект на дженго
  
  
