from copy import deepcopy
from rlfd.params.cql_online import gym_mujoco_params

params_config = deepcopy(gym_mujoco_params)

params_config["env_name"] = "walker2d-medium-expert-v0"

# Exp 1 CQL Online
params_config["config"] = ("walker-medium-expert-cql-online-trial1", )

params_config["seed"] = tuple(range(5))