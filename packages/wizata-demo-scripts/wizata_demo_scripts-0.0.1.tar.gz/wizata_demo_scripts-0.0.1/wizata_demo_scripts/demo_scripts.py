import wizata_dsapi
import numpy as np
import pandas as pd
from math import log10, floor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error


def LR_model_training(context: wizata_dsapi.Context):

    df = context.dataframe

    df_pred = df.dropna()
    target_var_name = "target"

    model = LinearRegression()
    model.fit(df_pred.drop(columns=target_var_name), df_pred[target_var_name])

    context.set_model(model, df_pred.drop(columns=target_var_name).columns)


def LR_model_evaluation(context: wizata_dsapi.Context):

    df = context.dataframes["df"]
    df_pred = context.dataframes["df_pred"]

    df_pred_target = df_pred.copy()
    df_pred_target["target"] = df["target"]
    df_pred_target = df_pred_target.applymap(
        lambda x: round(x, 3 - int(floor(log10(abs(x)))) - 1 if (x != 0) & (~np.isnan(x)) else x))

    df_metrics = pd.DataFrame(index=["score"])
    df_metrics["mse"] = [np.sqrt(mean_squared_error(df_pred_target["target"], df_pred_target["LR_prediction"]))]
    df_metrics["r2"] = [r2_score(df_pred_target["target"], df_pred_target["LR_prediction"])]
    df_metrics = df_metrics.applymap(
        lambda x: round(x, 4 - int(floor(log10(abs(x)))) - 1 if (x != 0) & (~np.isnan(x)) else x))

    return df_pred_target, df_metrics