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

#include "formatter.hpp"
#include "mimir/formalism/ground_function.hpp"
#include "mimir/formalism/ground_function_value.hpp"

namespace mimir
{
GroundFunctionValueImpl::GroundFunctionValueImpl(Index index, GroundFunction function, double number) :
    m_index(index),
    m_function(std::move(function)),
    m_number(number)
{
}

Index GroundFunctionValueImpl::get_index() const { return m_index; }

const GroundFunction& GroundFunctionValueImpl::get_function() const { return m_function; }

double GroundFunctionValueImpl::get_number() const { return m_number; }

std::ostream& operator<<(std::ostream& out, const GroundFunctionValueImpl& element)
{
    auto formatter = PDDLFormatter();
    formatter.write(element, out);
    return out;
}

std::ostream& operator<<(std::ostream& out, GroundFunctionValue element)
{
    out << *element;
    return out;
}

}
