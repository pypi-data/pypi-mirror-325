from dataclasses import dataclass

from envquest.agents.common import EpsilonDecay


@dataclass
class EnvArguments:
    task: str = "CartPole-v1"
    max_episode_length: int = 1000


@dataclass
class LoggingArguments:
    wandb_enabled: bool = True
    project_name: str = "envquest"
    exp_id: str = None
    render_width: int = 256
    render_height: int = 256
    save_train_videos: bool = False
    log_eval_videos: bool = True
    save_eval_videos: bool = True
    save_agent_snapshots: bool = True


@dataclass
class TrainerArguments:
    # Training
    batch_size: int = 64
    num_train_steps: int = 1000000
    num_seed_steps: int = 5000
    num_updates: int = 1
    update_every_steps: int = 1

    # Evaluation
    num_eval_episodes: int = 5
    eval_every_steps: int = 10000


@dataclass
class MCTrainerArguments(TrainerArguments):
    num_train_trajectories: int = 5


@dataclass
class AgentArguments:
    class_name: str = None
    discount: float = 0.99
    lr: float = 1e-4
    mem_capacity: int = 1000000


@dataclass
class PPOAgentArguments(AgentArguments):
    class_name: str = "ppo"
    clip_eps: float = 0.2
    num_policy_updates: int = 5


@dataclass
class DQNAgentArguments(AgentArguments):
    class_name: str = "dqn"
    n_steps: int = 6
    tau: float = 0.005

    eps_start: float = 0.95
    eps_end: float = 0.05
    eps_step_duration: int = 100000
    eps_decay: str = EpsilonDecay.EXPONENTIAL  # "linear" or "exponential"


@dataclass
class SarsaAgentArguments(AgentArguments):
    class_name: str = "sarsa"

    eps_start: float = 0.95
    eps_end: float = 0.05
    eps_step_duration: int = 100000
    eps_decay: str = EpsilonDecay.EXPONENTIAL  # "linear" or "exponential"


@dataclass
class TrainingArguments:
    env: EnvArguments = EnvArguments()
    agent: AgentArguments = None
    trainer: TrainerArguments = TrainerArguments()
    logging: LoggingArguments = LoggingArguments()
