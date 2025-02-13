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

#include "mimir/search/algorithms/brfs.hpp"

#include "mimir/formalism/parser.hpp"
#include "mimir/search/algorithms.hpp"
#include "mimir/search/applicable_action_generators.hpp"
#include "mimir/search/axiom_evaluators.hpp"
#include "mimir/search/delete_relaxed_problem_explorator.hpp"
#include "mimir/search/grounders/grounder.hpp"
#include "mimir/search/plan.hpp"
#include "mimir/search/state_repository.hpp"

#include <gtest/gtest.h>

namespace mimir::tests
{

/// @brief Instantiate a lifted BrFS
class LiftedBrFSPlanner
{
private:
    PDDLParser m_parser;

    std::shared_ptr<Grounder> m_grounder;
    std::shared_ptr<ILiftedApplicableActionGeneratorEventHandler> m_applicable_action_generator_event_handler;
    std::shared_ptr<LiftedApplicableActionGenerator> m_applicable_action_generator;
    std::shared_ptr<ILiftedAxiomEvaluatorEventHandler> m_axiom_evaluator_event_handler;
    std::shared_ptr<LiftedAxiomEvaluator> m_axiom_evaluator;
    std::shared_ptr<StateRepository> m_state_repository;
    std::shared_ptr<IBrFSAlgorithmEventHandler> m_brfs_event_handler;

public:
    LiftedBrFSPlanner(const fs::path& domain_file, const fs::path& problem_file) :
        m_parser(PDDLParser(domain_file, problem_file)),
        m_grounder(std::make_shared<Grounder>(m_parser.get_problem(), m_parser.get_pddl_repositories())),
        m_applicable_action_generator_event_handler(std::make_shared<DefaultLiftedApplicableActionGeneratorEventHandler>()),
        m_applicable_action_generator(
            std::make_shared<LiftedApplicableActionGenerator>(m_grounder->get_action_grounder(), m_applicable_action_generator_event_handler)),
        m_axiom_evaluator_event_handler(std::make_shared<DefaultLiftedAxiomEvaluatorEventHandler>()),
        m_axiom_evaluator(std::make_shared<LiftedAxiomEvaluator>(m_grounder->get_axiom_grounder(), m_axiom_evaluator_event_handler)),
        m_state_repository(std::make_shared<StateRepository>(m_axiom_evaluator)),
        m_brfs_event_handler(std::make_shared<DefaultBrFSAlgorithmEventHandler>(false))
    {
    }

    SearchResult find_solution() { return find_solution_brfs(m_applicable_action_generator, m_state_repository, std::nullopt, m_brfs_event_handler); }

    const BrFSAlgorithmStatistics& get_algorithm_statistics() const { return m_brfs_event_handler->get_statistics(); }

    const LiftedApplicableActionGeneratorStatistics& get_applicable_action_generator_statistics() const
    {
        return m_applicable_action_generator_event_handler->get_statistics();
    }

    const LiftedAxiomEvaluatorStatistics& get_axiom_evaluator_statistics() const { return m_axiom_evaluator_event_handler->get_statistics(); }
};

/// @brief Instantiate a grounded BrFS
class GroundedBrFSPlanner
{
private:
    PDDLParser m_parser;

    std::shared_ptr<Grounder> m_grounder;
    DeleteRelaxedProblemExplorator m_delete_relaxed_problem_explorator;
    std::shared_ptr<IGroundedApplicableActionGeneratorEventHandler> m_applicable_action_generator_event_handler;
    std::shared_ptr<GroundedApplicableActionGenerator> m_applicable_action_generator;
    std::shared_ptr<IGroundedAxiomEvaluatorEventHandler> m_axiom_evaluator_event_handler;
    std::shared_ptr<GroundedAxiomEvaluator> m_axiom_evaluator;
    std::shared_ptr<StateRepository> m_state_repository;
    std::shared_ptr<IBrFSAlgorithmEventHandler> m_brfs_event_handler;

public:
    GroundedBrFSPlanner(const fs::path& domain_file, const fs::path& problem_file) :
        m_parser(PDDLParser(domain_file, problem_file)),
        m_grounder(std::make_shared<Grounder>(m_parser.get_problem(), m_parser.get_pddl_repositories())),
        m_delete_relaxed_problem_explorator(m_grounder),
        m_applicable_action_generator_event_handler(std::make_shared<DefaultGroundedApplicableActionGeneratorEventHandler>()),
        m_applicable_action_generator(
            m_delete_relaxed_problem_explorator.create_grounded_applicable_action_generator(m_applicable_action_generator_event_handler)),
        m_axiom_evaluator_event_handler(std::make_shared<DefaultGroundedAxiomEvaluatorEventHandler>()),
        m_axiom_evaluator(m_delete_relaxed_problem_explorator.create_grounded_axiom_evaluator(m_axiom_evaluator_event_handler)),
        m_state_repository(std::make_shared<StateRepository>(m_axiom_evaluator)),
        m_brfs_event_handler(std::make_shared<DefaultBrFSAlgorithmEventHandler>())
    {
    }

    SearchResult find_solution() { return find_solution_brfs(m_applicable_action_generator, m_state_repository, std::nullopt, m_brfs_event_handler); }

    const BrFSAlgorithmStatistics& get_algorithm_statistics() const { return m_brfs_event_handler->get_statistics(); }

    const GroundedApplicableActionGeneratorStatistics& get_applicable_action_generator_statistics() const
    {
        return m_applicable_action_generator_event_handler->get_statistics();
    }

    const GroundedAxiomEvaluatorStatistics& get_axiom_evaluator_statistics() const { return m_axiom_evaluator_event_handler->get_statistics(); }
};

/**
 * agricola-opt18-strips
 *
 * IPC instances are too difficult
 */

/**
 * Airport
 */

TEST(MimirTests, SearchAlgorithmsBrFSGroundedAssemblyTest)
{
    auto brfs = GroundedBrFSPlanner(fs::path(std::string(DATA_DIR) + "assembly/domain.pddl"), fs::path(std::string(DATA_DIR) + "assembly/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 1);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_fluent_ground_atoms(), 7);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_derived_ground_atoms(), 3);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_actions(), 6);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_delete_free_axioms(), 3);

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_actions(), 6);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_nodes_in_action_match_tree(), 14);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axioms(), 2);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_nodes_in_axiom_match_tree(), 2);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 3);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 1);
}

TEST(MimirTests, SearchAlgorithmsBrFSLiftedAssemblyTest)
{
    auto brfs = LiftedBrFSPlanner(fs::path(std::string(DATA_DIR) + "assembly/domain.pddl"), fs::path(std::string(DATA_DIR) + "assembly/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 1);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_hits_per_search_layer().back(), 0);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_misses_per_search_layer().back(), 3);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_hits_per_search_layer().back(), 4);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_misses_per_search_layer().back(), 2);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 3);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 1);
}

/**
 * Airport
 */

TEST(MimirTests, SearchAlgorithmsBrFSGroundedAirportTest)
{
    auto brfs = GroundedBrFSPlanner(fs::path(std::string(DATA_DIR) + "airport/domain.pddl"), fs::path(std::string(DATA_DIR) + "airport/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 8);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_fluent_ground_atoms(), 58);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_derived_ground_atoms(), 389);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_actions(), 43);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_delete_free_axioms(), 464);

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_actions(), 43);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_nodes_in_action_match_tree(), 138);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axioms(), 420);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_nodes_in_axiom_match_tree(), 26);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 20);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 18);
}

TEST(MimirTests, SearchAlgorithmsBrFSLiftedAirportTest)
{
    auto brfs = LiftedBrFSPlanner(fs::path(std::string(DATA_DIR) + "airport/domain.pddl"), fs::path(std::string(DATA_DIR) + "airport/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 8);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_hits_per_search_layer().back(), 0);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_misses_per_search_layer().back(), 20);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_hits_per_search_layer().back(), 322);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_misses_per_search_layer().back(), 350);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 20);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 18);
}

/**
 * Barman
 */

TEST(MimirTests, SearchAlgorithmsBrFSGroundedBarmanTest)
{
    auto brfs = GroundedBrFSPlanner(fs::path(std::string(DATA_DIR) + "barman/domain.pddl"), fs::path(std::string(DATA_DIR) + "barman/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 11);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_fluent_ground_atoms(), 26);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_derived_ground_atoms(), 0);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_actions(), 84);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_delete_free_axioms(), 0);

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_actions(), 84);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_nodes_in_action_match_tree(), 237);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axioms(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_nodes_in_axiom_match_tree(), 1);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 708);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 230);
}

TEST(MimirTests, SearchAlgorithmsBrFSLiftedBarmanTest)
{
    auto brfs = LiftedBrFSPlanner(fs::path(std::string(DATA_DIR) + "barman/domain.pddl"), fs::path(std::string(DATA_DIR) + "barman/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 11);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_hits_per_search_layer().back(), 668);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_misses_per_search_layer().back(), 40);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_hits_per_search_layer().back(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_misses_per_search_layer().back(), 0);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 708);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 230);
}

/**
 * Blocks 3 ops
 */

TEST(MimirTests, SearchAlgorithmsBrFSGroundedBlocks3opsTest)
{
    auto brfs = GroundedBrFSPlanner(fs::path(std::string(DATA_DIR) + "blocks_3/domain.pddl"), fs::path(std::string(DATA_DIR) + "blocks_3/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 4);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_fluent_ground_atoms(), 15);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_derived_ground_atoms(), 0);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_actions(), 45);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_delete_free_axioms(), 0);

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_actions(), 45);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_nodes_in_action_match_tree(), 96);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axioms(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_nodes_in_axiom_match_tree(), 1);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 68);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 21);
}

TEST(MimirTests, SearchAlgorithmsBrFSLiftedBlocks3opsTest)
{
    auto brfs = LiftedBrFSPlanner(fs::path(std::string(DATA_DIR) + "blocks_3/domain.pddl"), fs::path(std::string(DATA_DIR) + "blocks_3/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 4);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_hits_per_search_layer().back(), 41);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_misses_per_search_layer().back(), 27);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_hits_per_search_layer().back(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_misses_per_search_layer().back(), 0);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 68);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 21);
}

/**
 * Blocks 4 ops
 */

TEST(MimirTests, SearchAlgorithmsBrFSGroundedBlocks4opsTest)
{
    auto brfs = GroundedBrFSPlanner(fs::path(std::string(DATA_DIR) + "blocks_4/domain.pddl"), fs::path(std::string(DATA_DIR) + "blocks_4/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 4);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_fluent_ground_atoms(), 19);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_derived_ground_atoms(), 0);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_actions(), 24);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_delete_free_axioms(), 0);

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_actions(), 24);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_nodes_in_action_match_tree(), 72);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axioms(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_nodes_in_axiom_match_tree(), 1);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 21);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 9);
}

TEST(MimirTests, SearchAlgorithmsBrFSLiftedBlocks4opsTest)
{
    auto brfs = LiftedBrFSPlanner(fs::path(std::string(DATA_DIR) + "blocks_4/domain.pddl"), fs::path(std::string(DATA_DIR) + "blocks_4/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 4);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_hits_per_search_layer().back(), 6);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_misses_per_search_layer().back(), 15);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_hits_per_search_layer().back(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_misses_per_search_layer().back(), 0);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 21);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 9);
}

/**
 * Childsnack
 */

TEST(MimirTests, SearchAlgorithmsBrFSGroundedChildsnackTest)
{
    auto brfs =
        GroundedBrFSPlanner(fs::path(std::string(DATA_DIR) + "childsnack/domain.pddl"), fs::path(std::string(DATA_DIR) + "childsnack/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 4);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_fluent_ground_atoms(), 8);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_derived_ground_atoms(), 0);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_actions(), 7);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_delete_free_axioms(), 0);

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_actions(), 7);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_nodes_in_action_match_tree(), 12);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axioms(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_nodes_in_axiom_match_tree(), 1);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 16);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 6);
}

TEST(MimirTests, SearchAlgorithmsBrFSLiftedChildsnackTest)
{
    auto brfs = LiftedBrFSPlanner(fs::path(std::string(DATA_DIR) + "childsnack/domain.pddl"), fs::path(std::string(DATA_DIR) + "childsnack/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 4);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_hits_per_search_layer().back(), 9);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_misses_per_search_layer().back(), 7);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_hits_per_search_layer().back(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_misses_per_search_layer().back(), 0);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 16);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 6);
}

/**
 * Delivery
 */

TEST(MimirTests, SearchAlgorithmsBrFSGroundedDeliveryTest)
{
    auto brfs = GroundedBrFSPlanner(fs::path(std::string(DATA_DIR) + "delivery/domain.pddl"), fs::path(std::string(DATA_DIR) + "delivery/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 4);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_fluent_ground_atoms(), 10);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_derived_ground_atoms(), 0);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_actions(), 16);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_delete_free_axioms(), 0);

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_actions(), 16);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_nodes_in_action_match_tree(), 32);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axioms(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_nodes_in_axiom_match_tree(), 1);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 18);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 7);
}

TEST(MimirTests, SearchAlgorithmsBrFSLiftedDeliveryTest)
{
    auto brfs = LiftedBrFSPlanner(fs::path(std::string(DATA_DIR) + "delivery/domain.pddl"), fs::path(std::string(DATA_DIR) + "delivery/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 4);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_hits_per_search_layer().back(), 6);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_misses_per_search_layer().back(), 12);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_hits_per_search_layer().back(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_misses_per_search_layer().back(), 0);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 18);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 7);
}

/**
 * Driverlog
 */

TEST(MimirTests, SearchAlgorithmsBrFSGroundedDriverlogTest)
{
    auto brfs = GroundedBrFSPlanner(fs::path(std::string(DATA_DIR) + "driverlog/domain.pddl"), fs::path(std::string(DATA_DIR) + "driverlog/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 9);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_fluent_ground_atoms(), 10);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_derived_ground_atoms(), 0);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_actions(), 14);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_delete_free_axioms(), 0);

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_actions(), 14);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_nodes_in_action_match_tree(), 28);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axioms(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_nodes_in_axiom_match_tree(), 1);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 57);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 23);
}

TEST(MimirTests, SearchAlgorithmsBrFSLiftedDriverlogTest)
{
    auto brfs = LiftedBrFSPlanner(fs::path(std::string(DATA_DIR) + "driverlog/domain.pddl"), fs::path(std::string(DATA_DIR) + "driverlog/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 9);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_hits_per_search_layer().back(), 43);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_misses_per_search_layer().back(), 14);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_hits_per_search_layer().back(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_misses_per_search_layer().back(), 0);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 57);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 23);
}

/**
 * Ferry
 */

TEST(MimirTests, SearchAlgorithmsBrFSGroundedFerryTest)
{
    auto brfs = GroundedBrFSPlanner(fs::path(std::string(DATA_DIR) + "ferry/domain.pddl"), fs::path(std::string(DATA_DIR) + "ferry/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 7);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_fluent_ground_atoms(), 9);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_derived_ground_atoms(), 0);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_actions(), 12);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_delete_free_axioms(), 0);

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_actions(), 12);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_nodes_in_action_match_tree(), 30);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axioms(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_nodes_in_axiom_match_tree(), 1);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 28);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 14);
}

TEST(MimirTests, SearchAlgorithmsBrFSLiftedFerryTest)
{
    auto brfs = LiftedBrFSPlanner(fs::path(std::string(DATA_DIR) + "ferry/domain.pddl"), fs::path(std::string(DATA_DIR) + "ferry/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 7);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_hits_per_search_layer().back(), 18);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_misses_per_search_layer().back(), 10);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_hits_per_search_layer().back(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_misses_per_search_layer().back(), 0);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 28);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 14);
}

/**
 * Grid
 */

TEST(MimirTests, SearchAlgorithmsBrFSGroundedGridTest)
{
    auto brfs = GroundedBrFSPlanner(fs::path(std::string(DATA_DIR) + "grid/domain.pddl"), fs::path(std::string(DATA_DIR) + "grid/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 4);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_fluent_ground_atoms(), 21);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_derived_ground_atoms(), 0);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_actions(), 35);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_delete_free_axioms(), 0);

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_actions(), 35);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_nodes_in_action_match_tree(), 88);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axioms(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_nodes_in_axiom_match_tree(), 1);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 18);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 7);
}

TEST(MimirTests, SearchAlgorithmsBrFSLiftedGridTest)
{
    auto brfs = LiftedBrFSPlanner(fs::path(std::string(DATA_DIR) + "grid/domain.pddl"), fs::path(std::string(DATA_DIR) + "grid/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 4);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_hits_per_search_layer().back(), 5);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_misses_per_search_layer().back(), 13);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_hits_per_search_layer().back(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_misses_per_search_layer().back(), 0);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 18);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 7);
}

/**
 * Gripper
 */

TEST(MimirTests, SearchAlgorithmsBrFSGroundedGripperTest)
{
    auto brfs = GroundedBrFSPlanner(fs::path(std::string(DATA_DIR) + "gripper/domain.pddl"), fs::path(std::string(DATA_DIR) + "gripper/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 3);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_fluent_ground_atoms(), 12);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_derived_ground_atoms(), 0);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_actions(), 20);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_delete_free_axioms(), 0);

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_actions(), 20);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_nodes_in_action_match_tree(), 48);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axioms(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_nodes_in_axiom_match_tree(), 1);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 44);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 12);
}

TEST(MimirTests, SearchAlgorithmsBrFSLiftedGripperTest)
{
    auto brfs = LiftedBrFSPlanner(fs::path(std::string(DATA_DIR) + "gripper/domain.pddl"), fs::path(std::string(DATA_DIR) + "gripper/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 3);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_hits_per_search_layer().back(), 28);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_misses_per_search_layer().back(), 16);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_hits_per_search_layer().back(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_misses_per_search_layer().back(), 0);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 44);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 12);
}

/**
 * Hiking
 */

TEST(MimirTests, SearchAlgorithmsBrFSGroundedHikingTest)
{
    auto brfs = GroundedBrFSPlanner(fs::path(std::string(DATA_DIR) + "hiking/domain.pddl"), fs::path(std::string(DATA_DIR) + "hiking/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 4);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_fluent_ground_atoms(), 12);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_derived_ground_atoms(), 0);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_actions(), 57);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_delete_free_axioms(), 0);

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_actions(), 41);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_nodes_in_action_match_tree(), 60);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axioms(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_nodes_in_axiom_match_tree(), 1);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 145);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 24);
}

TEST(MimirTests, SearchAlgorithmsBrFSLiftedHikingTest)
{
    auto brfs = LiftedBrFSPlanner(fs::path(std::string(DATA_DIR) + "hiking/domain.pddl"), fs::path(std::string(DATA_DIR) + "hiking/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 4);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_hits_per_search_layer().back(), 104);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_misses_per_search_layer().back(), 41);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_hits_per_search_layer().back(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_misses_per_search_layer().back(), 0);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 145);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 24);
}

/**
 * Logistics
 */

TEST(MimirTests, SearchAlgorithmsBrFSGroundedLogisticsTest)
{
    auto brfs = GroundedBrFSPlanner(fs::path(std::string(DATA_DIR) + "logistics/domain.pddl"), fs::path(std::string(DATA_DIR) + "logistics/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 4);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_fluent_ground_atoms(), 9);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_derived_ground_atoms(), 0);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_actions(), 14);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_delete_free_axioms(), 0);

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_actions(), 14);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_nodes_in_action_match_tree(), 26);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axioms(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_nodes_in_axiom_match_tree(), 1);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 43);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 8);
}

TEST(MimirTests, SearchAlgorithmsBrFSLiftedLogisticsTest)
{
    auto brfs = LiftedBrFSPlanner(fs::path(std::string(DATA_DIR) + "logistics/domain.pddl"), fs::path(std::string(DATA_DIR) + "logistics/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 4);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_hits_per_search_layer().back(), 30);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_misses_per_search_layer().back(), 13);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_hits_per_search_layer().back(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_misses_per_search_layer().back(), 0);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 43);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 8);
}

/**
 * Miconic
 */

TEST(MimirTests, SearchAlgorithmsBrFSGroundedMiconicTest)
{
    auto brfs = GroundedBrFSPlanner(fs::path(std::string(DATA_DIR) + "miconic/domain.pddl"), fs::path(std::string(DATA_DIR) + "miconic/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 5);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_fluent_ground_atoms(), 8);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_derived_ground_atoms(), 0);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_actions(), 6);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_delete_free_axioms(), 0);

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_actions(), 6);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_nodes_in_action_match_tree(), 14);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axioms(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_nodes_in_axiom_match_tree(), 1);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 26);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 14);
}

TEST(MimirTests, SearchAlgorithmsBrFSLiftedMiconicTest)
{
    auto brfs = LiftedBrFSPlanner(fs::path(std::string(DATA_DIR) + "miconic/domain.pddl"), fs::path(std::string(DATA_DIR) + "miconic/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 5);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_hits_per_search_layer().back(), 20);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_misses_per_search_layer().back(), 6);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_hits_per_search_layer().back(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_misses_per_search_layer().back(), 0);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 26);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 14);
}

/**
 * Miconic-fulladl
 */

TEST(MimirTests, SearchAlgorithmsBrFSGroundedMiconicFullAdlTest)
{
    auto brfs = GroundedBrFSPlanner(fs::path(std::string(DATA_DIR) + "miconic-fulladl/domain.pddl"),
                                    fs::path(std::string(DATA_DIR) + "miconic-fulladl/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 7);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_fluent_ground_atoms(), 9);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_derived_ground_atoms(), 8);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_actions(), 7);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_delete_free_axioms(), 20);

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_actions(), 10);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_nodes_in_action_match_tree(), 45);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axioms(), 16);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_nodes_in_axiom_match_tree(), 12);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 105);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 41);
}

TEST(MimirTests, SearchAlgorithmsBrFSLiftedMiconicFullAdlTest)
{
    auto brfs = LiftedBrFSPlanner(fs::path(std::string(DATA_DIR) + "miconic-fulladl/domain.pddl"),
                                  fs::path(std::string(DATA_DIR) + "miconic-fulladl/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 7);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_hits_per_search_layer().back(), 95);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_misses_per_search_layer().back(), 10);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_hits_per_search_layer().back(), 472);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_misses_per_search_layer().back(), 16);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 105);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 41);
}

/**
 * Miconic-simpleadl
 */

TEST(MimirTests, SearchAlgorithmsBrFSGroundedMiconicSimpleAdlTest)
{
    auto brfs = GroundedBrFSPlanner(fs::path(std::string(DATA_DIR) + "miconic-simpleadl/domain.pddl"),
                                    fs::path(std::string(DATA_DIR) + "miconic-simpleadl/test_problem.pddl"));

    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 4);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_fluent_ground_atoms(), 4);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_derived_ground_atoms(), 0);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_actions(), 4);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_delete_free_axioms(), 0);

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_actions(), 4);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_nodes_in_action_match_tree(), 4);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axioms(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_nodes_in_axiom_match_tree(), 1);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 8);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 4);
}

TEST(MimirTests, SearchAlgorithmsBrFSLiftedMiconicSimpleAdlTest)
{
    auto brfs = LiftedBrFSPlanner(fs::path(std::string(DATA_DIR) + "miconic-simpleadl/domain.pddl"),
                                  fs::path(std::string(DATA_DIR) + "miconic-simpleadl/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 4);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_hits_per_search_layer().back(), 4);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_misses_per_search_layer().back(), 4);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_hits_per_search_layer().back(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_misses_per_search_layer().back(), 0);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 8);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 4);
}

/**
 * Philosophers
 */

TEST(MimirTests, SearchAlgorithmsBrFSGroundedPhilosophersTest)
{
    auto brfs =
        GroundedBrFSPlanner(fs::path(std::string(DATA_DIR) + "philosophers/domain.pddl"), fs::path(std::string(DATA_DIR) + "philosophers/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 18);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_fluent_ground_atoms(), 50);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_derived_ground_atoms(), 21);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_actions(), 34);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_delete_free_axioms(), 38);

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_actions(), 34);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_nodes_in_action_match_tree(), 132);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axioms(), 34);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_nodes_in_axiom_match_tree(), 94);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 210);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 125);
}

TEST(MimirTests, SearchAlgorithmsBrFSLiftedPhilosophersTest)
{
    auto brfs =
        LiftedBrFSPlanner(fs::path(std::string(DATA_DIR) + "philosophers/domain.pddl"), fs::path(std::string(DATA_DIR) + "philosophers/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 18);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_hits_per_search_layer().back(), 184);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_misses_per_search_layer().back(), 26);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_hits_per_search_layer().back(), 1414);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_misses_per_search_layer().back(), 22);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 210);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 125);
}

/**
 * Reward
 */

TEST(MimirTests, SearchAlgorithmsBrFSGroundedRewardTest)
{
    auto brfs = GroundedBrFSPlanner(fs::path(std::string(DATA_DIR) + "reward/domain.pddl"), fs::path(std::string(DATA_DIR) + "reward/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 4);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_fluent_ground_atoms(), 7);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_derived_ground_atoms(), 0);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_actions(), 6);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_delete_free_axioms(), 0);

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_actions(), 6);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_nodes_in_action_match_tree(), 10);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axioms(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_nodes_in_axiom_match_tree(), 1);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 12);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 7);
}

TEST(MimirTests, SearchAlgorithmsBrFSLiftedRewardTest)
{
    auto brfs = LiftedBrFSPlanner(fs::path(std::string(DATA_DIR) + "reward/domain.pddl"), fs::path(std::string(DATA_DIR) + "reward/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 4);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_hits_per_search_layer().back(), 6);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_misses_per_search_layer().back(), 6);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_hits_per_search_layer().back(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_misses_per_search_layer().back(), 0);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 12);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 7);
}

/**
 * Rovers
 */

TEST(MimirTests, SearchAlgorithmsBrFSGroundedRoversTest)
{
    auto brfs = GroundedBrFSPlanner(fs::path(std::string(DATA_DIR) + "rovers/domain.pddl"), fs::path(std::string(DATA_DIR) + "rovers/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 4);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_fluent_ground_atoms(), 12);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_derived_ground_atoms(), 0);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_actions(), 7);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_delete_free_axioms(), 0);

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_actions(), 7);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_nodes_in_action_match_tree(), 17);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axioms(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_nodes_in_axiom_match_tree(), 1);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 24);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 10);
}

TEST(MimirTests, SearchAlgorithmsBrFSLiftedRoversTest)
{
    auto brfs = LiftedBrFSPlanner(fs::path(std::string(DATA_DIR) + "rovers/domain.pddl"), fs::path(std::string(DATA_DIR) + "rovers/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 4);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_hits_per_search_layer().back(), 17);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_misses_per_search_layer().back(), 7);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_hits_per_search_layer().back(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_misses_per_search_layer().back(), 0);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 24);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 10);
}

/**
 * Satellite
 */

TEST(MimirTests, SearchAlgorithmsBrFSGroundedSatelliteTest)
{
    auto brfs = GroundedBrFSPlanner(fs::path(std::string(DATA_DIR) + "satellite/domain.pddl"), fs::path(std::string(DATA_DIR) + "satellite/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 7);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_fluent_ground_atoms(), 12);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_derived_ground_atoms(), 0);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_actions(), 18);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_delete_free_axioms(), 0);

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_actions(), 18);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_nodes_in_action_match_tree(), 21);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axioms(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_nodes_in_axiom_match_tree(), 1);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 303);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 56);
}

TEST(MimirTests, SearchAlgorithmsBrFSLiftedSatelliteTest)
{
    auto brfs = LiftedBrFSPlanner(fs::path(std::string(DATA_DIR) + "satellite/domain.pddl"), fs::path(std::string(DATA_DIR) + "satellite/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 7);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_hits_per_search_layer().back(), 285);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_misses_per_search_layer().back(), 18);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_hits_per_search_layer().back(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_misses_per_search_layer().back(), 0);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 303);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 56);
}

/**
 * Schedule
 */

TEST(MimirTests, SearchAlgorithmsBrFSGroundedScheduleTest)
{
    auto brfs = GroundedBrFSPlanner(fs::path(std::string(DATA_DIR) + "schedule/domain.pddl"), fs::path(std::string(DATA_DIR) + "schedule/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 2);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_fluent_ground_atoms(), 45);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_derived_ground_atoms(), 0);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_actions(), 49);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_delete_free_axioms(), 0);

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_actions(), 49);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_nodes_in_action_match_tree(), 144);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axioms(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_nodes_in_axiom_match_tree(), 1);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 884);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 45);
}

TEST(MimirTests, SearchAlgorithmsBrFSLiftedScheduleTest)
{
    auto brfs = LiftedBrFSPlanner(fs::path(std::string(DATA_DIR) + "schedule/domain.pddl"), fs::path(std::string(DATA_DIR) + "schedule/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 2);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_hits_per_search_layer().back(), 839);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_misses_per_search_layer().back(), 45);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_hits_per_search_layer().back(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_misses_per_search_layer().back(), 0);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 884);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 45);
}

/**
 * Spanner
 */

TEST(MimirTests, SearchAlgorithmsBrFSGroundedSpannerTest)
{
    auto brfs = GroundedBrFSPlanner(fs::path(std::string(DATA_DIR) + "spanner/domain.pddl"), fs::path(std::string(DATA_DIR) + "spanner/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 4);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_fluent_ground_atoms(), 9);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_derived_ground_atoms(), 0);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_actions(), 4);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_delete_free_axioms(), 0);

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_actions(), 4);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_nodes_in_action_match_tree(), 12);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axioms(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_nodes_in_axiom_match_tree(), 1);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 5);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 5);
}

TEST(MimirTests, SearchAlgorithmsBrFSLiftedSpannerTest)
{
    auto brfs = LiftedBrFSPlanner(fs::path(std::string(DATA_DIR) + "spanner/domain.pddl"), fs::path(std::string(DATA_DIR) + "spanner/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 4);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_hits_per_search_layer().back(), 1);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_misses_per_search_layer().back(), 4);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_hits_per_search_layer().back(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_misses_per_search_layer().back(), 0);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 5);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 5);
}

/**
 * Transport
 */

TEST(MimirTests, SearchAlgorithmsBrFSGroundedTransportTest)
{
    auto brfs = GroundedBrFSPlanner(fs::path(std::string(DATA_DIR) + "transport/domain.pddl"), fs::path(std::string(DATA_DIR) + "transport/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 5);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_fluent_ground_atoms(), 26);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_derived_ground_atoms(), 0);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_actions(), 104);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_delete_free_axioms(), 0);

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_actions(), 104);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_nodes_in_action_match_tree(), 246);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axioms(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_nodes_in_axiom_match_tree(), 1);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 384);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 85);
}

TEST(MimirTests, SearchAlgorithmsBrFSLiftedTransportTest)
{
    auto brfs = LiftedBrFSPlanner(fs::path(std::string(DATA_DIR) + "transport/domain.pddl"), fs::path(std::string(DATA_DIR) + "transport/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 5);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_hits_per_search_layer().back(), 332);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_misses_per_search_layer().back(), 52);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_hits_per_search_layer().back(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_misses_per_search_layer().back(), 0);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 384);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 85);
}

/**
 * Visitall
 */

TEST(MimirTests, SearchAlgorithmsBrFSGroundedVisitallTest)
{
    auto brfs = GroundedBrFSPlanner(fs::path(std::string(DATA_DIR) + "visitall/domain.pddl"), fs::path(std::string(DATA_DIR) + "visitall/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 8);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_fluent_ground_atoms(), 14);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_derived_ground_atoms(), 0);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_actions(), 12);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_delete_free_axioms(), 0);

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_actions(), 12);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_nodes_in_action_match_tree(), 14);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axioms(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_nodes_in_axiom_match_tree(), 1);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 77);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 41);
}

TEST(MimirTests, SearchAlgorithmsBrFSLiftedVisitallTest)
{
    auto brfs = LiftedBrFSPlanner(fs::path(std::string(DATA_DIR) + "visitall/domain.pddl"), fs::path(std::string(DATA_DIR) + "visitall/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 8);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_hits_per_search_layer().back(), 65);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_misses_per_search_layer().back(), 12);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_hits_per_search_layer().back(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_misses_per_search_layer().back(), 0);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 77);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 41);
}

/**
 * Woodworking
 */

TEST(MimirTests, SearchAlgorithmsBrFSGroundedWoodworkingTest)
{
    auto brfs =
        GroundedBrFSPlanner(fs::path(std::string(DATA_DIR) + "woodworking/domain.pddl"), fs::path(std::string(DATA_DIR) + "woodworking/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 2);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_fluent_ground_atoms(), 19);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_reachable_derived_ground_atoms(), 0);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_delete_free_actions(), 57);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_delete_free_axioms(), 0);

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_actions(), 57);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_nodes_in_action_match_tree(), 112);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axioms(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_nodes_in_axiom_match_tree(), 1);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 10);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 3);
}

TEST(MimirTests, SearchAlgorithmsBrFSLiftedWoodworkingTest)
{
    auto brfs =
        LiftedBrFSPlanner(fs::path(std::string(DATA_DIR) + "woodworking/domain.pddl"), fs::path(std::string(DATA_DIR) + "woodworking/test_problem.pddl"));
    const auto result = brfs.find_solution();
    EXPECT_EQ(result.status, SearchStatus::SOLVED);
    EXPECT_EQ(result.plan.value().get_actions().size(), 2);

    const auto& applicable_action_generator_statistics = brfs.get_applicable_action_generator_statistics();
    const auto& axiom_evaluator_statistics = brfs.get_axiom_evaluator_statistics();

    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_hits_per_search_layer().back(), 1);
    EXPECT_EQ(applicable_action_generator_statistics.get_num_ground_action_cache_misses_per_search_layer().back(), 9);

    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_hits_per_search_layer().back(), 0);
    EXPECT_EQ(axiom_evaluator_statistics.get_num_ground_axiom_cache_misses_per_search_layer().back(), 0);

    const auto& brfs_statistics = brfs.get_algorithm_statistics();

    EXPECT_EQ(brfs_statistics.get_num_generated_until_g_value().back(), 10);
    EXPECT_EQ(brfs_statistics.get_num_expanded_until_g_value().back(), 3);
}

}
