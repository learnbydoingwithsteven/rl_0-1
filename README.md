# Rl 0 1

A high-quality workspace folder project named Rl 0 1, built using various technologies and focused on workspace folder concepts with rich metadata.

---


## 📦 Project Structure

```text
rl_0-1/
├── project.meta.json
├── projects.index.json
├── rl_courses/
  ├── COMPLETION_REPORT.md
  ├── DEMO_VERIFICATION.md
  ├── GENERATION_GUIDE.md
  ├── PROJECT_STATUS.md
  ├── README.md
  ├── batch_generate.py
  ├── course_001_intro_to_rl/
  ├── course_001_introduction_to_reinforcement_learning/
  ├── course_001_introduction_to_rl/
  ├── course_002_agent_environment/
  ├── course_002_agent_environment_interaction/
  ├── course_003_markov_decision_processes/
  ├── course_004_rewards_and_returns/
  ├── course_005_policies_and_value_functions/
  ├── course_006_bellman_equations/
  ├── course_007_optimal_policies/
  ├── course_008_multi_armed_bandits/
  ├── course_008_multi_armed_bandits_intro/
  ├── course_009_epsilon_greedy/
  ├── course_009_epsilon_greedy_strategy/
  ├── course_010_upper_confidence_bound/
  ├── course_011_thompson_sampling/
  ├── course_012_contextual_bandits/
  ├── course_013_finite_mdps/
  ├── course_014_discount_factor/
  ├── course_015_state_value_functions/
  ├── course_016_action_value_functions/
  ├── course_017_policy_evaluation/
  ├── course_018_policy_improvement/
  ├── course_019_policy_iteration/
  ├── course_020_value_iteration/
  ├── course_021_dynamic_programming/
  ├── course_021_dynamic_programming_basics/
  ├── course_022_generalized_policy_iteration/
  ├── course_023_asynchronous_dp/
  ├── course_024_gridworld/
  ├── course_024_gridworld_environment/
  ├── course_025_cliff_walking/
  ├── course_025_cliff_walking_problem/
  ├── course_026_frozen_lake/
  ├── course_026_frozen_lake_problem/
  ├── course_027_taxi_problem/
  ├── course_028_model_based_vs_model_free/
  ├── course_029_exploration_vs_exploitation/
  ├── course_030_beginner_review/
  ├── course_031_monte_carlo_methods/
  ├── course_032_first_visit_mc/
  ├── course_032_first_visit_monte_carlo/
  ├── course_033_every_visit_mc/
  ├── course_033_every_visit_monte_carlo/
  ├── course_034_mc_control/
  ├── course_034_monte_carlo_control/
  ├── course_035_on_policy_vs_off_policy/
  ├── course_036_temporal_difference/
  ├── course_036_temporal_difference_learning/
  ├── course_037_td0/
  ├── course_037_td0_algorithm/
  ├── course_038_sarsa/
  ├── course_038_sarsa_algorithm/
  ├── course_039_q_learning/
  ├── course_039_q_learning_algorithm/
  ├── course_040_expected_sarsa/
  ├── course_041_double_q_learning/
  ├── course_042_n_step_td/
  ├── course_042_n_step_td_methods/
  ├── course_043_td_lambda/
  ├── course_044_forward_view_td_lambda/
  ├── course_045_backward_view_td_lambda/
  ├── course_046_function_approximation/
  ├── course_047_linear_approximation/
  ├── course_047_linear_function_approximation/
  ├── course_048_feature_engineering/
  ├── course_049_tile_coding/
  ├── course_050_radial_basis_functions/
  ├── course_051_coarse_coding/
  ├── course_052_semi_gradient_td/
  ├── course_053_linear_td/
  ├── course_053_linear_td_approximation/
  ├── course_054_convergence_of_td/
  ├── course_054_td_convergence/
  ├── course_055_deadly_triad/
  ├── course_055_deadly_triad_problem/
  ├── course_056_experience_replay/
  ├── course_057_prioritized_replay/
  ├── course_058_target_networks/
  ├── course_059_batch_rl/
  ├── course_059_batch_rl_methods/
  ├── course_060_intermediate_review/
  ├── course_061_deep_q_networks/
  ├── course_062_dqn_architecture/
  ├── course_063_double_dqn/
  ├── course_064_dueling_dqn/
  ├── course_065_rainbow_dqn/
  ├── course_066_policy_gradient_methods/
  ├── course_066_policy_gradients/
  ├── course_067_reinforce/
  ├── course_067_reinforce_algorithm/
  ├── course_068_policy_gradient_theorem/
  ├── course_069_baseline_methods/
  ├── course_070_actor_critic/
  ├── course_070_actor_critic_methods/
  ├── course_071_a2c/
  ├── course_071_advantage_actor_critic/
  ├── course_072_a3c/
  ├── course_072_a3c_algorithm/
  ├── course_073_trpo/
  ├── course_073_trust_region_policy_optimization/
  ├── course_074_ppo/
  ├── course_074_proximal_policy_optimization/
  ├── course_075_deterministic_gradients/
  ├── course_075_deterministic_policy_gradients/
  ├── course_076_ddpg/
  ├── course_076_deep_deterministic_policy_gradient/
  ├── course_077_td3/
  ├── course_077_twin_delayed_ddpg/
  ├── course_078_sac/
  ├── course_078_soft_actor_critic/
  ├── course_079_maximum_entropy_rl/
  ├── course_080_continuous_action_spaces/
  ├── course_080_continuous_actions/
  ├── course_081_hierarchical_rl/
  ├── course_082_options_framework/
  ├── course_083_intrinsic_motivation/
  ├── course_084_reward_shaping/
  ├── course_085_advanced_review/
  ├── course_086_model_based_rl/
  ├── course_087_world_models/
  ├── course_088_dyna/
  ├── course_088_dyna_architecture/
  ├── course_089_mcts/
  ├── course_089_monte_carlo_tree_search/
  ├── course_090_alphago/
  ├── course_090_alphago_and_alphazero/
  ├── course_091_multi_agent_rl/
  ├── course_092_competitive_marl/
  ├── course_092_competitive_multi_agent_rl/
  ├── course_093_meta_learning/
  ├── course_094_transfer_learning/
  ├── course_094_transfer_learning_in_rl/
  ├── course_095_inverse_rl/
  ├── course_096_imitation_learning/
  ├── course_097_safe_rl/
  ├── course_098_offline_rl/
  ├── course_099_real_world_applications/
  ├── course_099_real_world_rl/
  ├── course_100_future_directions/
  ├── course_manifest.json
  ├── courses_data.js
  ├── create_all_courses.py
  ├── index.html
  ├── project.meta.json
  ├── shared/
  ├── template/
```

## 🛠️ Technology Stack

- **General Documentation & Source Files**


## 🚀 Quick Start

1. Clone or navigate to the repository.
2. Explore the file structure listed above to find entry points.
3. Review the source files to learn by doing!