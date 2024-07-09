import seaborn as sns
import matplotlib.pyplot as plt

def reg_resid_plots(data):
    # Create a pair plot to visualize the relationships
    sns.pairplot(data)
    plt.show()

    # Plot regression plot for each pair of columns
    columns = data.columns
    for col1 in columns:
        for col2 in columns:
            if col1 != col2:
                sns.lmplot(x=col1, y=col2, data=data)
                plt.show()

    # Plot residual plots for each pair of columns
    for col1 in columns:
        for col2 in columns:
            if col1 != col2:
                sns.residplot(x=col1, y=col2, data=data)
                plt.show()
