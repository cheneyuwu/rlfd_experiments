from copy import deepcopy
from rlfd.params.sac import gym_mujoco_params

params_config = deepcopy(gym_mujoco_params)

params_config["config"] = ("SAC", )

params_config["env_name"] = "halfcheetah-medium-v0"
# Tuned values
params_config["seed"] = tuple(range(5))

# Exp 1 sac.
params_config["config"] = ("SAC", )

# # Exp 2 copy actor, critic and alpha from a pretrained cql agent: cql.pkl
# params_config["config"] = ("SAC_CQLPretrained", )
# params_config["agent"]["use_pretrained_critic"] = True
# params_config["agent"]["use_pretrained_actor"] = True
# params_config["agent"]["use_pretrained_alpha"] = True

# # Exp 3 copy actor, critic and alpha from a pretrained gan agent: gan.pkl
# params_config["config"] = ("SAC_GANPretrained", )
# params_config["agent"]["use_pretrained_critic"] = True
