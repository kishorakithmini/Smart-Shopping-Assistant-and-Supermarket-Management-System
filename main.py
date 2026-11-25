    print('{:<8} {:<23} {:>6} {:>17} {:>17}'.format(
        'ID', 'Product', 'Qty', 'Unit price', 'Item total'))
    print('-' * 78)
    for item in cart:
        product = products[find_product(item[0])]
        item_total = calculate_item_total(product[3], item[1])
        print('{:<8} {:<23} {:>6} {:>17} {:>17}'.format(
            product[0], product[1], item[1], money(product[3]), money(item_total)))
    print('-' * 78)
    print('Total bill:', money(calculate_bill(cart)))
    print('-' * 78)


# Cancel without changing stock or sales.
def cancel_purchase(cart):
    if len(cart) == 0:
        print('Your shopping cart is empty.')
    else:
        cart.clear()
        print('Purchase cancelled. Stock and sales are unchanged.')


# Reduce stock only after the entire cart is validated and confirmed.
def reduce_stock(cart):
    for item in cart:
        index = find_product(item[0])
        products[index][4] = products[index][4] - item[1]


# Generate a simple receipt for a completed purchase.
def generate_receipt(cart):
    print('\n========== SUPERMARKET RECEIPT ==========')
    print('Receipt number:', len(sales))
    display_bill(cart)
    print('Payment status: Confirmed')
    print('Thank you for shopping with us!')


# Confirm or cancel the entire purchase.
def checkout(cart):
    if len(cart) == 0:
        print('Your shopping cart is empty.')
        return

    # Recheck every item before changing any stock.
    for item in cart:
        if not validate_stock(item[0], item[1]):
            print('Insufficient stock for', item[0], '- purchase not completed.')
            return

    print('\n========== CHECKOUT ==========')
    display_bill(cart)
    while True:
        answer = input('Confirm purchase? (Y/N): ').strip().upper()
        if answer == 'Y':
            total = calculate_bill(cart)
            reduce_stock(cart)
            sales.append(total)
            generate_receipt(cart)
            cart.clear()
            return
        elif answer == 'N':
            cancel_purchase(cart)
            return
        else:
            print('Please enter Y or N.')


# Only confirmed purchases are recorded in the sales list.
def sales_report():
    revenue = 0
    for amount in sales:
        revenue = revenue + amount
    print('\n========== SALES REPORT ==========')
    print('Completed purchases:', len(sales))
    print('Total revenue:', money(revenue))
    print('=' * 34)


# ==================================================
# 06. MAIN PROGRAM
# ==================================================

def main():
    while True:
        print('\n====== SMART SHOPPING ASSISTANT ======')
        print('1. Customer Portal')
        print('2. Officer Portal')
        print('3. Exit')
        choice = input('Enter your choice: ').strip()

        if choice == '1':
            customer_portal()
        elif choice == '2':
            officer_portal()
        elif choice == '3':
            print('Thank you. Goodbye!')
            return
        else:
            print('Invalid menu choice. Please try again.')


main()
