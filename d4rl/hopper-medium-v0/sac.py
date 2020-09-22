from copy import deepcopy
from rlfd.params.sac import gym_mujoco_params

params_config = deepcopy(gym_mujoco_params)

params_config["config"] = ("SAC", )

params_config["env_name"] = "hopper-medium-v0"
# Tuned values
params_config["seed"] = tuple(range(5))

# # Exp 1 sac.
# params_config["config"] = ("SAC", )
# params_config["seed"] = tuple(range(5))

# Exp 2 sac with same parameters as cql online
params_config["config"] = ("SAC_Param", )
params_config["random_expl_num_cycles"] = (0, )
params_config["agent"]["pi_lr"] = (3e-5, )
params_config["seed"] = tuple(range(5))
