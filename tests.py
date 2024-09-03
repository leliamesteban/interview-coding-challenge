from challenge1 import challenge1
from challenge2 import challenge2
from challenge3 import challenge3

assert challenge1("ADDZ", "CDDY", "UDDF") == "DD"
assert challenge1("UIBAZDBSIAHFB", "PQACIZDBIBDLAG", "QIDBCZDBKSHDVF") == "ZDB"

assert challenge2("05/05/2024 8:30AM") == "2024-05-05T08:30:00Z"
assert challenge2("12/31/2023 11:59PM") == "2023-12-31T23:59:00Z"

assert challenge3(["y", "y", "b", "b", "g", "g"]) == 1
assert challenge3(["y", "y", "b", "b", "g"]) == 0
assert challenge3(["y", "b", "g", "g", "b", "y"]) == 3
