from copy import deepcopy
from rlfd.params.cql_online import gym_mujoco_params

params_config = deepcopy(gym_mujoco_params)

params_config["config"] = ("CQLOnline", )

params_config["env_name"] = "walker2d-medium-v0"
# Tuned values
params_config["seed"] = tuple(range(5))

# Exp 1 CQL Online
params_config["config"] = ("CQLOnline", )
params_config["agent"]["cql_tau"] = (0.0, 1.0, 5.0)
params_config["agent"]["online_sample_ratio"] = 0.5
params_config["agent"]["cql_weight_decay_factor"] = 0.9999
params_config["seed"] = tuple(range(5))
