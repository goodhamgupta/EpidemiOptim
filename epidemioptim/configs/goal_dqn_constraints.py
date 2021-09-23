import numpy as np


params = dict(
    expe_name="",
    trial_id=0,
    env_id="EpidemicDiscrete-v0",
    seed=int(np.random.randint(1e6)),
    num_train_steps=1e6,
    simulation_horizon=364,
    algo_id="DQN",
    algo_params=dict(
        eval_and_log_every=50,
        save_policy_every=1000,
        batch_size=32,
        gamma=0.99,
        layers=(64,),
        replace_target_count=5000,
        goal_conditioned=True,
        lr=1e-3,
        buffer_size=1e6,
        epsilon_greedy=0.2,
        n_evals_if_stochastic=30,
        pareto_size=100,
    ),
    model_id="prague_seirah",
    model_params=dict(region="IDF", stochastic=True),
    cost_id="multi_cost_death_gdp_controllable",
    cost_params=dict(
        N_region=10 * 1e6,
        N_country=60 * 1e6,
        ratio_death_to_R=0.005,
        use_constraints=True,
    ),
)
