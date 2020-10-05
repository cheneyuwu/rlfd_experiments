from copy import deepcopy
from rlfd.params.cql import gym_mujoco_params

params_config = deepcopy(gym_mujoco_params)

params_config["config"] = ("CQL", )

params_config["env_name"] = "hopper-medium-v0"
# Tuned values
params_config["seed"] = tuple(range(5))

# # Exp 1 CQL
# params_config["config"] = ("CQL", )

# # Exp2 Parameter Search
# params_config["config"] = ("CQL_GridSearch2",)
# params_config["agent"]["cql_log_alpha"] = (1.0, 1.5, 2.0, 5.0)
# params_config["agent"]["auto_cql_alpha"] = (False,)

# Exp3 Parameter Search
params_config["config"] = ("hopper-medium-cql-trial1-alpha-lr", )
params_config["agent"]["cql_tau"] = (1.0)
params_config["agent"]["cql_alpha_lr"] = (3e-4, 1e-5, 1e-3, 5e-4)
params_config["agent"]["auto_cql_alpha"] = (True)
