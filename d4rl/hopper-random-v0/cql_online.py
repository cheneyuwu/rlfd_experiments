from copy import deepcopy
from rlfd.params.cql_online import gym_mujoco_params

params_config = deepcopy(gym_mujoco_params)

params_config["env_name"] = "hopper-random-v0"
# Tuned values
params_config["seed"] = tuple(range(5))

# Exp 1 CQL Online with Tuning
params_config["config"] = ("hopper-random-cql-online-trail1", )
params_config["agent"]["cql_tau"] = (1.0)
params_config["agent"]["cql_weight_decay_factor"] = 0.9999
params_config["seed"] = tuple(range(5))