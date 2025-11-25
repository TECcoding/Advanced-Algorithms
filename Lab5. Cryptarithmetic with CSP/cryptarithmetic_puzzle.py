#----------------------------------------------------------
# Lab #5: Cryptarithmetic with CSP
# General cryptarithmetic puzzle solver.
#
# Date: 17-Oct-2025
# Authors:
#           A01801044 Yael Sinuhe Grajeda Martinez
#           A01800840 Tadeo Emanuel Arellano Conde
#----------------------------------------------------------
from __future__ import annotations
from typing import Dict, List, Optional, Set

from csp import Constraint, CSP

def _to_upper_words(words: List[str]) -> List[str]:
    return [w.upper() for w in words]


def _unique_sorted_letters(addends: List[str], answer: str) -> List[str]:
    letters: Set[str] = set("".join(addends) + answer)
    return sorted(letters)


class AllDifferentConstraint(Constraint[str, int]):
    def __init__(self, variables: List[str]) -> None:
        super().__init__(variables)

    def satisfied(self, assignment: Dict[str, int]) -> bool:
        seen: Set[int] = set()
        for v in self.variables:
            if v in assignment:
                val = assignment[v]
                if val in seen:
                    return False
                seen.add(val)
        return True

class AlphameticSumConstraint(Constraint[str, int]):
    def __init__(self, addends: List[str], answer: str, variables: List[str]) -> None:
        super().__init__(variables)
        self.addends = addends
        self.answer = answer

    def _fully_assigned(self, a: Dict[str, int]) -> bool:
        return all(v in a for v in self.variables)

    def _word_value(self, w: str, a: Dict[str, int]) -> int:
        return int("".join(str(a[ch]) for ch in w))

    def satisfied(self, assignment: Dict[str, int]) -> bool:
        if not self._fully_assigned(assignment):
            return True
        total = sum(self._word_value(w, assignment) for w in self.addends)
        return total == self._word_value(self.answer, assignment)

def solve_cryptarithmetic_puzzle(
    addends: List[str],
    answer: str) -> Dict[str, int] | None:

    add_u = _to_upper_words(addends)
    ans_u = answer.upper()

    variables = _unique_sorted_letters(add_u, ans_u)

    all_digits = list(range(10))
    domains: Dict[str, List[int]] = {v: all_digits[:] for v in variables}

    csp = CSP(variables, domains)
    csp.add_constraint(AllDifferentConstraint(variables))
    csp.add_constraint(AlphameticSumConstraint(add_u, ans_u, variables))

    solution: Optional[Dict[str, int]] = csp.backtracking_search()
    return solution
