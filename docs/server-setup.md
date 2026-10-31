## 8. Веб-сервер

- Пакет: nginx (версия 1.24.0). Установка: sudo apt update && sudo apt install -y nginx.
- Конфигурация ресурса: /etc/nginx/sites-available/devops-site, активируется ссылкой /etc/nginx/sites-enabled/devops-site. Ссылка стандартного ресурса /etc/nginx/sites-enabled/default удалена.
- Содержимое конфигурации: два блока server. Первый слушает порт 80 и выполняет return 301 https://$host$request_uri. Второй слушает порт 443 ssl, содержит пути к сертификату и ключу, root /var/www/devops-site, index index.html, location / { try_files $uri $uri/ =404; }, error_page 404 /404.html.
- Каталог ресурса: /var/www/devops-site, владелец devops:devops, права 755 для каталогов и 644 для файлов.
- Сертификат: самоподписанный, /etc/ssl/certs/devops.crt (владелец root, права 644); закрытый ключ /etc/ssl/private/devops.key (владелец root, права 600); срок действия 365 дней.
- Применение конфигурации: sudo nginx -t && sudo systemctl reload nginx.
- Межсетевой экран: порты 80/tcp и 443/tcp разрешены.
## 9. Контейнеризация
- Установка Docker Engine из официального репозитория. Версия: 29.9.2. Compose: v5.6.1.
- Участники группы docker: devops.
- Расположение проекта: /home/devops/app.
- Файл .env: /home/devops/app/.env, права 600.
- Публикуемые порты: 127.0.0.1:5000 (приложение). Порт 5432 не публикуется.
- Именованные тома: app_db_data.
- Конфигурация Nginx: location /app/ проксирует на http://127.0.0.1:5000/.
