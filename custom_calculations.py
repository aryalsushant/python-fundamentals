# monthly expenses and revenues over course of year
expenses = [40000., 42500., 47000., 40500., 38000., 36000., 39500., 43000., 47000., 48500., 49000., 50000.]
revenues = [38000., 42500., 52000., 50000., 48000., 43000., 44500., 45000., 50000., 49500., 52000., 54000.]
monthly_gross = [revenues[i]-expenses[i] for i in range(12)]

def mean(x):
    """
    return the mean value of the elements in x
    by summing the elements and dividing by the length;
    if the input type does not support this, 
    return the input itself
    """
    try:
        return sum(x)/len(x)
    except TypeError:
        return x

def compute_quarterly_figures(expenses, revenues):
    quarterlies = {}
    for quarter in [1,2,3,4]:
        start = (quarter - 1)*3
        end = start + 3
        total_expenses_qtr = sum(expenses[start:end])
        mean_expenses = mean(expenses[start:end])
        total_revenues_qtr = sum(revenues[start:end])
        mean_revenues = mean(revenues[start:end])
        total_gross_qtr = total_revenues_qtr - total_expenses_qtr
        summary = 'Q{}: rev = {:.2f}, exp = {:.2f}, gross = {:.2f}'
        summary_line = summary.format(
            quarter, mean_revenues, mean_expenses, total_gross_qtr)

        print(summary_line)

        quarterlies['Q{0}'.format(quarter)] = \
          (mean_revenues,mean_expenses, total_gross_qtr)
    return quarterlies