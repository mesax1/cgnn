#   Copyright 2019 Takenori Yamamoto
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
"""A program that plots a training history."""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("history.csv")
df["train_rmse"] = df["train_loss"].map(np.sqrt)
df["val_rmse"] = df["val_loss"].map(np.sqrt)
ax1 = df.plot(x="epoch", y=["train_mae", "val_mae", "train_rmse", "val_rmse"])
ax1.set_ylabel("Error")
ax1.set_xlabel("Epochs")

plt.show()
