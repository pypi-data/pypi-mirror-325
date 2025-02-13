# -*- coding: utf-8 -*-

from __future__ import annotations

import json
from enum import Enum
from typing import Any, Dict, List, Optional, Union

import numpy as np
from pydantic import BaseModel, Field, RootModel


class ModelType(Enum):
    BAYESIAN_NETWORK = "bayesian_network"
    MARKOV_RANDOM_FIELD = "markov_random_field"
    POMDP = "pomdp"
    FACTOR_GRAPH = "factor_graph"


class Metadata(BaseModel):
    model_version: Optional[str] = None
    model_type: Optional[ModelType] = None
    description: Optional[str] = None


class Tensor(RootModel[Union[float, List["Tensor"]]]):
    root: Union[float, List["Tensor"]]

    def __iter__(self):
        if isinstance(self.root, float):
            yield self.root
        else:
            yield from self._to_floats()

    def __len__(self):
        if isinstance(self.root, float):
            return 1
        return len(self.root)

    def _to_floats(self) -> Union[float, List[float]]:
        if isinstance(self.root, float):
            return self.root
        if isinstance(self.root, list):
            return [
                item._to_floats() if isinstance(item, Tensor) else item
                for item in self.root
            ]
        raise ValueError("Invalid tensor value")

    def numpy(self):
        return np.array(self._to_floats())


class FactorRole(Enum):
    TRANSITION = "transition"
    PREFERENCE = "preference"
    LIKELIHOOD = "likelihood"
    INITIAL_STATE_PRIOR = "initial_state_prior"


class VariableRole(Enum):
    CONTROL_STATE = "control_state"
    LATENT = "latent"


class DiscreteVariableNamedElements(BaseModel):
    elements: List[str]
    role: Optional[VariableRole] = None


class DiscreteVariableAnonymousElements(BaseModel):
    cardinality: int = Field(..., ge=1, description="Cardinality")
    role: Optional[VariableRole] = None


class Variable(
    RootModel[Union[DiscreteVariableNamedElements, DiscreteVariableAnonymousElements]]
):
    def get_elements(self):
        if isinstance(self.root, DiscreteVariableNamedElements):
            return self.root.elements
        if isinstance(self.root, DiscreteVariableAnonymousElements):
            return [str(c) for c in range(self.root.cardinality)]

        raise ValueError(f"Cannot parse VFG Variable: {self}")


class Distribution(Enum):
    CATEGORICAL = "categorical"
    CATEGORICAL_CONDITIONAL = "categorical_conditional"


class Factor(BaseModel):
    variables: List[str]
    distribution: Distribution
    values: Tensor
    role: Optional[FactorRole] = None


class VFG(BaseModel):
    version: str = Field("0.4.0", Literal=True)
    metadata: Optional[Metadata] = Field(default=None)
    variables: Dict[str, Variable] = Field(default_factory=dict)
    factors: List[Factor] = Field(default_factory=list)
    visualization_metadata: Optional[Any] = None

    def __init__(
        self,
        variables: Optional[Dict[str, Variable]] = None,
        factors: Optional[List[Factor]] = None,
        **data,
    ):
        if variables is None:
            variables = {}
        if factors is None:
            factors = []
        super().__init__(variables=variables, factors=factors, **data)

    # TODO field validation
    # metadata must be Metadata

    def to_dict(self, exclude_none: bool = True) -> dict:
        vfg_model_dump: str = self.model_dump_json(exclude_none=exclude_none)
        vfg_dict = json.loads(vfg_model_dump)
        return vfg_dict


Tensor.model_rebuild()
