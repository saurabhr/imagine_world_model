from parse import *
import pandas as pd

def sim_data_extract(data):
    x = data["taskdata"]
    y = []
    for i in x:
        y.append(
            {
                "trial_idx": i["trial_idx"],
                "system_message_idx": i["system_message_idx"],
                "system_message": i["system_message"],
                "system_template": i["system_template"],
                "chaintype": i["chain_type"],
                "trace": i["trace_id"],
                "trid": i["trid"],
                "context": i["context"],
                "context_item": i["context_item"],
                "item": i["stimulus"],
                **(eval(i["pred_resp"]["content"])),
            }
        )
    return y


def extract_population(x):
    parsed = parse(x["system_template"], x["system_message"])
    system_persona = parsed.named["system_persona"]
    if "Typical imagery" in system_persona:
        return "Typical Imagery"
    elif "Hypophantasia" in system_persona:
        return "Hypophantasia"
    elif "Aphantasia" in system_persona:
        return "Aphantasia"
    elif "Hyperphantasia" in system_persona:
        return "Hyperphantasia"
    return "No Imagery Ability Instruction"



def pivot_ai_vividness(data, index=None, columns=None, values=None):
    if index is None:
        index = ["system_message_idx", "task", "model", "imagination_ability"]
    if columns is None:
        columns = "trid"
    if values is None:
        values = "Vividness"
    data = data.pivot(
        index=index,
        columns=columns,
        values=values,
    )
    return data

def sample_from_quantiles(ai_data, quantiles, N=60):
    quantile_ranges = [
        [quantiles[0], quantiles[1]],
        [quantiles[1], quantiles[2]],
        [quantiles[2], quantiles[3]],
        [quantiles[3], quantiles[4]],
        [quantiles[4], quantiles[5]],
        [quantiles[5], quantiles[6]],
        [quantiles[6], quantiles[7]],
        [quantiles[7], quantiles[8]],
        [quantiles[8], quantiles[9]],
        [quantiles[9], quantiles[10]],
    ]

    pai_data = {}  # population ai data
    # Loop through each task and model, sampling N instances from each quantile range
    # and storing them in a dictionary with (task, model) as keys.
    # The dictionary will have the structure: {(task, model): sampled_data}
    # where sampled_data is a DataFrame containing the sampled instances.
    # N is the number of samples to take from each quantile range.
    # If the number of instances in a quantile range is less than N, it samples
    # all available instances and fills the rest with random samples from the same model.
    for task in ai_data["task"].unique():
        ai_data_t = ai_data.loc[ai_data["task"] == task]
        for model in ai_data_t["model"].unique():
            ai_ = pd.DataFrame()
            ai_data_m = ai_data_t.loc[ai_data_t["model"] == model]

            for i, qrange in enumerate(quantile_ranges):
                data_range = ai_data_m[
                    ai_data_m["score"].between(qrange[0], qrange[1], inclusive="right")
                ]

                if data_range.shape[0] < N:
                    data_range_sample = data_range
                    data_range_sample2 = ai_data_m.sample(
                        n=(N - data_range.shape[0]), random_state=(i + 1) * (100)
                    )
                    ai_data_m = ai_data_m.drop(data_range_sample2.index)
                    data_range_sample = pd.concat([data_range_sample, data_range_sample2])
                else:
                    data_range_sample = data_range.sample(n=N, random_state=100)

                ai_ = pd.concat([ai_, data_range_sample])

            pai_data[(task, model)] = ai_
            print(task, model, ai_.shape)

    return pai_data