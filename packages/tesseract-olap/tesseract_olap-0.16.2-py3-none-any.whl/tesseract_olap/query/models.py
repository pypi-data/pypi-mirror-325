"""Query-related internal structs module.

This module contains data-storing structs, used mainly on the query and backend
modules.
"""

import dataclasses as dcls
from collections.abc import Generator, Iterable, Mapping, Sequence
from copy import copy
from functools import cached_property
from typing import Annotated, Any, Literal, NamedTuple, Optional, Union

from pydantic import BaseModel, Field, model_validator

from tesseract_olap.common import Array, Prim, shorthash
from tesseract_olap.schema import (
    AnyMeasure,
    CalculatedMeasure,
    DimensionTraverser,
    HierarchyTraverser,
    InlineTable,
    LevelTraverser,
    MemberType,
    PropertyTraverser,
    Table,
)

from .enums import (
    AnyOrder,
    Comparison,
    JoinType,
    LogicOperator,
    Membership,
    NullityOperator,
    Order,
    Restriction,
    TimeScale,
)

NumericConstraint = tuple[Union[Comparison, str], float]
ConditionOperator = Union[LogicOperator, Literal["and", "or"]]
MembershipConstraint = tuple[Membership, Array[str]]

SingleFilterCondition = tuple[NumericConstraint]
DoubleFilterCondition = tuple[NumericConstraint, ConditionOperator, NumericConstraint]

FilterCondition = Union[
    NullityOperator,
    # MembershipConstraint,
    SingleFilterCondition,
    DoubleFilterCondition,
]


def parse_filter_condition(value: str) -> FilterCondition:
    nullity_match = NullityOperator.match(value)
    if nullity_match:
        return nullity_match

    if ".and." in value:
        cond1, cond2 = value.split(".and.")
        return (
            parse_numeric_constraint(cond1),
            "and",
            parse_numeric_constraint(cond2),
        )

    if ".or." in value:
        cond1, cond2 = value.split(".or.")
        return (
            parse_numeric_constraint(cond1),
            "or",
            parse_numeric_constraint(cond2),
        )

    return (parse_numeric_constraint(value),)


def parse_numeric_constraint(value: Union[str, Sequence]) -> NumericConstraint:
    if isinstance(value, str):
        comparison, scalar = value.split(".", 1)
    else:
        assert len(value) == 2, (
            "Invalid numeric constraint, tuple must contain only the comparison "
            + f"operator and the scalar value. Found {value!r}"
        )
        comparison, scalar = value
    return Comparison.from_str(comparison), float(scalar)


class CutIntent(BaseModel):
    """Filtering instructions for a qualitative value.

    Instances of this class are used to define cut parameters.
    Its values are directly inputted by the user, so should never be considered
    valid by itself.
    """

    level: str
    include_members: set[Prim]
    exclude_members: set[Prim]

    def __lt__(self, other: Any):
        if isinstance(other, type(self)):
            return self.level < other.level
        return self.level < other

    @model_validator(mode="before")
    @classmethod
    def parse(cls, value: Any):
        if isinstance(value, str):
            level, members = value.split(":", 1)
            value = {
                "level": level.lstrip("~"),
                "include_members": [] if level.startswith("~") else members.split(","),
                "exclude_members": members.split(",") if level.startswith("~") else [],
            }

        if isinstance(value, Sequence):
            level, incl, excl, *_ = [*value, [], []]
            value = {"level": level, "include_members": incl, "exclude_members": excl}

        if isinstance(value, dict):
            nullables = ("", ",")
            include = value.get("include") or value["include_members"]
            value["include_members"] = set(include).difference(nullables)
            exclude = value.get("exclude") or value["exclude_members"]
            value["exclude_members"] = set(exclude).difference(nullables)

        return value


class FilterIntent(BaseModel):
    """Filtering instructions for a quantitative value.

    Instances of this class are used to define filter parameters.
    Its values are directly inputted by the user, so should never be considered
    valid by itself.
    """

    field: str
    condition: FilterCondition

    def __lt__(self, other: Any):
        if isinstance(other, type(self)):
            return self.field < other.field
        return self.field < other

    @model_validator(mode="before")
    @classmethod
    def parse(cls, value: Any):
        if isinstance(value, str):
            field, condition = value.split(".", 1)
            return {"field": field, "condition": parse_filter_condition(condition)}

        if isinstance(value, Sequence):
            field, *condition = value
            assert isinstance(field, str), (
                "When parsing a tuple, the first element must be a string with "
                f"the name of the measure to apply the filter. Found {field!r}"
            )

            if len(condition) == 1:
                if isinstance(condition[0], str):
                    condition = parse_filter_condition(condition[0])
                else:
                    condition = (parse_numeric_constraint(condition[0]),)

            elif len(condition) == 3:
                operator_match = LogicOperator.match(condition[1])
                assert operator_match, (
                    "Joint in double condition tuple is not valid. "
                    f"Accepted values are 'and' 'or' 'xor', found {condition[1]!r}"
                )
                condition = (
                    parse_numeric_constraint(condition[0]),
                    operator_match,
                    parse_numeric_constraint(condition[2]),
                )

            else:
                msg = f"""\
This filter has no valid conditions. You must provide one of the following configurations:
A single string: 'isnull' / 'gte.0' / 'gt.1000.and.lte.100000'
A single condition tuple: ('gt', 3000)
A double condition tuple: ('>', 0), 'and', ('<=', 100)
Found {condition!r}"""
                raise ValueError(msg)

            return {"field": field, "condition": condition}

        return value

    def as_tuple(self):
        return self.field, self.condition


class JoinOnColumns(BaseModel):
    left_on: Union[str, list[str]]
    right_on: Union[str, list[str]]


class JoinIntent(BaseModel):
    """Specifies the intent of the user to perform a Join operation between 2 datasets."""

    on: Union[str, list[str], "JoinOnColumns", None] = None
    how: JoinType = JoinType.LEFT
    suffix: Optional[str] = None
    validate_relation: Literal["m:m", "m:1", "1:m", "1:1"] = "m:m"
    join_nulls: bool = False
    coalesce: Optional[bool] = None


class PaginationIntent(BaseModel):
    """Pagination instructions."""

    limit: Annotated[int, Field(ge=0)] = 0
    offset: Annotated[int, Field(ge=0)] = 0

    @model_validator(mode="before")
    @classmethod
    def parse(cls, value: Any):
        if isinstance(value, str):
            value = (0, 0) if value == "" else value.strip().split(",")

        if isinstance(value, Sequence):
            if len(value) not in (1, 2):
                msg = f"Invalid pagination value, must provide 1 or 2 integers. Found {value!r}"
                raise ValueError(msg)
            return {"limit": value[0], "offset": value[1] if len(value) == 2 else 0}

        return value

    def as_tuple(self):
        return self.limit, self.offset


class SortingIntent(BaseModel):
    """Sorting instructions for internal use."""

    field: str
    order: AnyOrder

    @model_validator(mode="before")
    @classmethod
    def parse(cls, value: Any):
        if isinstance(value, str):
            field, order, *_ = f"{value}.asc".split(".")
            assert field, "Sorting field must be a valid column name"
            return {"field": field, "order": Order.match(order) or Order.ASC}

        if isinstance(value, Sequence):
            field, order, *_ = [*value, "asc"]
            assert field, "Sorting field must be a valid column name"
            return {"field": field, "order": Order.match(order) or Order.ASC}

        return value

    def as_tuple(self):
        return self.field, self.order


class TimeRestriction(BaseModel):
    """Time-axis filtering instructions for internal use.

    Instances of this class are used to define a time restriction over the
    resulting data. It must always contain both fields.
    """

    level: Union[str, TimeScale]
    constraint: Union[
        tuple[Literal[Restriction.LATEST, Restriction.OLDEST], int],
        tuple[Literal[Restriction.EXPR], FilterCondition],
    ]

    @model_validator(mode="before")
    @classmethod
    def parse(cls, value: Any):
        if isinstance(value, str):
            assert "." in value, "Time restriction is malformed; tokens must be separated by dots"
            value = value.split(".")

        if isinstance(value, (list, tuple)):
            assert value, (
                "Time restriction needs to specify a time scale/level name, and a constraint over it"
            )
            level, *constraint = value
            constraint = ".".join(constraint).split(".")

            assert level, (
                "Time restriction needs to specify a level from a time dimension, or a valid time scale available as level in this cube."
            )
            # Attempt to match a TimeScale, else use value as Level name
            level = TimeScale.match(level) or level

            assert constraint, (
                "Time restriction needs to specify a constraint applied to the provided level, which can be a relative time frame or a filtering condition"
            )
            token = constraint[0].strip().lower()

            restriction_match = Restriction.match(token)
            if restriction_match and restriction_match != Restriction.EXPR:
                amount = int(constraint[1] if len(constraint) > 1 else "1")
                constraint = (restriction_match, amount)
            else:
                constraint = (
                    Restriction.EXPR,
                    parse_filter_condition(".".join(constraint)),
                )

            return {"level": level, "constraint": constraint}

        return value


class TopkIntent(BaseModel):
    """Limits the results to the K first/last elements in subsets determined by one or more levels and their associated value.

    Adds a column that indicates the position of each element in that ranking.
    """

    levels: tuple[str, ...]
    measure: str
    order: AnyOrder = Order.DESC
    amount: int = 1

    @model_validator(mode="before")
    @classmethod
    def parse(cls, value: Any):
        if isinstance(value, str):
            amount, levels, measure, order, *_ = f"{value}....".split(".")
            assert levels, (
                "Topk 'levels' field must contain at least a valid level name "
                "from the drilldowns in your request."
            )
            assert measure, (
                "Topk 'measure' field must contain a valid measure name "
                "from the measures in your request."
            )
            return {
                "amount": amount,
                "levels": levels.split(","),
                "measure": measure,
                "order": Order.match(order) or Order.ASC,
            }

        return value


class GrowthIntent(BaseModel):
    """Calculation of growth with respect to a time parameter and a measure"""

    time_level: str
    measure: str
    method: Union[
        tuple[Literal["period"], int],
        tuple[Literal["fixed"], str],
    ] = ("period", 1)

    @model_validator(mode="before")
    @classmethod
    def parse(cls, value: Any):
        if isinstance(value, str):
            time_level, measure, *params = value.split(".")
            assert time_level, (
                "Growth calculation requires the name of a level from a "
                "time dimension included in your request."
            )
            assert measure, (
                "Growth calculation must contain a valid measure name "
                "from the measures in your request."
            )
            assert len(params) > 1, (
                "Growth calculation method requires 2 parameters: "
                "'fixed' and the member key to use as anchor value, or "
                "'period' and an integer for how many periods to take as difference."
            )
            method = ("fixed", params[1]) if params[0] == "fixed" else ("period", int(params[1]))
            return {"time_level": time_level, "measure": measure, "method": method}

        return value


class AliasesIntent(BaseModel):
    """Aliases for levels."""

    aliases: Mapping[str, str]

    @model_validator(mode="before")
    @classmethod
    def parse(cls, value: Any):
        if isinstance(value, str):
            string = value.strip()
            assert string, "Aliases parameter cannot be empty"

            # transform the string into a dictionary
            alias_pairs = cls._validate_str_pairs(
                pair.split(":", 1) for pair in string.split(";") if ":" in pair
            )
            value = dict(alias_pairs)

        if isinstance(value, Mapping):
            return {"aliases": value}

        return value

    @staticmethod
    def _validate_str_pairs(
        generator: Iterable[list[str]],
    ) -> Generator[tuple[str, str], Any, None]:
        seen_keys = set()
        for name, alias in generator:
            clean_name, clean_alias = name.strip(), alias.strip()
            assert clean_name, f"Empty level name in alias pair: '{name}:{alias}'"
            assert clean_alias, f"Empty level alias in alias pair: '{name}:{alias}'"
            assert clean_name not in seen_keys, (
                f"Request contains two aliases for the same level: '{clean_name}'"
            )
            seen_keys.add(clean_name)
            yield clean_name, clean_alias


@dcls.dataclass(eq=True, frozen=True, order=False)
class HierarchyField:
    """Contains the parameters associated to a slicing operation on the data, based on a single Hierarchy from a Cube's Dimension."""

    dimension: "DimensionTraverser"
    hierarchy: "HierarchyTraverser"
    levels: tuple["LevelField", ...]

    def __copy__(self):
        return HierarchyField(
            dimension=self.dimension,
            hierarchy=self.hierarchy,
            levels=tuple(self.levels),
        )

    @property
    def alias(self) -> str:
        """Returns a deterministic unique short ID for the entity."""
        return shorthash(self.dimension.name + self.hierarchy.primary_key)

    @property
    def cut_levels(self) -> Iterable["LevelField"]:
        return (item for item in self.levels if item.is_cut)

    @property
    def drilldown_levels(self) -> Iterable["LevelField"]:
        return (item for item in self.levels if item.is_drilldown)

    @property
    def deepest_level(self) -> "LevelField":
        """Return the deepest LevelField requested in this Hierarchy, for this query operation."""
        # TODO: check if is needed to force this to use drilldowns only
        return self.levels[-1]

    @property
    def foreign_key(self) -> str:
        """Return the column in the fact table of the Cube this Dimension belongs to, that matches the primary key of the items in the dim_table."""
        return self.dimension.foreign_key

    @property
    def has_drilldowns(self) -> bool:
        """Verify if any of the contained LevelFields is being used as a drilldown."""
        return any(self.drilldown_levels)

    @property
    def primary_key(self) -> str:
        """Return the column in the dimension table for the parent Dimension, which is used as primary key for the whole set of levels in the chosen Hierarchy."""
        return self.hierarchy.primary_key

    @property
    def table(self) -> Union[Table, InlineTable, None]:
        """Return the table to use as source for the Dimension data.

        If not set, the data is stored directly in the fact table for the Cube.
        """
        return self.hierarchy.table


@dcls.dataclass(eq=True, frozen=True, order=False, repr=False)
class LevelField:
    """Contains the parameters associated to the slice operation, specifying the columns each resulting group should provide to the output data."""

    level: "LevelTraverser"
    level_alias: Optional[str] = None
    caption: Optional["PropertyTraverser"] = None
    is_drilldown: bool = False
    members_exclude: set[str] = dcls.field(default_factory=set)
    members_include: set[str] = dcls.field(default_factory=set)
    properties: frozenset["PropertyTraverser"] = dcls.field(default_factory=frozenset)
    time_restriction: Optional[TimeRestriction] = None

    def __copy__(self):
        return LevelField(
            level=self.level,
            level_alias=self.level_alias,
            caption=self.caption,
            is_drilldown=self.is_drilldown,
            members_exclude=set(self.members_exclude),
            members_include=set(self.members_include),
            properties=frozenset(self.properties),
            time_restriction=(
                self.time_restriction.model_copy() if self.time_restriction else None
            ),
        )

    def __repr__(self):
        params = (
            f"name={self.level.name!r}",
            f"is_drilldown={self.is_drilldown!r}",
            f"alias={self.level_alias!r}",
            f"caption={self.caption!r}",
            f"properties={sorted(self.properties, key=lambda x: x.name)!r}",
            f"cut_exclude={sorted(self.members_exclude)!r}",
            f"cut_include={sorted(self.members_include)!r}",
            f"time_restriction={self.time_restriction!r}",
        )
        return f"{type(self).__name__}({', '.join(params)})"

    @property
    def alias(self) -> str:
        """Returns a deterministic unique short ID for the entity."""
        return shorthash(self.level.name + self.level.key_column)

    @property
    def is_cut(self) -> bool:
        return len(self.members_exclude) + len(self.members_include) > 0

    @property
    def key_column(self) -> str:
        return self.level.key_column

    @property
    def name(self) -> str:
        return self.level.name

    def id_column(self, locale: str) -> "Column":
        """Return the column used as ID for the level in this object."""
        key_column = self.level.key_column
        if self.level.get_name_column(locale) is None:
            return Column(key_column, self.level.name)
        return Column(key_column, f"{self.level.name} ID")

    def iter_columns(self, locale: str):
        """Yield the related columns in the database as defined by this object.

        This comprises Drilldown ID, Drilldown Caption, and Properties.
        """
        name = self.level.name
        key_column = self.level.key_column
        name_column = self.level.get_name_column(locale)
        if name_column is None:
            yield Column(key_column, name)
        else:
            yield Column(key_column, f"{name} ID")
            yield Column(name_column, name)
        for propty in self.properties:
            propty_column = propty.get_key_column(locale)
            yield Column(propty_column, propty.name)


@dcls.dataclass(eq=True, frozen=True, order=False, repr=False)
class MeasureField:
    """MeasureField dataclass.

    Contains the parameters needed to filter the data points returned by the
    query operation from the server.
    """

    measure: "AnyMeasure"
    is_measure: bool = False
    constraint: Optional[FilterCondition] = None
    with_ranking: Optional[Literal["asc", "desc"]] = None

    def __copy__(self):
        return MeasureField(
            measure=self.measure,
            is_measure=self.is_measure,
            constraint=(
                copy(self.constraint)
                if isinstance(self.constraint, tuple)
                else self.constraint
            ),
            with_ranking=self.with_ranking,
        )

    def __repr__(self) -> str:
        params = (
            f"name={self.measure.name!r}",
            f"is_measure={self.is_measure!r}",
            f"constraint={self.constraint!r}",
            f"with_ranking={self.with_ranking!r}",
        )
        return f"{type(self).__name__}({', '.join(params)})"

    @cached_property
    def alias_name(self) -> str:
        """Return a deterministic short hash of the name of the entity."""
        return shorthash(self.measure.name)

    @cached_property
    def alias_key(self) -> str:
        """Return a deterministic hash of the key column of the entity."""
        return shorthash(
            repr(self.measure.formula)
            if isinstance(self.measure, CalculatedMeasure)
            else self.measure.key_column,
        )

    @property
    def name(self) -> str:
        """Quick method to return the measure name."""
        return self.measure.name

    @property
    def aggregator_params(self) -> dict[str, str]:
        """Quick method to retrieve the measure aggregator params."""
        return self.measure.aggregator.get_params()

    @property
    def aggregator_type(self) -> str:
        """Quick method to retrieve the measure aggregator type."""
        return str(self.measure.aggregator)

    def get_source(self):
        # TODO add locale compatibility
        """Quick method to obtain the source information of the measure."""
        return self.measure.annotations.get("source")

    @property
    def datatype(self):
        return MemberType.FLOAT64


class Column(NamedTuple):
    name: str
    alias: str

    @property
    def hash(self):
        return shorthash(self.alias + self.name)
