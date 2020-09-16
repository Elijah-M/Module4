"""
Author: Elijah Morishita
elmorishita@dmacc.edu
9/14/2020
This is the Nested if Assignment, which gathers a user's input
of price, case coupon, and % coupon, calculates the total, and
prints the total with taxes (6%) and shipping.
"""

#  Title
print("\n========== SuperAwesomeCouponDealsAndStuff.com ==========\n")

def calculate_price(price, cash_coupon, percent_coupon):
    """A function to calculate the total based on user input"""
    TEN = 10; THIRTY = 30; FIFTY = 50; TAX = 0.06

    #  calculating pre-tax cost after discounts
    pre_percent_total = price - cash_coupon
    post_percent_total = pre_percent_total * percent_coupon
    pre_tax_total = pre_percent_total - post_percent_total

    #  calculating the total tax to add after shipping
    tax_total = pre_tax_total * TAX

    #  calculating shipping cost
    if pre_tax_total <= TEN:
        shipping_price = 5.95
    elif TEN < pre_tax_total <= THIRTY:
        shipping_price = 7.95
    elif THIRTY < pre_tax_total <= FIFTY:
        shipping_price = 11.95
    elif FIFTY < pre_tax_total:
        shipping_price = 0.00

    #  calculates pre-tax, tax, and shipping together
    total_cost = pre_tax_total + tax_total + shipping_price

    print(" Sub-total:", pre_tax_total, "\n",
          "Taxes:", tax_total, "\n",
          "Shipping:", shipping_price, "\n",
          "Grand Total:", total_cost)

    return total_cost #  return is only for the sake of testing

if __name__ == '__main__':

    #  Gather the price, case_coupon, and percent_coupon
    price = float(input(" Please enter the your price: "))
    cash_coupon = float(input(" Please enter the your cash coupon: "))
    percent_coupon = float(input(" Please enter the your percent coupon: "))

    #  Spacing
    print("========================================================")

    #  Calculates the total
    calculate_price(price, cash_coupon, percent_coupon)