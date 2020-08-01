from copy import deepcopy
from rlfd.params.sac import gym_mujoco_params

params_config = deepcopy(gym_mujoco_params)

params_config["config"] = ("SAC", )

params_config["env_name"] = "halfcheetah-medium-v0"
# Tuned values
params_config["seed"] = tuple(range(5))
