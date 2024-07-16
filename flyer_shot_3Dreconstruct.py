import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time


def model_displacement(pdv0_path, pdv1_path, pdv2_path, pdv3_path):
    #import all csv files
    df0 = pd.read_csv(pdv0_path)
    df0.columns = ["time", "velocity"]

    df1 = pd.read_csv(pdv1_path)
    df1.columns = ["time", "velocity"]

    df2 = pd.read_csv(pdv2_path)
    df2.columns = ["time", "velocity"]

    df3 = pd.read_csv(pdv3_path)
    df3.columns = ["time", "velocity"]

    min_rows = min(df0.shape[0], df1.shape[0], df2.shape[0], df3.shape[0])



    fig = plt.figure()
    ax = plt.axes(projection='3d')

    #define location of all 4 pdv locations (left column:x location, middle column:y location)
    vertices = np.array([[0, 0, 0.001],
                        [0, 1, 0],
                        [1, 0, 0],
                        [1, 1, 0]])

    # Define the triangles displayed vertex indices
    triangles = [[0, 1, 3], [0, 2, 3]]

    """
    #loop for velocity graphs 3D animated
    for i in range(min_rows):

        if i % 10 == 0: 
            #updating z value of verticies
            vertices[0, 2] = df0.at[i, "velocity"]
            vertices[1, 2] = df1.at[i, "velocity"]
            vertices[2, 2] = df2.at[i, "velocity"]
            vertices[3, 2] = df3.at[i, "velocity"]

            #plotting
            ax.cla()
            ax.set_zlim(-500, 500)  # Fix z-axis limits
            ax.plot_trisurf(vertices[:, 0], vertices[:, 1], vertices[:, 2], triangles=triangles, cmap='viridis')
            plt.pause(0.1)
            print(df0.at[i, "velocity"])
        
        print(i)
    """    

    #loop for displacement graphs animated
    df0_pos = 0
    df1_pos = 0
    df2_pos = 0
    df3_pos = 0

    for i in range(1, min_rows):  

        df0_pos += df0.at[i, "velocity"]*(df0.at[i, "time"]-df0.at[i-1, "time"])
        df1_pos += df1.at[i, "velocity"]*(df1.at[i, "time"]-df1.at[i-1, "time"])
        df2_pos += df2.at[i, "velocity"]*(df2.at[i, "time"]-df2.at[i-1, "time"])
        df3_pos += df3.at[i, "velocity"]*(df3.at[i, "time"]-df3.at[i-1, "time"])

        if i % 100 == 0:

            #updating z value of verticies
            vertices[0, 2] = df0_pos
            vertices[1, 2] = df1_pos
            vertices[2, 2] = df2_pos
            vertices[3, 2] = df3_pos

            ax.cla()
            ax.set_zlim(0, 0.0003)
            ax.plot_trisurf(vertices[:, 0], vertices[:, 1], vertices[:, 2], triangles=triangles)
            plt.pause(0.1)
            print(df0_pos)
        time.sleep(0.001)

    plt.show()


def model_velocity(pdv0_path, pdv1_path, pdv2_path, pdv3_path):
    #import all csv files
    df0 = pd.read_csv(pdv0_path)
    df0.columns = ["time", "velocity"]

    df1 = pd.read_csv(pdv1_path)
    df1.columns = ["time", "velocity"]

    df2 = pd.read_csv(pdv2_path)
    df2.columns = ["time", "velocity"]

    df3 = pd.read_csv(pdv3_path)
    df3.columns = ["time", "velocity"]

    min_rows = min(df0.shape[0], df1.shape[0], df2.shape[0], df3.shape[0])



    fig = plt.figure()
    ax = plt.axes(projection='3d')

    #define location of all 4 pdv locations (left column:x location, middle column:y location)
    vertices = np.array([[0, 0, 0.001],
                        [0, 1, 0],
                        [1, 0, 0],
                        [1, 1, 0]])

    # Define the triangles displayed vertex indices
    triangles = [[0, 1, 3], [0, 2, 3]]

    
    #loop for velocity graphs 3D animated
    for i in range(min_rows):

        if i % 100 == 0: 
            #updating z value of verticies
            vertices[0, 2] = df0.at[i, "velocity"]
            vertices[1, 2] = df1.at[i, "velocity"]
            vertices[2, 2] = df2.at[i, "velocity"]
            vertices[3, 2] = df3.at[i, "velocity"]

            #plotting
            ax.cla()
            ax.set_zlim(-100, 1500)  # Fix z-axis limits
            ax.plot_trisurf(vertices[:, 0], vertices[:, 1], vertices[:, 2], triangles=triangles, color = 'purple')
            plt.pause(0.1)
            print(df0.at[i, "velocity"])
        
        time.sleep(0.001)
        

    

    plt.show()


