from DynamicBRB import BRBModel, ModelType
import matplotlib.pyplot as plt
import numpy as np
  
  

"""
Created on Fri Apr  7 15:30:03 2023

@author: snzisad
"""



"""
BRB for Explainability
"""

rule_base = [1, 0, 0, 0, 1, 0, 0, 0, 1]

brb = BRBModel(modelType = ModelType.DISJUNCTIVE_BRB, num_ant_attr = 3, num_ref_values = 3, isDebug = False)

brb.setRefValues(ref_value_list = [[1, 0.5, 0], [1, 0.5, 0], [1, 0.5, 0]])
brb.setIntitalWeights(relative_weight_list = [1]*3, rule_weight_list = [1]*3)
brb.setUtilityScore(utility_score_list = [1, 0.5, 0])
brb.setRuleBase(rule_base_list = rule_base)

explainability_score = brb.runBRB(input_list = [1.0, 18.13, 7.67])
print("Explainability Score: "+str(explainability_score))



"""
BRB for accuracy
"""

rule_base = [1, 0, 0, 0, 1, 0, 0, 0, 1]

brb = BRBModel(modelType = ModelType.DISJUNCTIVE_BRB, num_ant_attr = 2, num_ref_values = 3, isDebug = False)

brb.setRefValues(ref_value_list = [[100, 50, 0], [100, 50, 0]])
brb.setIntitalWeights(relative_weight_list = [1]*2, rule_weight_list = [1]*3)
brb.setUtilityScore(utility_score_list = [1, 0.5, 0])
brb.setRuleBase(rule_base_list = rule_base)

accuracy_score = brb.runBRB(input_list = [42.27, 59.49])
print("Accuracy Score: "+str(accuracy_score))




"""
BRB for combination
"""

rule_base = [1, 0, 0, 0, 1, 0, 0, 0, 1]

brb = BRBModel(modelType = ModelType.DISJUNCTIVE_BRB, num_ant_attr = 2, num_ref_values = 3, isDebug = False)

brb.setRefValues(ref_value_list = [[1, 0.5, 0], [1, 0.5, 0]])
brb.setIntitalWeights(relative_weight_list = [1]*2, rule_weight_list = [1]*3)
brb.setUtilityScore(utility_score_list = [1, 0.5, 0])
brb.setRuleBase(rule_base_list = rule_base)

balance_score = brb.runBRB(input_list = [explainability_score, accuracy_score])
print("Balance Score: "+str(balance_score))


"""
Plot the balance
"""
plt.plot([0, balance_score], [1, 1], linestyle='-', marker='o', color='red', label='Distance from Accuracy')
plt.plot([0.5, balance_score], [1, 1], linestyle='--', marker='p', color='green', label='Distance from Standard')
plt.plot([balance_score, 1], [1, 1], linestyle='-', marker='o', color='blue', label='Distance from Explainability')
plt.plot([0.5, 0.5], [1, 1], linestyle='--', marker='p', color='green', label='Standard Value')
plt.legend()
plt.show()




