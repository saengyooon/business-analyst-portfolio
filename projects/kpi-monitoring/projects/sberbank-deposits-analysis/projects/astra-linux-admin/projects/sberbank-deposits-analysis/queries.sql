select
    product_name,
    count(*) as total_accounts,
    sum(balance) as total_balance,
    avg(interest_rate) as avg_rate,
    min(open_date) as first_deposit,
    max(open_date) as last_deposit
from deposits
where status = 'active'
group by product_name
order by total_balance desc;

select
    date_trunc('month', transaction_date) as month,
    sum(case when transaction_type = 'deposit' then amount else 0 end) as inflow,
    sum(case when transaction_type = 'withdrawal' then amount else 0 end) as outflow,
    sum(case
        when transaction_type = 'deposit' then amount
        else -amount
    end) as net_flow
from deposit_transactions
where transaction_date >= '2024-01-01'
group by date_trunc('month', transaction_date)
order by month;

select
    client_id,
    count(*) as num_deposits,
    sum(balance) as total_balance,
    avg(balance) as avg_balance
from deposits
group by client_id
having sum(balance) > 100000
order by total_balance desc
limit 10;

select
    product_name,
    sum(balance * interest_rate / 100) as yearly_income,
    avg(case
        when maturity_date is not null
        then balance * interest_rate / 100
    end) as avg_income
from deposits
where status = 'active'
group by product_name
order by yearly_income desc
