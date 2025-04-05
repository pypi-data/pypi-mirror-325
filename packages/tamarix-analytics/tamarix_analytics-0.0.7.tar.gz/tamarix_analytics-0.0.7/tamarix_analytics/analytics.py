from __future__ import annotations
from typing import Sequence, Tuple
from munkres import Munkres  # type: ignore
from pydantic import BaseModel


def match_rows(
    tentative_data: list[BaseModel],
    baseline_data: list[BaseModel],
) -> Sequence[Tuple[int, int]]:
    """
    Finds the optimal assignment of rows between two tables using the Hungarian algorithm.
    The output is a list of tuples (i, j) where i is the index of a row in the approved table and j is the index of a row in the tentative table.

    The optimal assignment is invariant to the order of the rows in the tables.
    This allows us to make a comparison between tables even if the order/number of rows is different.
    """
    cost_matrix = []
    for row_a in tentative_data:
        row = []
        for row_b in baseline_data:
            cost = 0
            for field_name in row_a.model_fields.keys():
                tentative_value = getattr(row_a, field_name)
                baseline_value = getattr(row_b, field_name)
                if baseline_value != tentative_value:
                    cost += 1
            row.append(cost)
        cost_matrix.append(row)

    # Apply the Hungarian algorithm to find the optimal assignment
    m = Munkres()
    indexes = list(m.compute(cost_matrix))

    # Pad indexes with None values for unassigned indexes
    for i in range(len(tentative_data)):
        if i not in [index[0] for index in indexes]:
            indexes.append((i, None))
    for j in range(len(baseline_data)):
        if j not in [index[1] for index in indexes]:
            indexes.append((None, j))

    return indexes


def f1_score_unordered(
    tentative_data: list[BaseModel],
    baseline_data: list[BaseModel],
) -> float:
    """
    Calculates the f1 score between two tables.
    The f1 score is the harmonic mean of precision and recall.
    """

    if not baseline_data:
        raise ValueError("baseline_data cannot be empty")
    if not tentative_data:
        return 0.0

    tp = fp = fn = 0
    reference_values = [value for row in baseline_data for value in row.model_dump().values()]
    tentative_values = [value for row in tentative_data for value in row.model_dump().values()]

    fn = sum(1 for value in reference_values if value is not None) - sum(1 for value in tentative_values if value is not None)
    fn = max(0, fn)
    for value in tentative_values:
        if value in reference_values:
            reference_values.remove(value)
            tp += 1
        elif value is None:
            continue
        else:
            fp += 1

    precision = tp / (tp + fp) if tp + fp > 0 else 0
    recall = tp / (tp + fn) if tp + fn > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if precision + recall > 0 else 0
    return f1_score


def f1_score_ordered(
    tentative_data: list[BaseModel],
    baseline_data: list[BaseModel],
) -> float:
    """
    returns the f1 score where values are checked with consideration to the structure and order of the tables
    being compared.
    """

    if not baseline_data:
        raise ValueError("baseline_data cannot be empty")
    if not tentative_data:
        return 0.0

    def create_empty_row_from_model(instance: BaseModel) -> BaseModel:
        field_names = instance.model_fields.keys()
        return type(instance).model_construct(**{field_name: None for field_name in field_names})

    indexes = match_rows(tentative_data, baseline_data)
    tp = fn = fp = 0
    for i, j in indexes:
        if i is None and j is None:
            raise ValueError("Both tentative_row and approved_row cannot be None")

        if j is None:
            approved_row = create_empty_row_from_model(tentative_data[i])
        else:
            approved_row = baseline_data[j]

        if i is None:
            tentative_row = create_empty_row_from_model(baseline_data[j])
        else:
            tentative_row = tentative_data[i]

        if approved_row.model_fields.keys() != tentative_row.model_fields.keys():
            raise ValueError("Field names of tentative_row and approved_row must match")

        for field_name in tentative_row.model_fields.keys():
            tentative_value = getattr(tentative_row, field_name)
            baseline_value = getattr(approved_row, field_name)

            if tentative_value is not None and baseline_value is not None:
                if tentative_value == baseline_value:
                    tp += 1
                else:
                    fp += 1
            elif tentative_value is None and baseline_value is not None:
                fn += 1
            elif tentative_value is not None and baseline_value is None:
                fp += 1

    precision = tp / (tp + fp) if tp + fp > 0 else 0
    recall = tp / (tp + fn) if tp + fn > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if precision + recall > 0 else 0
    return f1_score


def get_row_score(
    tentative_data: list[BaseModel],
    baseline_data: list[BaseModel],
) -> float:
    num_baseline_rows = len(baseline_data)
    num_tentative_rows = len(tentative_data)

    return num_tentative_rows / num_baseline_rows
