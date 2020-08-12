from copy import deepcopy
from rlfd.params.nf import gym_mujoco_params

params_config = deepcopy(gym_mujoco_params)

params_config["config"] = ("NF", )

params_config["env_name"] = "walker2d-expert-v0"
# Tuned values
params_config["seed"] = tuple(range(5))

# Exp 1 NF
params_config["config"] = ("NF", )
