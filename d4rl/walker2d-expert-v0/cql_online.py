from copy import deepcopy
from rlfd.params.cql_online import gym_mujoco_params

params_config = deepcopy(gym_mujoco_params)

params_config["env_name"] = "walker2d-expert-v0"

# Exp 1 CQL Online
params_config["config"] = ("walker-expert-cql-online-trial1", )
params_config["random_expl_num_cycles"] = (0, )
params_config["agent"]["pi_lr"] = (3e-5, 3e-4)
params_config["seed"] = tuple(range(5))