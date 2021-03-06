from copy import deepcopy
from rlfd.params.cql import gym_mujoco_params

params_config = deepcopy(gym_mujoco_params)

params_config["config"] = ("CQL", )

params_config["env_name"] = "walker2d-expert-v0"
# Tuned values
params_config["seed"] = tuple(range(5))

# # Exp 1 CQL
params_config["config"] = ("CQL", )
params_config["agent"]["cql_tau"] = (1.0, 2.0, 5.0 10.0, 20.0)
params_config["agent"]["auto_cql_alpha"] = (True, )
