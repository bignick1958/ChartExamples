import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# данные для графика 4  
def plot_chart():
    sns.set()
    
    np.random.seed(33)
    normal_data_a = np.random.normal(size = 500, loc = 100, scale = 10)
    
    df_normal_a = pd.DataFrame(data = normal_data_a, columns = ['score']).assign(group = 'Group A')
    
    sns.histplot(data = df_normal_a
                    , x = 'score'
                    , bins = 50
                    , kde = True
                    )
    
    plt.show()
    
    
# данные для графика 5  
def plot_chart2():
    #sns.set()
    sns.color_palette (n_colors = 16, desat = .90)
    sns.set_style('whitegrid', {'ytick.color'         : '.10'})
    
    
    
    
    np.random.seed(33)
    normal_data_a = np.random.normal(size = 500, loc = 100, scale = 6)
    normal_data_b = np.random.normal(size = 500, loc = 107, scale = 5)
    
    df_normal_a = pd.DataFrame(data = normal_data_a, columns = ['score']).assign(group = 'Group A')
    df_normal_b = pd.DataFrame(data = normal_data_b, columns = ['score']).assign(group = 'Group B')
    
    score_data = pd.concat([df_normal_a, df_normal_b], ignore_index = True)
    
    # print (score_data)
    
    sns.histplot(data = score_data
                    , x = 'score'
                    , alpha = .7
                    , hue = 'group'
                    , bins = 50
                    , kde = True
                    )
    
    plt.show()
