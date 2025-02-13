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

#ifndef MIMIR_FORMALISM_TRANSLATORS_BASE_RECURSE_HPP_
#define MIMIR_FORMALISM_TRANSLATORS_BASE_RECURSE_HPP_

#include "mimir/formalism/translators/interface.hpp"

#include <deque>
#include <loki/loki.hpp>
#include <unordered_map>

namespace mimir
{

/**
 * Base implementation recursively calls translate.
 */
template<typename Derived_>
class BaseRecurseTranslator : public ITranslator<BaseRecurseTranslator<Derived_>>
{
private:
    BaseRecurseTranslator() = default;
    friend Derived_;

    /// @brief Helper to cast to Derived_.
    constexpr const auto& self() const { return static_cast<const Derived_&>(*this); }
    constexpr auto& self() { return static_cast<Derived_&>(*this); }

protected:
    loki::PDDLRepositories& m_pddl_repositories;

    explicit BaseRecurseTranslator(loki::PDDLRepositories& pddl_repositories) : m_pddl_repositories(pddl_repositories) {}

protected:
    /* Implement ITranslator interface */
    friend class ITranslator<BaseRecurseTranslator<Derived_>>;

    template<std::ranges::forward_range Range>
    void prepare_base(const Range& input)
    {
        self().prepare_impl(input);
    }
    template<std::ranges::forward_range Range>
    void prepare_impl(const Range& input)
    {
        std::ranges::for_each(input, [this](auto&& arg) { this->prepare(*arg); });
    }

    template<typename T>
    void prepare_base(const T& element)
    {
        self().prepare_impl(element);
    }

    void prepare_impl(const loki::RequirementsImpl& requirements) {}
    void prepare_impl(const loki::TypeImpl& type) { this->prepare(type.get_bases()); }
    void prepare_impl(const loki::ObjectImpl& object) { this->prepare(object.get_bases()); }
    void prepare_impl(const loki::VariableImpl& variable) {}
    void prepare_impl(const loki::TermImpl& term)
    {
        std::visit([this](auto&& arg) { return this->prepare(*arg); }, term.get_object_or_variable());
    }
    void prepare_impl(const loki::ParameterImpl& parameter) { this->prepare(*parameter.get_variable()); }
    void prepare_impl(const loki::PredicateImpl& predicate) { this->prepare(predicate.get_parameters()); }
    void prepare_impl(const loki::AtomImpl& atom)
    {
        this->prepare(*atom.get_predicate());
        this->prepare(atom.get_terms());
    }
    void prepare_impl(const loki::LiteralImpl& literal) { this->prepare(*literal.get_atom()); }
    void prepare_impl(const loki::FunctionValueImpl& function_value) { this->prepare(*function_value.get_function()); }
    void prepare_impl(const loki::ConditionLiteralImpl& condition) { this->prepare(*condition.get_literal()); }
    void prepare_impl(const loki::ConditionAndImpl& condition) { this->prepare(condition.get_conditions()); }
    void prepare_impl(const loki::ConditionOrImpl& condition) { this->prepare(condition.get_conditions()); }
    void prepare_impl(const loki::ConditionNotImpl& condition) { this->prepare(*condition.get_condition()); }
    void prepare_impl(const loki::ConditionImplyImpl& condition)
    {
        this->prepare(*condition.get_condition_left());
        this->prepare(*condition.get_condition_right());
    }
    void prepare_impl(const loki::ConditionExistsImpl& condition)
    {
        this->prepare(condition.get_parameters());
        this->prepare(*condition.get_condition());
    }
    void prepare_impl(const loki::ConditionForallImpl& condition)
    {
        this->prepare(condition.get_parameters());
        this->prepare(*condition.get_condition());
    }
    void prepare_impl(const loki::ConditionNumericConstraintImpl& condition)
    {
        this->prepare(*condition.get_function_expression_left());
        this->prepare(*condition.get_function_expression_right());
    }
    void prepare_impl(const loki::ConditionImpl& condition)
    {
        std::visit([this](auto&& arg) { return this->prepare(*arg); }, condition.get_condition());
    }
    void prepare_impl(const loki::EffectLiteralImpl& effect) { this->prepare(*effect.get_literal()); }
    void prepare_impl(const loki::EffectAndImpl& effect) { this->prepare(effect.get_effects()); }
    void prepare_impl(const loki::EffectNumericImpl& effect)
    {
        this->prepare(*effect.get_function());
        this->prepare(*effect.get_function_expression());
    }
    void prepare_impl(const loki::EffectCompositeForallImpl& effect)
    {
        this->prepare(effect.get_parameters());
        this->prepare(*effect.get_effect());
    }
    void prepare_impl(const loki::EffectCompositeWhenImpl& effect)
    {
        this->prepare(*effect.get_condition());
        this->prepare(*effect.get_effect());
    }
    void prepare_impl(const loki::EffectCompositeOneofImpl& effect) { this->prepare(effect.get_effects()); }
    void prepare_impl(const loki::EffectCompositeProbabilisticImpl& effect)
    {
        for (const auto& [probability, effect] : effect.get_effect_distribution())
        {
            this->prepare(*effect);
        }
    }
    void prepare_impl(const loki::EffectImpl& effect)
    {
        std::visit([this](auto&& arg) { return this->prepare(*arg); }, effect.get_effect());
    }
    void prepare_impl(const loki::FunctionExpressionNumberImpl& function_expression) {}
    void prepare_impl(const loki::FunctionExpressionBinaryOperatorImpl& function_expression)
    {
        this->prepare(*function_expression.get_left_function_expression());
        this->prepare(*function_expression.get_right_function_expression());
    }
    void prepare_impl(const loki::FunctionExpressionMultiOperatorImpl& function_expression) { this->prepare(function_expression.get_function_expressions()); }
    void prepare_impl(const loki::FunctionExpressionMinusImpl& function_expression) { this->prepare(*function_expression.get_function_expression()); }
    void prepare_impl(const loki::FunctionExpressionFunctionImpl& function_expression) { this->prepare(*function_expression.get_function()); }
    void prepare_impl(const loki::FunctionExpressionImpl& function_expression)
    {
        std::visit([this](auto&& arg) { return this->prepare(*arg); }, function_expression.get_function_expression());
    }
    void prepare_impl(const loki::FunctionSkeletonImpl& function_skeleton)
    {
        this->prepare(function_skeleton.get_parameters());
        this->prepare(*function_skeleton.get_type());
    }
    void prepare_impl(const loki::FunctionImpl& function)
    {
        this->prepare(*function.get_function_skeleton());
        this->prepare(function.get_terms());
    }
    void prepare_impl(const loki::ActionImpl& action)
    {
        this->prepare(action.get_parameters());
        if (action.get_condition().has_value())
        {
            this->prepare(*action.get_condition().value());
        }
        if (action.get_effect().has_value())
        {
            this->prepare(*action.get_effect().value());
        }
    }
    void prepare_impl(const loki::AxiomImpl& axiom)
    {
        this->prepare(axiom.get_parameters());
        this->prepare(*axiom.get_condition());
    }
    void prepare_impl(const loki::DomainImpl& domain)
    {
        this->prepare(*domain.get_requirements());
        this->prepare(domain.get_types());
        this->prepare(domain.get_constants());
        this->prepare(domain.get_predicates());
        this->prepare(domain.get_functions());
        this->prepare(domain.get_actions());
        this->prepare(domain.get_axioms());
    }
    void prepare_impl(const loki::OptimizationMetricImpl& metric) { this->prepare(*metric.get_function_expression()); }
    void prepare_impl(const loki::ProblemImpl& problem)
    {
        this->prepare(*problem.get_domain());
        this->prepare(*problem.get_requirements());
        this->prepare(problem.get_objects());
        this->prepare(problem.get_derived_predicates());
        this->prepare(problem.get_initial_literals());
        this->prepare(problem.get_function_values());
        if (problem.get_goal_condition().has_value())
        {
            this->prepare(*problem.get_goal_condition().value());
        }
        if (problem.get_optimization_metric().has_value())
        {
            this->prepare(*problem.get_optimization_metric().value());
        }
        this->prepare(problem.get_axioms());
    }

    /// @brief Translate a container of elements into a container of elements.
    ///        Default behavior reparses it into the pddl_repositories.
    template<IsBackInsertibleRange Range>
    auto translate_base(const Range& input)
    {
        return self().translate_impl(input);
    }
    template<IsBackInsertibleRange Range>
    auto translate_impl(const Range& input)
    {
        std::remove_cvref_t<Range> output;

        if constexpr (requires { output.reserve(std::ranges::size(input)); })
        {
            output.reserve(std::ranges::size(input));
        }

        std::ranges::transform(input, std::back_inserter(output), [this](auto&& arg) { return this->translate(*arg); });

        return output;
    }

    /// @brief Translate a single element.
    ///        Default behavior reparses it into the pddl_repositories.
    template<typename T>
    auto translate_base(const T& element)
    {
        return self().translate_impl(element);
    }

    loki::Requirements translate_impl(const loki::RequirementsImpl& requirements)
    {
        return this->m_pddl_repositories.get_or_create_requirements(requirements.get_requirements());
    }
    loki::Type translate_impl(const loki::TypeImpl& type)
    {
        return this->m_pddl_repositories.get_or_create_type(type.get_name(), this->translate(type.get_bases()));
    }
    loki::Object translate_impl(const loki::ObjectImpl& object)
    {
        return this->m_pddl_repositories.get_or_create_object(object.get_name(), this->translate(object.get_bases()));
    }
    loki::Variable translate_impl(const loki::VariableImpl& variable) { return this->m_pddl_repositories.get_or_create_variable(variable.get_name()); }
    loki::Term translate_impl(const loki::TermImpl& term)
    {
        return std::visit([this](auto&& arg) -> loki::Term { return this->m_pddl_repositories.get_or_create_term(this->translate(*arg)); },
                          term.get_object_or_variable());
    }
    loki::Parameter translate_impl(const loki::ParameterImpl& parameter)
    {
        return this->m_pddl_repositories.get_or_create_parameter(this->translate(*parameter.get_variable()), this->translate(parameter.get_bases()));
    }
    loki::Predicate translate_impl(const loki::PredicateImpl& predicate)
    {
        return this->m_pddl_repositories.get_or_create_predicate(predicate.get_name(), this->translate(predicate.get_parameters()));
    }
    loki::Atom translate_impl(const loki::AtomImpl& atom)
    {
        return this->m_pddl_repositories.get_or_create_atom(this->translate(*atom.get_predicate()), this->translate(atom.get_terms()));
    }
    loki::Literal translate_impl(const loki::LiteralImpl& literal)
    {
        return this->m_pddl_repositories.get_or_create_literal(literal.is_negated(), this->translate(*literal.get_atom()));
    }
    loki::FunctionValue translate_impl(const loki::FunctionValueImpl& function_value)
    {
        return this->m_pddl_repositories.get_or_create_function_value(this->translate(*function_value.get_function()), function_value.get_number());
    }
    loki::Condition translate_impl(const loki::ConditionLiteralImpl& condition)
    {
        return this->m_pddl_repositories.get_or_create_condition(
            this->m_pddl_repositories.get_or_create_condition_literal(this->translate(*condition.get_literal())));
    }
    loki::Condition translate_impl(const loki::ConditionAndImpl& condition)
    {
        return this->m_pddl_repositories.get_or_create_condition(
            this->m_pddl_repositories.get_or_create_condition_and(this->translate(condition.get_conditions())));
    }
    loki::Condition translate_impl(const loki::ConditionOrImpl& condition)
    {
        return this->m_pddl_repositories.get_or_create_condition(
            this->m_pddl_repositories.get_or_create_condition_or(this->translate(condition.get_conditions())));
    }
    loki::Condition translate_impl(const loki::ConditionNotImpl& condition)
    {
        return this->m_pddl_repositories.get_or_create_condition(
            this->m_pddl_repositories.get_or_create_condition_not(this->translate(*condition.get_condition())));
    }
    loki::Condition translate_impl(const loki::ConditionImplyImpl& condition)
    {
        return this->m_pddl_repositories.get_or_create_condition(
            this->m_pddl_repositories.get_or_create_condition_imply(this->translate(*condition.get_condition_left()),
                                                                    this->translate(*condition.get_condition_right())));
    }
    loki::Condition translate_impl(const loki::ConditionExistsImpl& condition)
    {
        return this->m_pddl_repositories.get_or_create_condition(
            this->m_pddl_repositories.get_or_create_condition_exists(this->translate(condition.get_parameters()), this->translate(*condition.get_condition())));
    }
    loki::Condition translate_impl(const loki::ConditionForallImpl& condition)
    {
        return this->m_pddl_repositories.get_or_create_condition(
            this->m_pddl_repositories.get_or_create_condition_forall(this->translate(condition.get_parameters()), this->translate(*condition.get_condition())));
    }
    loki::Condition translate_impl(const loki::ConditionNumericConstraintImpl& condition)
    {
        return this->m_pddl_repositories.get_or_create_condition(
            this->m_pddl_repositories.get_or_create_condition_numeric_constraint(condition.get_binary_comparator(),
                                                                                 this->translate(*condition.get_function_expression_left()),
                                                                                 this->translate(*condition.get_function_expression_right())));
    }
    loki::Condition translate_impl(const loki::ConditionImpl& condition)
    {
        return std::visit([this](auto&& arg) -> loki::Condition { return this->translate(*arg); }, condition.get_condition());
    }
    loki::Effect translate_impl(const loki::EffectLiteralImpl& effect)
    {
        return this->m_pddl_repositories.get_or_create_effect(this->m_pddl_repositories.get_or_create_effect_literal(this->translate(*effect.get_literal())));
    }
    loki::Effect translate_impl(const loki::EffectAndImpl& effect)
    {
        return this->m_pddl_repositories.get_or_create_effect(this->m_pddl_repositories.get_or_create_effect_and(this->translate(effect.get_effects())));
    }
    loki::Effect translate_impl(const loki::EffectNumericImpl& effect)
    {
        return this->m_pddl_repositories.get_or_create_effect(
            this->m_pddl_repositories.get_or_create_effect_numeric(effect.get_assign_operator(),
                                                                   this->translate(*effect.get_function()),
                                                                   this->translate(*effect.get_function_expression())));
    }
    loki::Effect translate_impl(const loki::EffectCompositeForallImpl& effect)
    {
        return this->m_pddl_repositories.get_or_create_effect(
            this->m_pddl_repositories.get_or_create_effect_composite_forall(this->translate(effect.get_parameters()), this->translate(*effect.get_effect())));
    }
    loki::Effect translate_impl(const loki::EffectCompositeWhenImpl& effect)
    {
        return this->m_pddl_repositories.get_or_create_effect(
            this->m_pddl_repositories.get_or_create_effect_composite_when(this->translate(*effect.get_condition()), this->translate(*effect.get_effect())));
    }
    loki::Effect translate_impl(const loki::EffectCompositeOneofImpl& effect)
    {
        return this->m_pddl_repositories.get_or_create_effect(
            this->m_pddl_repositories.get_or_create_effect_composite_oneof(this->translate(effect.get_effects())));
    }
    loki::Effect translate_impl(const loki::EffectCompositeProbabilisticImpl& effect)
    {
        auto distribution = loki::EffectDistribution();
        for (const auto& [probability, effect] : effect.get_effect_distribution())
        {
            distribution.emplace_back(probability, this->translate(*effect));
        }
        return this->m_pddl_repositories.get_or_create_effect(this->m_pddl_repositories.get_or_create_effect_composite_probabilistic(distribution));
    }
    loki::Effect translate_impl(const loki::EffectImpl& effect)
    {
        return std::visit([this](auto&& arg) -> loki::Effect { return this->translate(*arg); }, effect.get_effect());
    }
    loki::FunctionExpression translate_impl(const loki::FunctionExpressionNumberImpl& function_expression)
    {
        return this->m_pddl_repositories.get_or_create_function_expression(
            this->m_pddl_repositories.get_or_create_function_expression_number(function_expression.get_number()));
    }
    loki::FunctionExpression translate_impl(const loki::FunctionExpressionBinaryOperatorImpl& function_expression)
    {
        return this->m_pddl_repositories.get_or_create_function_expression(
            this->m_pddl_repositories.get_or_create_function_expression_binary_operator(function_expression.get_binary_operator(),
                                                                                        this->translate(*function_expression.get_left_function_expression()),
                                                                                        this->translate(*function_expression.get_right_function_expression())));
    }
    loki::FunctionExpression translate_impl(const loki::FunctionExpressionMultiOperatorImpl& function_expression)
    {
        return this->m_pddl_repositories.get_or_create_function_expression(
            this->m_pddl_repositories.get_or_create_function_expression_multi_operator(function_expression.get_multi_operator(),
                                                                                       this->translate(function_expression.get_function_expressions())));
    }
    loki::FunctionExpression translate_impl(const loki::FunctionExpressionMinusImpl& function_expression)
    {
        return this->m_pddl_repositories.get_or_create_function_expression(
            this->m_pddl_repositories.get_or_create_function_expression_minus(this->translate(*function_expression.get_function_expression())));
    }
    loki::FunctionExpression translate_impl(const loki::FunctionExpressionFunctionImpl& function_expression)
    {
        return this->m_pddl_repositories.get_or_create_function_expression(
            this->m_pddl_repositories.get_or_create_function_expression_function(this->translate(*function_expression.get_function())));
    }
    loki::FunctionExpression translate_impl(const loki::FunctionExpressionImpl& function_expression)
    {
        return std::visit([this](auto&& arg) -> loki::FunctionExpression { return this->translate(*arg); }, function_expression.get_function_expression());
    }
    loki::FunctionSkeleton translate_impl(const loki::FunctionSkeletonImpl& function_skeleton)
    {
        return this->m_pddl_repositories.get_or_create_function_skeleton(function_skeleton.get_name(),
                                                                         this->translate(function_skeleton.get_parameters()),
                                                                         this->translate(*function_skeleton.get_type()));
    }
    loki::Function translate_impl(const loki::FunctionImpl& function)
    {
        return this->m_pddl_repositories.get_or_create_function(this->translate(*function.get_function_skeleton()), this->translate(function.get_terms()));
    }
    loki::Action translate_impl(const loki::ActionImpl& action)
    {
        return this->m_pddl_repositories.get_or_create_action(
            action.get_name(),
            action.get_original_arity(),
            this->translate(action.get_parameters()),
            (action.get_condition().has_value() ? std::optional<loki::Condition>(this->translate(*action.get_condition().value())) : std::nullopt),
            (action.get_effect().has_value() ? std::optional<loki::Effect>(this->translate(*action.get_effect().value())) : std::nullopt));
    }
    loki::Axiom translate_impl(const loki::AxiomImpl& axiom)
    {
        return this->m_pddl_repositories.get_or_create_axiom(axiom.get_derived_predicate_name(),
                                                             this->translate(axiom.get_parameters()),
                                                             this->translate(*axiom.get_condition()));
    }
    loki::Domain translate_impl(const loki::DomainImpl& domain)
    {
        return this->m_pddl_repositories.get_or_create_domain(domain.get_filepath(),
                                                              domain.get_name(),
                                                              this->translate(*domain.get_requirements()),
                                                              this->translate(domain.get_types()),
                                                              this->translate(domain.get_constants()),
                                                              this->translate(domain.get_predicates()),
                                                              this->translate(domain.get_functions()),
                                                              this->translate(domain.get_actions()),
                                                              this->translate(domain.get_axioms()));
    }
    loki::OptimizationMetric translate_impl(const loki::OptimizationMetricImpl& metric)
    {
        return this->m_pddl_repositories.get_or_create_optimization_metric(metric.get_optimization_metric(),
                                                                           this->translate(*metric.get_function_expression()));
    }

    loki::Problem translate_impl(const loki::ProblemImpl& problem)
    {
        return this->m_pddl_repositories.get_or_create_problem(
            problem.get_filepath(),
            this->translate(*problem.get_domain()),
            problem.get_name(),
            this->translate(*problem.get_requirements()),
            this->translate(problem.get_objects()),
            this->translate(problem.get_derived_predicates()),
            this->translate(problem.get_initial_literals()),
            this->translate(problem.get_function_values()),
            (problem.get_goal_condition().has_value() ? std::optional<loki::Condition>(this->translate(*problem.get_goal_condition().value())) : std::nullopt),
            (problem.get_optimization_metric().has_value() ?
                 std::optional<loki::OptimizationMetric>(this->translate(*problem.get_optimization_metric().value())) :
                 std::nullopt),
            this->translate(problem.get_axioms()));
    }

    /// @brief Recursively apply preparation followed by translation.
    ///        Default behavior runs prepare and translate and returns its results.
    loki::Problem run_base(const loki::ProblemImpl& problem) { return self().run_impl(problem); }

    loki::Problem run_impl(const loki::ProblemImpl& problem)
    {
        this->prepare(problem);
        return this->translate(problem);
    }
};
}

#endif