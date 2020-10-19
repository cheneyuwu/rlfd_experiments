from copy import deepcopy
from rlfd.params.cql_online import gym_mujoco_params

params_config = deepcopy(gym_mujoco_params)

params_config["config"] = ("hammer-demos-CQL-Online-trial1", )

params_config["env_name"] = "hammer-demos-v0"
# Tuned values
params_config["seed"] = tuple(range(5))

# Exp 1 CQL Online
params_config["agent"]["cql_tau"] = (5.0) #1 did not work for plain CQL
params_config["agent"]["online_sample_ratio"] = 0.5
params_config["agent"]["cql_weight_decay_factor"] = 0.9999
params_config["seed"] = tuple(range(5))