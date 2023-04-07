from DynamicBRB import BRBModel, ModelType
"""
Created on Fri Apr  7 15:30:03 2023

@author: snzisad
"""


inputs = [0.8, 0.6, 0.4]

"""
Disjunctive BRB
"""

dij_rule_base = [1, 0, 0, 0, 1, 0, 0, 0, 1]

brb = BRBModel(modelType = ModelType.DISJUNCTIVE_BRB, num_ant_attr = 3, num_ref_values = 3, isDebug = True)

brb.setRefValues(ref_value_list = [[1, 0.5, 0], [1, 0.5, 0], [1, 0.5, 0]])
brb.setIntitalWeights(relative_weight_list = [1]*3, rule_weight_list = [1]*3)
brb.setUtilityScore(utility_score_list = [1, 0.5, 0])
brb.setRuleBase(rule_base_list = dij_rule_base)

crisp_val = brb.runBRB(inputs)
print(crisp_val)

"""
Conjunctive BRB
"""

conj_rule_base = [1.0, 0.0, 0.0, 0.8, 0.2, 0.0, 0.8, 0.0, 0.2, 0.6, 0.4, 0.0, 0.4, 0.6, 0.0, 0.5, 0.3, 0.2, 0.8, 0.0, 0.2, 0.5, 0.3, 0.2, 0.2, 0.0, 0.8, 0.8, 0.2, 0.0, 0.4, 0.6, 0.0, 0.5, 0.3, 0.2, 0.4, 0.6, 0.0, 0.0, 1.0, 0.0, 0.0, 0.8, 0.2, 0.5, 0.3, 0.2, 0.0, 0.8, 0.2, 0.0, 0.2, 0.8, 0.8, 0.0, 0.2, 0.5, 0.3, 0.2, 0.2, 0.0, 0.8, 0.5, 0.3, 0.2, 0.0, 0.8, 0.2, 0.0, 0.2, 0.8, 0.2, 0.0, 0.8, 0.0, 0.2, 0.8, 0.0, 0.0, 1.0]

brb = BRBModel(modelType = ModelType.CONJUNCTIVE_BRB, num_ant_attr = 3, num_ref_values = 3, isDebug = True)

brb.setRefValues(ref_value_list = [[1, 0.5, 0], [1, 0.5, 0], [1, 0.5, 0]])
brb.setIntitalWeights(relative_weight_list = [1]*3, rule_weight_list = [1]*27)
brb.setUtilityScore(utility_score_list = [1, 0.5, 0])
brb.setRuleBase(rule_base_list = conj_rule_base)

crisp_val = brb.runBRB(inputs)
print(crisp_val)

