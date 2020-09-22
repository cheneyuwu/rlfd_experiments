from copy import deepcopy
from rlfd.params.sac_offline import gym_mujoco_params

params_config = deepcopy(gym_mujoco_params)

params_config["config"] = ("SACOffline", )

params_config["env_name"] = "walker2d-expert-v0"
# Tuned values
params_config["seed"] = tuple(range(5))

# Exp 1 sac offline.
params_config["config"] = ("SACOffline", )
params_config["agent"]["online_sample_ratio"] = 0.5
params_config["seed"] = tuple(range(5))
