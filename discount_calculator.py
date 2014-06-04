class DiscountCalculator(object):


  def calculate(self, total, discount_amount, discount_type):
    if discount_type=='percent':
        if discount_amount >= 100:
            raise ValueError("Percent discount cannot be more than 100%")

        percentage_discount = float(discount_amount) / 100
        discount = float(total) * percentage_discount

    elif discount_type=='absolute':
        if discount_amount>=total:
            raise ValueError("Absolute discount cannot be more than total")
        discount=discount_amount

    else:
        raise ValueError("invalid Discount")

    return discount