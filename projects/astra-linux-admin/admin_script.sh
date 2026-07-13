#!/bin/bash

check_services() {
    echo "=== проверка сервисов ==="
    systemctl list-units --type=service --state=running
}

check_network() {
    echo "=== проверка сети ==="
    ip addr show
    echo "---"
    ping -c 4 8.8.8.8
}

check_users() {
    echo "=== пользователи системы ==="
    cat /etc/passwd | grep -v nologin | grep -v false
}

check_disk() {
    echo "=== использование диска ==="
    df -h
}

check_logs() {
    echo "=== последние записи в логах ==="
    journalctl -n 20 --no-pager
}

main() {
    echo "запуск диагностики системы astra linux"
    echo "дата: $(date)"
    echo "---"
    check_services
    echo "---"
    check_network
    echo "---"
    check_users
    echo "---"
    check_disk
    echo "---"
    check_logs
    echo "---"
    echo "диагностика завершена"
}

main
