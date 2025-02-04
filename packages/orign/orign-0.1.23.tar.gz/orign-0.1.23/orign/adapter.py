from typing import Dict, Optional

from orign.buffer import ReplayBuffer
from orign.config import GlobalConfig
from orign.models import V1LlamaFactoryParams, V1MSSwiftBufferParams, V1VLLMParams
from orign.stream.chat import ChatModel


class Adapter:
    def __init__(
        self,
        name: str,
        model: Optional[str] = None,
        model_type: Optional[str] = None,
        vram_request: Optional[str] = None,
        provider: str = "ms-swift",
        namespace: Optional[str] = None,
        cpu_request: Optional[str] = None,
        dtype: Optional[str] = None,
        trust_remote_code: Optional[bool] = None,
        train_every: int = 50,
        sample_n: int = 100,
        sample_strategy: str = "Random",
        queue: Optional[str] = None,
        ms_swift_params: Optional[V1MSSwiftBufferParams] = None,
        vllm_params: Optional[V1VLLMParams] = None,
        llama_factory_params: Optional[V1LlamaFactoryParams] = None,
        labels: Optional[Dict[str, str]] = None,
        config: Optional[GlobalConfig] = None,
    ):
        self.name = name

        if model:
            if ms_swift_params:
                ms_swift_params.model = model
            if vllm_params:
                vllm_params.model = model

        if model_type:
            if model_type not in MODEL_TYPES:
                raise ValueError(f"Invalid model type: {model_type}")
            vllm_type = MODEL_TYPES[model_type]
            if ms_swift_params:
                ms_swift_params.model_type = model_type
            if vllm_params:
                vllm_params.model_type = vllm_type

        if ms_swift_params:
            if not ms_swift_params.lora_rank:
                ms_swift_params.lora_rank = 64
            if not ms_swift_params.lora_alpha:
                ms_swift_params.lora_alpha = 128

        self.buffer = ReplayBuffer(
            name=name,
            vram_request=vram_request,
            provider=provider,
            namespace=namespace,
            cpu_request=cpu_request,
            dtype=dtype,
            trust_remote_code=trust_remote_code,
            adapter=name,
            train_every=train_every,
            sample_n=sample_n,
            sample_strategy=sample_strategy,
            queue=queue,
            ms_swift_params=ms_swift_params,
            llama_factory_params=llama_factory_params,
            labels=labels,
            config=config,
        )

        self.model = ChatModel(model="allenai/Molmo-7B-D-0924", provider="vllm")


MODEL_TYPES = {
    "qwen2_vl": "qwen2_vl",
    "paligemma": "paligemma",
    "molmo": "molmo",
}
