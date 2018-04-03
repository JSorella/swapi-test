from features.swapiwrapper.swapi import Swapi
from behave import *
from datetime import datetime


@given('a Star Wars Api')
def step_impl(context):
    context.api = Swapi()


@when('user searchs for film number {film_number}')
def step_impl(context, film_number):
    context.result = context.api.get_film(film_number)


@then('"{movie_title}" title is given')
def step_impl(context, movie_title):
    title = context.result['title']

    assert(movie_title == title)


@then('{year} year release is given')
def step_impl(context, year):
    datetime_object = datetime.strptime(context.result['release_date'], '%Y-%m-%d')

    assert(datetime_object.year == int(year))


@then('{episode_number}th episode is given')
def step_impl(context, episode_number):
    episode_id = context.result['episode_id']

    assert(episode_id == int(episode_number))
