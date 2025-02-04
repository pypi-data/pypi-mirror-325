MODEL_DATA = {
    "gpt-4o":{
        "model_name": "gpt-4o-2024-05-13",
        "max_context_window": 128000,
        "max_output_tokens": 8192,
        "input_cost_per_token": 0.005 / 1000,
        "output_cost_per_token": 0.015 / 1000,
    },
    "gpt-4o-mini":{
        "model_name": "gpt-4o-mini-2024-07-18",
        "max_context_window": 128000,
        "max_output_tokens": 8192,
        "input_cost_per_token": 0.00015 / 1000,
        "output_cost_per_token": 0.0006 / 1000,
    },
    "gpt-4o-mini-products-ft":{
        "model_name": "ft:gpt-4o-mini-2024-07-18:vibrant-data-labs:financial-product-extraction-95:9yTaC31L",
        "max_context_window": 128000,
        "max_output_tokens": 8192,
        "input_cost_per_token": 0.00015 / 1000,
        "output_cost_per_token": 0.0006 / 1000,
    },
    "gpt-4": {
        "model_name": "gpt-4-0125-preview",
        "max_context_window": 128000,
        "max_output_tokens": 8192,
        "input_cost_per_token": 0.01 / 1000,
        "output_cost_per_token": 0.03 / 1000,
    },
    "gpt-3.5": {
        "model_name": "gpt-3.5-turbo-0125",
        "max_context_window": 16385,
        "max_output_tokens": 4096,
        "input_cost_per_token": 0.0005 / 1000,
        "output_cost_per_token": 0.0015 / 1000, },
}


SEED = 7118
