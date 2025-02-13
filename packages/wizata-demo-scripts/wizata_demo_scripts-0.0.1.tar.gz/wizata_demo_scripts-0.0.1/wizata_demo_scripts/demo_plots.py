import plotly.graph_objects as go
import wizata_dsapi

def ts_plot(context:wizata_dsapi.Context):
    
    name_df = list(context.dataframes.keys())[0]
    
    df_pred_target = context.dataframes["df_pred_target"]

    fig= go.Figure()
    fig.add_trace(go.Scatter(x = df_pred_target.index,y = df_pred_target["target"], name = "target"))
    fig.add_trace(go.Scatter(x = df_pred_target.index,y = df_pred_target["variable_1"], name = "variable_1"))
    fig.add_trace(go.Scatter(x = df_pred_target.index,y = df_pred_target["variable_2"], name = "variable_2"))
    fig.add_trace(go.Scatter(x = df_pred_target.index,y = df_pred_target["LR_prediction"], name = "LR_prediction"))
    context.set_plot(fig, name_df)