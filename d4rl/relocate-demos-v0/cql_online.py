from copy import deepcopy
from rlfd.params.cql_online import gym_mujoco_params

params_config = deepcopy(gym_mujoco_params)

params_config["config"] = ("CQLOnline", )

params_config["env_name"] = "relocate-demos-v0"
# Tuned values
params_config["seed"] = tuple(range(5))

# Exp 1 CQL Online
params_config["config"] = ("relocate-demos-CQL-online-trial1", )
params_config["agent"]["cql_tau"] = (1.0) #Was 0 in cloned trial 1, didn't go so well
params_config["agent"]["online_sample_ratio"] = 0.5
params_config["agent"]["cql_weight_decay_factor"] = 0.9999 #Was 1 in cloned trial, maybe this will stabilize learning
params_config["agent"]["pi_lr"] =  (3e-5, )
params_config["seed"] = tuple(range(5))