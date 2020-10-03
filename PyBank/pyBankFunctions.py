def generateReport():
    return "inside gr"
def generateReport(numMonths, profit_total, averageMonthlyProfit):
    return [
        "Financial Analysis",
        "----------------------------",
        "Total Months: %i" % numMonths,
        "Total: $%.2f" % profit_total,
        "Average  Change: $%.2f" % averageMonthlyProfit,
        "Greatest Increase in Profits: %s ($%.2f)" % (maxMonthlyProfitabilityMonth, maxMonthlyProfitability),
        "Greatest Decrease in Profits: %s ($%.2f)"% (minMonthlyProfitabilityMonth, minMonthlyProfitability)
    ]
