from copy import deepcopy
from rlfd.params.cql import gym_mujoco_params

params_config = deepcopy(gym_mujoco_params)

params_config["config"] = ("CQL", )

params_config["env_name"] = "hopper-expert-v0"
# Tuned values
params_config["seed"] = tuple(range(5))

# # Exp 1 CQL
# params_config["config"] = ("CQL", )
# params_config["agent"]["cql_tau"] = 5.0

# # Exp 2 Parameter Search
# params_config["config"] = ("CQL_GridSearch",)
# params_config["agent"]["cql_tau"] = (1.0, 2.0, 10.0, 20.0)
# params_config["agent"]["auto_cql_alpha"] = (True,)

# Exp 2 Parameter Search 2
params_config["config"] = ("CQL_GridSearch2", )
params_config["agent"]["cql_tau"] = 1.0
params_config["agent"]["auto_cql_alpha"] = True
params_config["agent"]["auto_alpha"] = (False, )
params_config["agent"]["alpha"] = (0.1, 1.0, 2.0, 10.0)