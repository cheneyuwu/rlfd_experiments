from copy import deepcopy
from rlfd.params.gan import gym_mujoco_params

params_config = deepcopy(gym_mujoco_params)

params_config["config"] = ("GAN", )

params_config["env_name"] = "walker2d-medium-v0"
# Tuned values
params_config["seed"] = tuple(range(5))

# Exp 1 GAN
params_config["config"] = ("GAN", )

