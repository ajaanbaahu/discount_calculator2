class DiscountCalculator(object):


  def calculate(self, total, discount_amount, discount_type):
    if discount_type=='percent':
        percentage_discount = float(discount_amount) / 100
        discount = float(total) * percentage_discount

    elif discount_type=='absolute':
        discount=discount_amount

    else:
        raise ValueError("invalid Discount")

    return discount