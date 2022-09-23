OpsTypes = {"mono": 0, "dual": 1, "ternary": 2}

OpsDict = {}
OpsDict["add"] = {"type": OpsTypes["dual"], "value": 0}
OpsDict["sub"] = {"type": OpsTypes["dual"], "value": 1}
OpsDict["mult"] = {"type": OpsTypes["dual"], "value": 2}
OpsDict["div"] = {"type": OpsTypes["dual"], "value": 3}

OpsDescriptions = {}
OpsDescriptions["add"] = "addition operand"
OpsDescriptions["sub"] = "substraction operand"
OpsDescriptions["mult"] = "multiplication operand"
OpsDescriptions["div"] = "division operand"

