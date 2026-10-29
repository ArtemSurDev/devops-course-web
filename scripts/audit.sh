echo "[4] Веб-сервер"
check "Служба nginx активна" "active" "$(systemctl is-active nginx)"

sudo nginx -t >/dev/null 2>&1; rc=$?
check "Конфигурация nginx корректна" "0" "$rc"

openssl x509 -checkend $((30*86400)) -noout -in /etc/ssl/certs/devops.crt >/dev/null 2>&1; rc=$?
check "Сертификат действителен не менее 30 дней" "0" "$rc"

check "В каталоге ресурса нет файлов, доступных для записи всем" "0" "$(sudo find /var/www/devops-site -perm -o+w | wc -l)"

check "Права закрытого ключа равны 600" "600" "$(sudo stat -c '%a' /etc/ssl/private/devops.key)"
