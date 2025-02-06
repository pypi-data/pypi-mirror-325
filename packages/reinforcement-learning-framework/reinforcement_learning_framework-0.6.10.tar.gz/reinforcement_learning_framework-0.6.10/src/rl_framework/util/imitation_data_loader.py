from typing import Iterable, List, Mapping, Union

import numpy as np
from imitation.data import types
from imitation.data.types import DictObs, stack_maybe_dictobs


def create_memory_efficient_transition_batcher(
    trajectories: Iterable[types.Trajectory], batch_size: int
) -> Iterable[types.TransitionMapping]:
    """
        Memory-efficient data loader. Converts a series of trajectories into individual transition batches.

    Args:
        trajectories: iterable of trajectories
        batch_size: number of transitions the data loader should yield per batch

    Yields:
        Batches of transitions in a dictionary format (with co-indexed elements per dictionary key)
        {
            "obs": np.ndarray,
            "next_obs": np.ndarray,
            "acts": np.ndarray,
            "dones": np.ndarray,
            "infos": np.ndarray,
        }
    """
    trajectory_part_keys = ["obs", "next_obs", "acts", "dones", "infos"]

    trajectory_as_dict_collected: Mapping[str, Union[np.ndarray, DictObs]] = {key: None for key in trajectory_part_keys}

    for traj in trajectories:
        assert isinstance(traj.obs, types.DictObs) or isinstance(traj.obs, np.ndarray)
        assert isinstance(traj.acts, np.ndarray)

        dones = np.zeros(len(traj.acts), dtype=bool)
        dones[-1] = traj.terminal

        infos = np.array([{}] * len(traj)) if traj.infos is None else traj.infos

        trajectory_as_dict = {
            "obs": traj.obs[:-1],
            "next_obs": traj.obs[1:],
            "acts": traj.acts,
            "dones": dones,
            "infos": infos,
        }

        if trajectory_as_dict_collected["dones"] is not None:
            trajectory_as_dict_collected = {
                k: types.concatenate_maybe_dictobs([trajectory_as_dict_collected[k], v])
                for k, v in trajectory_as_dict.items()
            }
        else:
            trajectory_as_dict_collected = trajectory_as_dict

        trajectory_part_lengths = set(map(len, trajectory_as_dict_collected.values()))
        assert len(trajectory_part_lengths) == 1, f"expected one length, got {trajectory_part_lengths}"

        if len(trajectory_as_dict_collected["dones"]) >= batch_size:
            transitions = types.Transitions(**trajectory_as_dict_collected)
            transitions_batches: List[List[types.Transitions]] = [
                transitions[i : i + batch_size] for i in range(0, len(transitions), batch_size)
            ]

            if len(transitions_batches[-1]) != batch_size:
                trajectory_as_dict_collected = {
                    k: v[-len(transitions_batches[-1]) :] for k, v in trajectory_as_dict.items()
                }
                transitions_batches = transitions_batches[:-1]
            else:
                trajectory_as_dict_collected = {key: None for key in trajectory_part_keys}

            for batch in transitions_batches:
                result = {
                    "obs": stack_maybe_dictobs([sample["obs"] for sample in batch]),
                    "next_obs": stack_maybe_dictobs([sample["next_obs"] for sample in batch]),
                    "acts": batch.acts,
                    "dones": batch.dones,
                    "infos": batch.infos,
                }
                yield result
