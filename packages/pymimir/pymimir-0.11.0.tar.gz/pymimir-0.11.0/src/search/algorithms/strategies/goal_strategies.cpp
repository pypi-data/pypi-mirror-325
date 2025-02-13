/*
 * Copyright (C) 2023 Dominik Drexler and Simon Stahlberg
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program. If not, see <https://www.gnu.org/licenses/>.
 */

#include "mimir/formalism/problem.hpp"
#include "mimir/search/algorithms/strategies/goal_strategy.hpp"

namespace mimir
{
ProblemGoal::ProblemGoal(Problem problem) : m_problem(problem) {}

bool ProblemGoal::test_static_goal() { return m_problem->static_goal_holds(); }

bool ProblemGoal::test_dynamic_goal(State state)
{
    // This uses the efficient check.
    return state->literals_hold<Fluent>(m_problem->get_positive_goal_atoms_indices<Fluent>(), m_problem->get_negative_goal_atoms_indices<Fluent>())
           && state->literals_hold<Derived>(m_problem->get_positive_goal_atoms_indices<Derived>(), m_problem->get_negative_goal_atoms_indices<Derived>());
}
}
