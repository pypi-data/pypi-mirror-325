# llms/__init__.py

# Internal registry for LLM implementations.
_registered_models = {}

def register_llm(name, llm_class):
    _registered_models[name.lower()] = llm_class

def get_llm(llm_name, *args, **kwargs):
    llm_class = _registered_models.get(llm_name.lower())
    if llm_class is None:
        raise ValueError(f"LLM '{llm_name}' is not registered.")
    return llm_class(*args, **kwargs)

# Import and automatically register built-in LLM implementations.
from .openai_llm import OpenAI
from .gemini_llm import Gemini

register_llm("openai", OpenAI)
register_llm("gemini", Gemini)
