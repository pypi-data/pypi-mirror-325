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

#ifndef MIMIR_SEARCH_APPLICABLE_ACTION_GENERATORS_GROUNDED_EVENT_HANDLERS_INTERFACE_HPP_
#define MIMIR_SEARCH_APPLICABLE_ACTION_GENERATORS_GROUNDED_EVENT_HANDLERS_INTERFACE_HPP_

#include "mimir/formalism/declarations.hpp"
#include "mimir/search/applicable_action_generators/grounded/event_handlers/statistics.hpp"
#include "mimir/search/declarations.hpp"
#include "mimir/search/match_tree.hpp"

namespace mimir
{
template<typename T>
class MatchTree;

/**
 * Interface class
 */
class IGroundedApplicableActionGeneratorEventHandler
{
public:
    virtual ~IGroundedApplicableActionGeneratorEventHandler() = default;

    /// @brief React on finishing delete-free exploration
    virtual void on_finish_delete_free_exploration(const GroundAtomList<Fluent>& reached_fluent_atoms,
                                                   const GroundAtomList<Derived>& reached_derived_atoms,
                                                   const GroundActionList& instantiated_actions) = 0;

    virtual void on_finish_grounding_unrelaxed_actions(const GroundActionList& unrelaxed_actions) = 0;

    virtual void on_finish_build_action_match_tree(const MatchTree<GroundAction>& action_match_tree) = 0;

    virtual void on_finish_search_layer() = 0;

    virtual void on_end_search() = 0;

    virtual const GroundedApplicableActionGeneratorStatistics& get_statistics() const = 0;
};

/**
 * Base class
 *
 * Collect statistics and call implementation of derived class.
 */
template<typename Derived_>
class GroundedApplicableActionGeneratorEventHandlerBase : public IGroundedApplicableActionGeneratorEventHandler
{
protected:
    GroundedApplicableActionGeneratorStatistics m_statistics;
    bool m_quiet;

private:
    GroundedApplicableActionGeneratorEventHandlerBase() = default;
    friend Derived_;

    /// @brief Helper to cast to Derived.
    constexpr const auto& self() const { return static_cast<const Derived_&>(*this); }
    constexpr auto& self() { return static_cast<Derived_&>(*this); }

public:
    explicit GroundedApplicableActionGeneratorEventHandlerBase(bool quiet = true) : m_statistics(), m_quiet(quiet) {}

    void on_finish_delete_free_exploration(const GroundAtomList<Fluent>& reached_fluent_atoms,
                                           const GroundAtomList<Derived>& reached_derived_atoms,
                                           const GroundActionList& instantiated_actions) override
    {  //
        m_statistics.set_num_delete_free_reachable_fluent_ground_atoms(reached_fluent_atoms.size());
        m_statistics.set_num_delete_free_reachable_derived_ground_atoms(reached_derived_atoms.size());
        m_statistics.set_num_delete_free_actions(instantiated_actions.size());

        if (!m_quiet)
        {
            self().on_finish_delete_free_exploration_impl(reached_fluent_atoms, reached_derived_atoms, instantiated_actions);
        }
    }

    void on_finish_grounding_unrelaxed_actions(const GroundActionList& unrelaxed_actions) override
    {  //
        m_statistics.set_num_ground_actions(unrelaxed_actions.size());

        if (!m_quiet)
        {
            self().on_finish_grounding_unrelaxed_actions_impl(unrelaxed_actions);
        }
    }

    void on_finish_build_action_match_tree(const MatchTree<GroundAction>& action_match_tree) override
    {  //
        m_statistics.set_num_nodes_in_action_match_tree(action_match_tree.get_num_nodes());

        if (!m_quiet)
        {
            self().on_finish_build_action_match_tree_impl(action_match_tree);
        }
    }

    void on_finish_search_layer() override
    {  //
        if (!m_quiet)
        {
            self().on_finish_search_layer_impl();
        }
    }

    void on_end_search() override
    {  //
        if (!m_quiet)
        {
            self().on_end_search_impl();
        }
    }

    const GroundedApplicableActionGeneratorStatistics& get_statistics() const override { return m_statistics; }
};
}

#endif
