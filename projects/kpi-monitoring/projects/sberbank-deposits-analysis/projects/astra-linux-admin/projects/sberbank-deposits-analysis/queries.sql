-- ============================================
-- Анализ депозитных продуктов Сбербанка
-- Автор: Арина
-- ============================================

-- 1. Общая статистика по активным депозитам
SELECT 
    product_name AS "Название продукта",
    COUNT(*) AS "Количество счетов",
    SUM(balance) AS "Общий баланс",
    AVG(interest_rate) AS "Средняя ставка %",
    MIN(open_date) AS "Первый депозит",
    MAX(open_date) AS "Последний депозит"
FROM deposits
WHERE status = 'active'
GROUP BY product_name
ORDER BY SUM(balance) DESC;

-- 2. KPI: Приток и отток средств по месяцам
SELECT 
    DATE_TRUNC('month', transaction_date) AS "Месяц",
    SUM(CASE WHEN transaction_type = 'deposit' THEN amount ELSE 0 END) AS "Приток",
    SUM(CASE WHEN transaction_type = 'withdrawal' THEN amount ELSE 0 END) AS "Отток",
    SUM(CASE 
        WHEN transaction_type = 'deposit' THEN amount 
        ELSE -amount 
    END) AS "Чистый поток"
FROM deposit_transactions
WHERE transaction_date >= '2024-01-01'
GROUP BY DATE_TRUNC('month', transaction_date)
ORDER BY "Месяц";

-- 3. Топ-10 клиентов по объёму депозитов
SELECT 
    client_id AS "ID клиента",
    COUNT(*) AS "Кол-во депозитов",
    SUM(balance) AS "Общий баланс",
    AVG(balance) AS "Средний баланс"
FROM deposits
GROUP BY client_id
HAVING SUM(balance) > 100000
ORDER BY SUM(balance) DESC
LIMIT 10;

-- 4. Анализ доходности продуктов
SELECT 
    product_name AS "Продукт",
    SUM(balance * interest_rate / 100) AS "Годовой доход",
    AVG(CASE 
        WHEN maturity_date IS NOT NULL 
        THEN balance * interest_rate / 100 
    END) AS "Средний доход по продукту"
FROM deposits
WHERE status = 'active'
GROUP BY product_name
ORDER BY "Годовой доход" DESC;
