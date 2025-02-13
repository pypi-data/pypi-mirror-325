"""
This example demonstrates how to use Goose to plan a meal.

Meal planning is a good use case because it demonstrates the need for tasks to depend on the outputs of other tasks.
You have your initial flow input, which is your overall health goals, and that's the starting point for breakfast.
But then lunch is a function of both your goals and your breakfast.
And then dinner is a function of your goals, your breakfast, and your lunch.
"""

import pytest

from goose import Agent, FlowArguments, Result, flow, task
from goose.agent import AIModel, SystemMessage, TextMessagePart, UserMessage


class HealthGoals(FlowArguments):
    goals: list[str]


class Meal(Result):
    dish_name: str
    ingredients: list[str]
    reason: str


@task
async def plan_breakfast(*, goals: list[str], agent: Agent) -> Meal:
    formatted_goals = "\n".join(f"- {goal}" for goal in goals)
    suggested_meal = await agent(
        messages=[
            UserMessage(
                parts=[
                    TextMessagePart(
                        text=f"What should I make for breakfast? Here are my health goals:\n{formatted_goals}"
                    )
                ]
            ),
        ],
        system=SystemMessage(
            parts=[
                TextMessagePart(
                    text=(
                        "You are a helpful assistant that helps plan breakfasts based on health goals. "
                        "Explain why you built the meal you did."
                    )
                )
            ]
        ),
        response_model=Meal,
        model=AIModel.GEMINI_FLASH,
        task_name="breakfast",
    )
    return suggested_meal


@task
async def plan_lunch(*, goals: list[str], breakfast: Meal, agent: Agent) -> Meal:
    formatted_goals = "\n".join(f"- {goal}" for goal in goals)
    formatted_breakfast = f"Breakfast: {breakfast.dish_name} ({', '.join(breakfast.ingredients)})"
    suggested_meal = await agent(
        messages=[
            UserMessage(
                parts=[
                    TextMessagePart(text=f"What should I make for lunch? Here are my health goals:\n{formatted_goals}"),
                    TextMessagePart(text=f"Here was my breakfast:\n{formatted_breakfast}"),
                ]
            ),
        ],
        system=SystemMessage(
            parts=[
                TextMessagePart(
                    text=(
                        "You are a helpful assistant that helps plan lunches based on health goals. "
                        "Consider the breakfast you had when planning your lunch. Explain why you built the meal you did."
                    ),
                )
            ]
        ),
        response_model=Meal,
        model=AIModel.GEMINI_FLASH,
        task_name="lunch",
    )
    return suggested_meal


@task
async def plan_dinner(*, goals: list[str], lunch: Meal, breakfast: Meal, agent: Agent) -> Meal:
    formatted_goals = "\n".join(f"- {goal}" for goal in goals)
    formatted_breakfast = f"Breakfast: {breakfast.dish_name} ({', '.join(breakfast.ingredients)})"
    formatted_lunch = f"Lunch: {lunch.dish_name} ({', '.join(lunch.ingredients)})"
    suggested_meal = await agent(
        messages=[
            UserMessage(
                parts=[
                    TextMessagePart(
                        text=f"What should I make for dinner? Here are my health goals:\n{formatted_goals}"
                    ),
                    TextMessagePart(text=f"Here was my breakfast:\n{formatted_breakfast}"),
                    TextMessagePart(text=f"Here was my lunch:\n{formatted_lunch}"),
                ]
            ),
        ],
        system=SystemMessage(
            parts=[
                TextMessagePart(
                    text=(
                        "You are a helpful assistant that helps plan dinners based on health goals. "
                        "Consider the breakfast and lunch you had when planning your dinner. "
                        "Explain why you built the meal you did."
                    ),
                )
            ]
        ),
        response_model=Meal,
        model=AIModel.GEMINI_FLASH,
        task_name="dinner",
    )
    return suggested_meal


@flow
async def meal_plan(*, flow_arguments: HealthGoals, agent: Agent) -> None:
    breakfast = await plan_breakfast(goals=flow_arguments.goals, agent=agent)
    lunch = await plan_lunch(goals=flow_arguments.goals, breakfast=breakfast, agent=agent)
    await plan_dinner(goals=flow_arguments.goals, lunch=lunch, breakfast=breakfast, agent=agent)


@pytest.mark.asyncio
async def test_meal_plan_flow() -> None:
    health_goals = HealthGoals(goals=["lose weight", "have more energy"])
    async with meal_plan.start_run(run_id="my-meal-plan") as run:
        await meal_plan.generate(health_goals)

    dinner = run.get(task=plan_dinner).result
    assert isinstance(dinner.reason, str)
