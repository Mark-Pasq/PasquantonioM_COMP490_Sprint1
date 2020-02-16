#!/usr/bin/env python3

# Mark Pasquantonio
# Senior Design and Dev COMP490
# Project 1 JobsAssignment Sprint 1 tests
# Filename: test_get_jobs.py

import pytest
import get_jobs
import sqlite3

global row


@pytest.fixture
def get_data():
    import get_jobs
    return get_jobs.get_git_jobs_data()


def test_my_jobs_dict(get_data):
    # first required test
    assert len(get_data) >= 100
    assert type(get_data[1]) is dict


def test_my_jobs_data(get_data):
    # any real data should have both full time and Contract
    # jobs in the list, assert this
    data = get_data
    full_time_found = False
    contract_found = False
    for item in data:
        if item['type'] == 'Contract':
            contract_found = True
        elif item['type'] == 'Full Time':
            full_time_found = True
    assert contract_found and full_time_found


def test_check_if_table_exists():
    connection = sqlite3.connect('git_jobs.sqlite')
    cursor_object = connection.cursor()
    # get the count of tables with the name
    cursor_object.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='git_jobs_tbl' ''')
    # if the count is 1, then table exists
    assert cursor_object.fetchone()[0] == 0
    print('There is only 1 table in the database named git_jobs_tbl.')


def test_sql_fetch():
    global row
    connection = sqlite3.connect('git_jobs.sqlite')
    cursor_obj = connection.cursor()
    cursor_obj.execute(''' SELECT id FROM main.git_jobs_tbl WHERE company='Nike' ''')
    rows = cursor_obj.fetchall()
    for row in rows:
        assert isinstance(row, object)
        print(row)


test_sql_fetch()
