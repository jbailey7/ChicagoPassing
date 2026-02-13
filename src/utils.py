import pandas as pd


TEMP_ORDER = ["below_32", "32_to_50", "above_50"]


def baseline_row(df: pd.DataFrame) -> pd.DataFrame:
    base = df.mean(numeric_only=True).to_frame().T
    base["temp_bin"] = df["temp_bin"].mode().iloc[0]
    return base


def predict_from_model(model, df: pd.DataFrame, **kwargs) -> float:
    base = baseline_row(df)
    for k, v in kwargs.items():
        base[k] = v
    base["temp_bin"] = pd.Categorical(base["temp_bin"], categories=TEMP_ORDER, ordered=True)
    return float(model.predict(base).iloc[0])


def predict_with_ci(model, df: pd.DataFrame, var_name: str, var_range, soldier_field_val: int,
                    fixed: dict | None = None, alpha: float = 0.05):
    if fixed is None:
        fixed = {}

    preds, lowers, uppers = [], [], []
    for val in var_range:
        base = baseline_row(df)
        base["soldier_field"] = soldier_field_val
        base[var_name] = val
        base["is_home"] = fixed.get("is_home", 0)
        base["precip"] = fixed.get("precip", 0)
        base["opp_def_epa_c"] = fixed.get("opp_def_epa_c", 0)
        base["wind_c"] = fixed.get("wind_c", base["wind_c"].iloc[0])
        base["temp_c"] = fixed.get("temp_c", base["temp_c"].iloc[0])
        base["temp_bin"] = pd.Categorical(base["temp_bin"], categories=TEMP_ORDER, ordered=True)

        pred = model.get_prediction(base)
        summary = pred.summary_frame(alpha=alpha)
        preds.append(summary["mean"].iloc[0])
        lowers.append(summary["mean_ci_lower"].iloc[0])
        uppers.append(summary["mean_ci_upper"].iloc[0])

    return preds, lowers, uppers
