from pathlib import Path
import glob
import json
import pandas as pd
import matplotlib.pyplot as plt

"""
What is does: parses a trainer_state.json file in a checkpoint directory.
Purpose: to track training progress.
Usage:
from HFTrainerInfo import HFTrainerInfo
trainer_info = HFTrainerInfo(">checkpoint_path>")
log_df = trainer_info.log_to_pandas()
trainer_info.plot_loss(save_path="./training-loss-viz.png")
"""


class HFTrainerInfo:
    def __init__(self, checkpoint_path):
        self.checkpoint_path = Path(checkpoint_path)
        self.best_metric = None
        self.best_model_checkpoint = None
        self.log_history = None
        self.logging_steps = None
        self.num_train_epochs = None
        self.save_steps = None
        self.train_batch_size = None
        self.trainer_state = self.get_trainer_state()

    def get_trainer_state(self):
        trainer_state_path = glob.glob(
            str(self.checkpoint_path / "trainer_state.json")
        )[0]
        with open(trainer_state_path) as f:
            trainer_state_dict = json.load(f)

        self.best_metric = trainer_state_dict["best_metric"]
        self.best_model_checkpoint = trainer_state_dict["best_model_checkpoint"]
        self.log_history = trainer_state_dict["log_history"]
        self.logging_steps = trainer_state_dict["logging_steps"]
        self.num_train_epochs = trainer_state_dict["num_train_epochs"]
        self.save_steps = trainer_state_dict["save_steps"]
        self.train_batch_size = trainer_state_dict["train_batch_size"]
        return trainer_state_dict

    def log_to_pandas(self):
        log_dict_list = []
        for log in self.log_history:
            log_dict = dict()
            log_dict["epoch"] = log["epoch"]
            if "loss" in log.keys():
                log_dict["loss"] = log["loss"]
                log_dict["eval_loss"] = None
            elif "eval_loss" in log.keys():
                log_dict["loss"] = None
                log_dict["eval_loss"] = log["eval_loss"]
            log_dict_list.append(log_dict)
        log_df = pd.DataFrame.from_dict(log_dict_list)
        return log_df

    def plot_loss(self, *, save_path=None):
        log_df = self.log_to_pandas()
        if log_df["loss"].count() > 2:
            log_df["loss"] = log_df["loss"].interpolate(
                method="linear", limit_direction="forward"
            )
        if log_df["eval_loss"].count() > 2:
            log_df["eval_loss_interpolated"] = log_df["eval_loss"].interpolate(
                method="linear", limit_direction="forward"
            )
        plt.figure(figsize=[10, 5])
        (train_loss,) = plt.plot("epoch", "loss", data=log_df, zorder=9)
        (eval_loss,) = plt.plot(
            "epoch", "eval_loss", ".g", label="evaluation loss", data=log_df, zorder=10
        )
        plt.plot(
            "epoch", "eval_loss_interpolated", "g", label="_", data=log_df, zorder=4
        )
        plt.grid()
        plt.xlabel("Epoch")
        plt.legend(
            handles=[
                train_loss,
                eval_loss,
            ]
        )
        if save_path:
            plt.savefig(save_path)
        plt.show()
