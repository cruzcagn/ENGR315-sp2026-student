"""
For investments over $1M it can be typically assumed that they will return 5% forever.
Using the [2022 - 2023 JMU Cost of Attendance](https://www.jmu.edu/financialaid/learn/cost-of-attendance-undergrad.shtml),
calculate how much a rich alumnus would have to give to pay for one full year (all costs) for an in-state student
and an out-of-state student. Store your final answer in the variables: "in_state_gift" and "out_state_gift".

Note: this problem does not require the "compounding interest" formula from the previous problem.

"""

### Dukes Unleashed Assignment (G.Cruz-Candido ENGR 315) ###

# Cost of Attendance of at JMU for 2022-2023
in_state_cost = 30792
out_state_cost = 47882

# Amount of money alumns would have to spend to cover one year of tuition
# _state_cost / _state_gift = 5% #
in_state_gift = in_state_cost / 0.05
out_state_gift = out_state_cost / 0.05

print("In-state gift needed:", in_state_gift)
print("Out-state gift needed:", out_state_gift)