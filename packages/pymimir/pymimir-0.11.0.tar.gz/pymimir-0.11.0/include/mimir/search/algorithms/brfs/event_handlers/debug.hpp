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

#ifndef MIMIR_SEARCH_ALGORITHMS_BRFS_EVENT_HANDLERS_DEBUG_HPP_
#define MIMIR_SEARCH_ALGORITHMS_BRFS_EVENT_HANDLERS_DEBUG_HPP_

#include "mimir/search/algorithms/brfs/event_handlers/interface.hpp"

#include <iostream>

namespace mimir
{

/**
 * Implementation class
 */
class DebugBrFSAlgorithmEventHandler : public BrFSAlgorithmEventHandlerBase<DebugBrFSAlgorithmEventHandler>
{
private:
    /* Implement AlgorithmEventHandlerBase interface */
    friend class BrFSAlgorithmEventHandlerBase<DebugBrFSAlgorithmEventHandler>;

    void on_expand_state_impl(State state, Problem problem, const PDDLRepositories& pddl_repositories) const;

    void on_generate_state_impl(State state, GroundAction action, Problem problem, const PDDLRepositories& pddl_repositories) const;

    void on_generate_state_in_search_tree_impl(State state, GroundAction action, Problem problem, const PDDLRepositories& pddl_repositories) const;

    void on_generate_state_not_in_search_tree_impl(State state, GroundAction action, Problem problem, const PDDLRepositories& pddl_repositories) const;

    void on_finish_g_layer_impl(uint32_t g_value, uint64_t num_expanded_states, uint64_t num_generated_states) const;

    void on_prune_state_impl(State state, Problem problem, const PDDLRepositories& pddl_repositories) const;

    void on_start_search_impl(State start_state, Problem problem, const PDDLRepositories& pddl_repositories) const;

    void on_end_search_impl(uint64_t num_reached_fluent_atoms,
                            uint64_t num_reached_derived_atoms,
                            uint64_t num_bytes_for_unextended_state_portion,
                            uint64_t num_bytes_for_extended_state_portion,
                            uint64_t num_bytes_for_nodes,
                            uint64_t num_bytes_for_actions,
                            uint64_t num_bytes_for_axioms,
                            uint64_t num_states,
                            uint64_t num_nodes,
                            uint64_t num_actions,
                            uint64_t num_axioms) const;

    void on_solved_impl(const Plan& plan, const PDDLRepositories& pddl_repositories) const;

    void on_unsolvable_impl() const;

    void on_exhausted_impl() const;

public:
    explicit DebugBrFSAlgorithmEventHandler(bool quiet = true) : BrFSAlgorithmEventHandlerBase<DebugBrFSAlgorithmEventHandler>(quiet) {}
};

}

#endif
