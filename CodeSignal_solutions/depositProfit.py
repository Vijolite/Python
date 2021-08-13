#You have deposited a specific amount of money into your bank account. Each year your balance increases at the same growth rate. With the assumption that you don't make any additional deposits, find out how long it would take for your balance to pass a specific threshold.

def depositProfit(deposit, rate, threshold):
    money=deposit
    years=0
    while money<threshold:
        money=money*(100+rate)/100
        years+=1
    return years
