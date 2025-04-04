from __future__ import annotations

import typing
from dataclasses import dataclass

import borsh_construct as borsh
from construct import Container


class UpdatePerpParametersArgsJSON(typing.TypedDict):
    min_funding_rate_percent: int
    max_funding_rate_percent: int
    perp_impact_cash_delta: int


@dataclass
class UpdatePerpParametersArgs:
    layout: typing.ClassVar = borsh.CStruct(
        "min_funding_rate_percent" / borsh.I64,
        "max_funding_rate_percent" / borsh.I64,
        "perp_impact_cash_delta" / borsh.U64,
    )
    min_funding_rate_percent: int
    max_funding_rate_percent: int
    perp_impact_cash_delta: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "UpdatePerpParametersArgs":
        return cls(
            min_funding_rate_percent=obj.min_funding_rate_percent,
            max_funding_rate_percent=obj.max_funding_rate_percent,
            perp_impact_cash_delta=obj.perp_impact_cash_delta,
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "min_funding_rate_percent": self.min_funding_rate_percent,
            "max_funding_rate_percent": self.max_funding_rate_percent,
            "perp_impact_cash_delta": self.perp_impact_cash_delta,
        }

    def to_json(self) -> UpdatePerpParametersArgsJSON:
        return {
            "min_funding_rate_percent": self.min_funding_rate_percent,
            "max_funding_rate_percent": self.max_funding_rate_percent,
            "perp_impact_cash_delta": self.perp_impact_cash_delta,
        }

    @classmethod
    def from_json(cls, obj: UpdatePerpParametersArgsJSON) -> "UpdatePerpParametersArgs":
        return cls(
            min_funding_rate_percent=obj["min_funding_rate_percent"],
            max_funding_rate_percent=obj["max_funding_rate_percent"],
            perp_impact_cash_delta=obj["perp_impact_cash_delta"],
        )
