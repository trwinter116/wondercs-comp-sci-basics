# %%
def final_amt(p, r, n, t):
    """
    Apply the compound interest formula to p
    to produce the final amount.
    """

    return p * (1 + r / n) ** (n * t)


def final_amt_v2(principalAmount, nominalPercentageRate, numTimesPerYear, years):
    return principalAmount * (1 + nominalPercentageRate / numTimesPerYear) ** (
        numTimesPerYear * years
    )


def final_amt_v3(amt, rate, compounded, years):
    return amt * (1 + rate / compounded) ** (compounded * years)


to_invest = float(input("How much do you want to invest?"))
final_amount = final_amt(to_invest, 0.08, 12, 5)
print("At the end of the period you'll have", final_amount)
