import enum
import itertools
import sys
import warnings
from collections.abc import Iterable
from typing import Any, TypeAlias

import gliner.multitask.base
import pydantic

from sieves.engines.core import Engine, Executable

PromptSignature: TypeAlias = list[str]
Model: TypeAlias = gliner.multitask.base.GLiNERBasePipeline
Result: TypeAlias = list[dict[str, str | float]]


class InferenceMode(enum.Enum):
    """Available inference modes."""

    ner = 0
    classification = 1
    question_answering = 2
    information_extraction = 3
    summarization = 4


class GliX(Engine[PromptSignature, Result, Model, InferenceMode]):
    @property
    def inference_modes(self) -> type[InferenceMode]:
        return InferenceMode

    @property
    def supports_few_shotting(self) -> bool:
        return False

    def build_executable(
        self,
        inference_mode: InferenceMode,
        prompt_template: str | None,
        prompt_signature: type[PromptSignature] | PromptSignature,
        fewshot_examples: Iterable[pydantic.BaseModel] = (),
    ) -> Executable[Result]:
        assert isinstance(prompt_signature, list)
        cls_name = self.__class__.__name__
        if prompt_template:
            warnings.warn(f"prompt_template is ignored by engine {cls_name}.")
        if len(list(fewshot_examples)):
            warnings.warn(f"Few-shot examples are not supported by engine {cls_name}.")

        def execute(values: Iterable[dict[str, Any]]) -> Iterable[Result]:
            """Execute prompts with engine for given values.
            :param values: Values to inject into prompts.
            :return Iterable[Result]: Results for prompts.
            """
            match inference_mode:
                case InferenceMode.classification:
                    batch_size = self._batch_size if self._batch_size != -1 else sys.maxsize
                    # Ensure values are read as generator for standardized batch handling (otherwise we'd have to use
                    # different batch handling depending on whether lists/tuples or generators are used).
                    values = (v for v in values)

                    while batch := [vals["text"] for vals in itertools.islice(values, batch_size)]:
                        if len(batch) == 0:
                            break

                        yield from self._model(
                            batch, classes=prompt_signature, **({"multi_label": True} | self._inference_kwargs)
                        )

                case _:
                    raise ValueError(f"Inference mode {inference_mode} not supported by {cls_name} engine.")

        return execute
