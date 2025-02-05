from typing import Dict, Optional, List, TypedDict
import os
import json

from l2m2.client import LLMClient

HOME_DIR = os.path.expanduser("~")
CONFIG_FILE = os.path.join(HOME_DIR, ".cliff", "config.json")

DIR = os.path.dirname(os.path.abspath(__file__))
HELP_FILE = os.path.join(DIR, "resources/config_help.txt")

HOSTED_PROVIDERS = {
    "groq",
    "cohere",
    "mistral",
    "replicate",
    "openai",
    "cerebras",
    "google",
    "anthropic",
}

DEFAULT_MODEL_MAPPING = {
    "groq": "llama-3.2-1b",
    "cohere": "command-r",
    "mistral": "mistral-small",
    "replicate": "llama-3-8b",
    "openai": "gpt-4o-mini",
    "cerebras": "llama-3.1-8b",
    "google": "gemini-2.0-flash",
    "anthropic": "claude-3.5-haiku",
}


class Config(TypedDict):
    provider_credentials: Dict[str, str]
    default_model: Optional[str]
    preferred_providers: Dict[str, str]
    ollama_models: List[str]
    memory_window: int


DEFAULT_CONFIG: Config = {
    "provider_credentials": {},
    "default_model": None,
    "preferred_providers": {},
    "ollama_models": [],
    "memory_window": 10,
}


def get_memory_window() -> int:
    config = load_config()
    return config["memory_window"]


def load_config() -> Config:
    if not os.path.exists(CONFIG_FILE):
        os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
        with open(CONFIG_FILE, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
        config = DEFAULT_CONFIG
    else:
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)

    return config


def apply_config(config: Config, llm: LLMClient) -> None:
    for provider in config["provider_credentials"]:
        llm.add_provider(provider, config["provider_credentials"][provider])

    llm.set_preferred_providers(config["preferred_providers"])

    for model in config["ollama_models"]:
        llm.add_local_model(model, "ollama")


def save_config(config: Config) -> None:
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)


def add_provider(provider: str, api_key: str) -> int:
    if provider not in HOSTED_PROVIDERS:
        print(f"[Cliff] Invalid provider: {provider}")
        return 1

    config = load_config()
    exists = config["provider_credentials"].get(provider)

    config["provider_credentials"][provider] = api_key

    if config["default_model"] is None:
        config["default_model"] = DEFAULT_MODEL_MAPPING[provider]

    save_config(config)

    if exists:
        print(f"[Cliff] Updated provider {provider}")
        return 0
    else:
        print(f"[Cliff] Added provider {provider}")
        return 0


def add_ollama(model: str) -> int:
    config = load_config()
    config["ollama_models"].append(model)
    if config["default_model"] is None:
        config["default_model"] = model
    save_config(config)
    print(f"[Cliff] Added local model {model}")
    return 0


def remove_ollama(model: str) -> int:
    config = load_config()
    if model not in config["ollama_models"]:
        print(f"[Cliff] local model {model} not found")
        return 1
    config["ollama_models"].remove(model)
    save_config(config)
    print(f"[Cliff] Removed local model {model}")
    return 0


def remove_provider(provider: str) -> int:
    # TODO get the provider mapping from l2m2 to make sure we reset the default model if its provider is removed

    config = load_config()
    exists = config["provider_credentials"].get(provider)

    if not exists:
        print(f"[Cliff] Provider {provider} not found")
        return 1

    del config["provider_credentials"][provider]
    save_config(config)

    print(f"[Cliff] Removed provider {provider}")
    return 0


def set_default_model(model: str, llm: LLMClient) -> int:
    active_models = llm.get_active_models()
    if model not in active_models:
        print(f"[Cliff] Model {model} not found")
        return 1

    config = load_config()
    config["default_model"] = model
    save_config(config)

    print(f"[Cliff] Set default model to {model}")
    return 0


def prefer_add(model: str, provider: str) -> int:
    config = load_config()
    config["preferred_providers"][model] = provider
    save_config(config)
    print(f"[Cliff] Added preferred provider {provider} for {model}")
    return 0


def prefer_remove(model: str) -> int:
    config = load_config()
    if model not in config["preferred_providers"]:
        print(f"[Cliff] Preferred provider for {model} not found")
        return 1
    del config["preferred_providers"][model]
    save_config(config)
    print(f"[Cliff] Removed preferred provider for {model}")
    return 0


def update_memory_window(window: int) -> int:
    config = load_config()
    config["memory_window"] = window
    save_config(config)
    print(f"[Cliff] Updated memory window size to {window}")
    return 0


def reset_config() -> int:
    save_config(DEFAULT_CONFIG)
    print("[Cliff] Reset config to defaults")
    return 0


def show_config() -> int:
    config = load_config()
    print(json.dumps(config, indent=4))
    return 0


def process_config_command(command: List[str], llm: LLMClient) -> int:
    if len(command) == 0 or command[0] == "help":
        with open(HELP_FILE, "r") as f:
            print(f.read())
        return 0

    elif command[0] == "add":
        if len(command) != 3:
            print("[Cliff] Usage: add [provider] [api-key] or add ollama [model]")
            return 1
        if command[1] == "ollama":
            return add_ollama(command[2])
        else:
            return add_provider(command[1], command[2])

    elif command[0] == "remove":
        if len(command) < 2:
            print("[Cliff] Usage: remove [provider] or remove ollama [model]")
            return 1
        if command[1] == "ollama":
            if len(command) != 3:
                print("[Cliff] Usage: remove ollama [model]")
                return 1
            return remove_ollama(command[2])
        else:
            return remove_provider(command[1])

    elif command[0] == "default-model":
        if len(command) != 2:
            print("[Cliff] Usage: default-model [model]")
            return 1
        return set_default_model(command[1], llm)

    elif command[0] == "prefer":
        if len(command) != 3:
            print("[Cliff] Usage: prefer [model] [provider] or prefer remove [model]")
            return 1
        if command[1] == "remove":
            return prefer_remove(command[2])
        else:
            return prefer_add(command[1], command[2])

    elif command[0] == "memory-window":
        if len(command) != 2:
            print("[Cliff] Usage: memory-window [window-size]")
            return 1
        return update_memory_window(int(command[1]))

    elif command[0] == "reset":
        return reset_config()

    elif command[0] == "show":
        return show_config()

    else:
        print(
            f"[Cliff] Unrecognized config command: {command[0]}. For usage, run cliff --config help"
        )
        return 1
