def generateReport2():
    return "inside gr"

def generateReport(number_of_months, total_profit, average_change_in_monthly_profit,
                  best_monthly_change_month, best_monthly_change_value,
                  worst_monthly_change_month, worst_monthly_change_value):
    return [
        "Financial Analysis",
        "----------------------------",
        "Total Months: %i" % number_of_months,
        "Total: $%.2f" % total_profit,
        "Average  Change: $%.2f" % average_change_in_monthly_profit,
        "Greatest Increase in Profits: %s ($%.2f)" % (best_monthly_change_month, best_monthly_change_value),
        "Greatest Decrease in Profits: %s ($%.2f)"% (worst_monthly_change_month, worst_monthly_change_value)
    ]
