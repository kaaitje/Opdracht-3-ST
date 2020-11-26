from money_model import MoneyModel
import matplotlib.pyplot as plt

model = MoneyModel(50, 10, 10)
for i in range(100):
    model.step()

gini = model.datacollector.get_model_vars_dataframe()
gini.plot()
plt.show()
