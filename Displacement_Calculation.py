import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_velocity = pd.read_csv(r"C:\Users\bowen\HEMI\flyer_shot_3D_reconstruction\C3--20240510--00000--velocity.csv")
df_velocity.columns = ["time", "velocity"]


df_displacement = np.zeros((df_velocity.shape[0], df_velocity.shape[1]))


for i in range(df_velocity.shape[0]):
    df_displacement[i, 1] = np.trapezoid(df_velocity.loc[0:i, "velocity"], df_velocity.loc[0:i, "time"])
    df_displacement[i, 0] = df_velocity.loc[i, "time"]

fig, ax = plt.subplots(1, 2, figsize=(10, 3))    
ax[0].plot(df_displacement[:,0], df_displacement[:,1], label='Displacement')
ax[1].plot(df_velocity["time"], df_velocity["velocity"], label='Velocity', color='r')

plt.show()