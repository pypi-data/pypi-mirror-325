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

#include "mimir/search/axiom_evaluators/lifted.hpp"

#include "mimir/formalism/existentially_quantified_conjunctive_condition.hpp"
#include "mimir/formalism/repositories.hpp"
#include "mimir/search/axiom_evaluators/lifted/event_handlers.hpp"
#include "mimir/search/dense_state.hpp"
#include "mimir/search/grounders/axiom_grounder.hpp"

namespace mimir
{
LiftedAxiomEvaluator::LiftedAxiomEvaluator(std::shared_ptr<AxiomGrounder> axiom_grounder) :
    LiftedAxiomEvaluator(std::move(axiom_grounder), std::make_shared<DefaultLiftedAxiomEvaluatorEventHandler>())
{
}

LiftedAxiomEvaluator::LiftedAxiomEvaluator(std::shared_ptr<AxiomGrounder> axiom_grounder, std::shared_ptr<ILiftedAxiomEvaluatorEventHandler> event_handler) :
    m_grounder(axiom_grounder),
    m_event_handler(event_handler),
    m_condition_grounders(),
    m_partitioning(compute_axiom_partitioning(m_grounder->get_problem()->get_problem_and_domain_axioms(),
                                              m_grounder->get_problem()->get_problem_and_domain_derived_predicates())),
    m_fluent_atoms(),
    m_derived_atoms(),
    m_fluent_assignment_set(m_grounder->get_problem()->get_objects().size(), m_grounder->get_problem()->get_domain()->get_predicates<Fluent>()),
    m_derived_assignment_set(m_grounder->get_problem()->get_objects().size(), m_grounder->get_problem()->get_problem_and_domain_derived_predicates())
{
    /* 3. Initialize condition grounders */
    for (const auto& axiom : m_grounder->get_problem()->get_problem_and_domain_axioms())
    {
        m_condition_grounders.emplace(axiom, SatisficingBindingGenerator(m_grounder->get_literal_grounder(), axiom->get_precondition()));
    }
}

void LiftedAxiomEvaluator::generate_and_apply_axioms(DenseState& dense_state)
{
    const auto& dense_fluent_atoms = dense_state.get_atoms<Fluent>();
    auto& dense_derived_atoms = dense_state.get_atoms<Derived>();

    /* 1. Initialize assignment set */

    m_event_handler->on_start_generating_applicable_axioms();

    m_grounder->get_pddl_repositories()->get_ground_atoms_from_indices(dense_fluent_atoms, m_fluent_atoms);
    m_fluent_assignment_set.clear();
    m_fluent_assignment_set.insert_ground_atoms(m_fluent_atoms);

    m_grounder->get_pddl_repositories()->get_ground_atoms_from_indices(dense_derived_atoms, m_derived_atoms);
    m_derived_assignment_set.clear();
    m_derived_assignment_set.insert_ground_atoms(m_derived_atoms);

    /* 2. Fixed point computation */

    auto applicable_axioms = GroundAxiomList {};

    for (const auto& partition : m_partitioning)
    {
        bool reached_partition_fixed_point;

        // TODO: Optimization 4: Inductively compile away axioms with static bodies. (grounded in match tree?)

        // Optimization 2: Track axioms that might trigger in next iteration.
        // Optimization 3: Use precomputed set of axioms that might be applicable initially
        auto relevant_axioms = partition.get_initially_relevant_axioms();

        do
        {
            reached_partition_fixed_point = true;

            /* Compute applicable axioms */

            applicable_axioms.clear();
            for (const auto& axiom : relevant_axioms)
            {
                // We move this check here to avoid unnecessary creations of mimir::generator.
                if (!nullary_conditions_hold(axiom->get_precondition(), dense_state))
                {
                    continue;
                }

                auto& condition_grounder = m_condition_grounders.at(axiom);

                for (auto&& binding : condition_grounder.create_binding_generator(dense_state, m_fluent_assignment_set, m_derived_assignment_set))
                {
                    const auto num_ground_axioms = m_grounder->get_num_ground_axioms();

                    const auto ground_axiom = m_grounder->ground_axiom(axiom, std::move(binding));

                    assert(ground_axiom->is_applicable(m_grounder->get_problem(), dense_state));

                    m_event_handler->on_ground_axiom(ground_axiom);

                    (m_grounder->get_num_ground_axioms() > num_ground_axioms) ? m_event_handler->on_ground_axiom_cache_miss(ground_axiom) :
                                                                                m_event_handler->on_ground_axiom_cache_hit(ground_axiom);

                    applicable_axioms.emplace_back(ground_axiom);
                }
            }

            /* Apply applicable axioms */

            relevant_axioms.clear();

            for (const auto& grounded_axiom : applicable_axioms)
            {
                assert(!grounded_axiom->get_derived_effect().is_negated);

                const auto grounded_atom_index = grounded_axiom->get_derived_effect().atom_index;

                if (!dense_derived_atoms.get(grounded_atom_index))
                {
                    // GENERATED NEW DERIVED ATOM!
                    const auto new_ground_atom = m_grounder->get_pddl_repositories()->get_ground_atom<Derived>(grounded_atom_index);
                    reached_partition_fixed_point = false;

                    // Update the assignment set
                    m_derived_assignment_set.insert_ground_atom(new_ground_atom);
                    dense_derived_atoms.set(grounded_atom_index);

                    // Retrieve relevant axioms
                    partition.retrieve_axioms_with_same_body_predicate(new_ground_atom, relevant_axioms);
                }
            }
        } while (!reached_partition_fixed_point);
    }

    m_event_handler->on_end_generating_applicable_axioms();
}

void LiftedAxiomEvaluator::on_finish_search_layer() { m_event_handler->on_finish_search_layer(); }

void LiftedAxiomEvaluator::on_end_search() { m_event_handler->on_end_search(); }

Problem LiftedAxiomEvaluator::get_problem() const { return m_grounder->get_problem(); }

const std::shared_ptr<PDDLRepositories>& LiftedAxiomEvaluator::get_pddl_repositories() const { return m_grounder->get_pddl_repositories(); }

const std::shared_ptr<AxiomGrounder>& LiftedAxiomEvaluator::get_axiom_grounder() const { return m_grounder; }

const std::shared_ptr<ILiftedAxiomEvaluatorEventHandler>& LiftedAxiomEvaluator::get_event_handler() const { return m_event_handler; }

const std::vector<AxiomPartition>& LiftedAxiomEvaluator::get_axiom_partitioning() const { return m_partitioning; }
}
