def bonAppetit(bill, k, b):
    bill.pop(k)
    total = sum(bill)
    if total // 2 == b:
        print('Bon Appetit')
    else:
        print(b - total // 2)

if __name__ == '__main__':
    bill = [3, 10, 2, 9]
    k = 1
    b = 12
    bonAppetit(bill, k, b) # 5
    bill = [3, 10, 2, 9]
    k = 1
    b = 7
    bonAppetit(bill, k, b) # Bon Appetit