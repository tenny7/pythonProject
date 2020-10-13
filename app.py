from ecommerce.utils import dollar_to_naira
from ecommerce.utils import naira_to_dollar
from pathlib import Path

path = Path()
for file in path.glob("*.py"):
    print(file)
# print(path.glob("*.*"))
# dollar_to_naira(30000)
# naira_to_dollar(500000)
