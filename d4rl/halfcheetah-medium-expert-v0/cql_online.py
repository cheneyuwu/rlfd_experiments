from copy import deepcopy
from rlfd.params.cql_online import gym_mujoco_params

params_config = deepcopy(gym_mujoco_params)

params_config["env_name"] = "halfcheetah-medium-expert-v0"
# Tuned values
params_config["seed"] = tuple(range(5))

# Exp 1 CQL Online (Copied the params from SAC and CQL halfcheetah medium trial 1, which went well)
params_config["config"] = ("halfcheetah-medium-expert-CQL-online_trial1", )
params_config["agent"]["cql_tau"] = (1.0)
params_config["seed"] = tuple(range(5))
