from aiomodrinth.models.project import ProjectType, Category, ProjectLicense, GameVersion

from typing import Union, Type

FacetType = Union[Category, GameVersion, ProjectLicense, ProjectType]


def facet_type_to_string(facet_type: Type[FacetType]) -> str:
    pattern = {Category: "categories",
               GameVersion: "versions",
               ProjectLicense: "license",
               ProjectType: "project_type"
               }

    return pattern[facet_type]


class Facet:
    value: FacetType

    def __init__(self, value: FacetType) -> None:
        self.value = value

    def __str__(self) -> str:
        facet_type = facet_type_to_string(type(self.value))
        facet_value = str(self.value)

        return f'"{facet_type}:{facet_value}"'

    def __and__(self, other: "Facet") -> "FacetAnd":
        return FacetAnd(self, other)

    def __or__(self, other: "Facet"):
        return FacetOr(self, other)


class FacetOr:
    facets: list[Facet, ...]

    def __init__(self, *facets: Facet) -> None:
        self.facets = list(facets)

    def __str__(self) -> str:
        facets_as_str = ",".join(map(str, self.facets))
        return f'[{facets_as_str}]'

    def __or__(self, other):
        return FacetOr(*self.facets, other)


class FacetAnd:
    facets: list[Facet, ...]

    def __init__(self, *facets: Facet) -> None:
        self.facets = list(facets)

    def __str__(self) -> str:
        facets_as_str = "],[".join(map(str, self.facets))
        return f'[{facets_as_str}]'

    def __and__(self, other: Facet) -> "FacetAnd":
        return FacetAnd(*self.facets, other)


class Facets:
    facets: list[Facet, FacetAnd, FacetOr, ...]

    def __init__(self, *facets: Union[Facet, FacetAnd, FacetOr]):
        self.facets = list(facets)

    def __str__(self):
        facets_as_str = ",".join(map(lambda f: f'[{f}]' if type(f) == Facet else str(f), self.facets))
        return f'[{facets_as_str}]'
