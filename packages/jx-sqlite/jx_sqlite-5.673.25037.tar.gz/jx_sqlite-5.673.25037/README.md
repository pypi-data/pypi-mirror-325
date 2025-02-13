# jx-sqlite 

JSON query expressions using SQLite


[![PyPI Latest Release](https://img.shields.io/pypi/v/jx-sqlite.svg)](https://pypi.org/project/jx-sqlite/)
[![Build Status](https://app.travis-ci.com/klahnakoski/jx-sqlite.svg?branch=master)](https://travis-ci.com/github/klahnakoski/jx-sqlite)
[![Coverage Status](https://coveralls.io/repos/github/klahnakoski/jx-sqlite/badge.svg?branch=dev)](https://coveralls.io/github/klahnakoski/jx-sqlite?branch=dev)

## Summary

This library will manage your database schema to store JSON documents. You get all the speed of a well-formed database schema without the schema migration headaches. 


## Status

Significant updates to the supporting libraries has broken this code.  It still works for the simple cases that require it

**Jan 2024** - 118 of 334 tests ignored


## Installation

    pip install jx-sqlite

## Code Example

The smoke test, found in the `tests` is a simple example of how to use this library.

```python
import jx_sqlite

table = (
    jx_sqlite
    .Container(filename="my.db")
    .get_or_create_facts("my_table")
    .insert([{"os": "linux", "value": 42}])
    .query({
        "select": "os",
        "where": {"gt": {"value": 0}}
    })
)
```

## More

This project is an attempt to store JSON documents in SQLite so that they are accessible via SQL. The hope is this will serve a basis for a general document-relational map (DRM), and leverage the database's query optimizer.
`jx-sqlite` is responsible for expanding the schema dynamically as new JSON documents are encountered.  It also strives to ensure old queries against the new schema have the same meaning; the same results.

The most interesting, and most important feature is that we query nested object arrays as if they were just another table.  This is important for two reasons:

1. Inner objects `{"a": {"b": 0}}` are a shortcut for nested arrays `{"a": [{"b": 0}]}`, plus
2. Schemas can be expanded from one-to-one  to one-to-many `{"a": [{"b": 0}, {"b": 1}]}`.


## Motivation

JSON is a nice format to store data, and it has become quite prevalent. Unfortunately, databases do not handle it well, often a human is required to declare a schema that can hold the JSON before it can be queried. If we are not overwhelmed by the diversity of JSON now, we soon will be. There will be more JSON, of more different shapes, as the number of connected devices( and the information they generate) continues to increase.

## Contributing

Contributions are always welcome! The best thing to do is find a failing test, and try to fix it.

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

    $ git clone https://github.com/klahnakoski/jx-sqlite
    $ cd jx-sqlite

### Running tests

There are over 300 tests used to confirm the expected behaviour: They test a variety of JSON forms, and the queries that can be performed on them. Most tests are further split into three different output formats ( list, table and cube).

The `requirements.lock` file is the last successful combination that passed all tests, despite the version conflicts.

    python.exe -m pip install --no-deps -r tests\requirements.lock


Linux

    export PYTHONPATH=.:vendor
    python -m unittest discover -v -s tests

Windows

    set PYTHONPATH=.;vendor
    python -m unittest discover -v -s tests


### Technical Docs

* [Json Query Expression](https://github.com/klahnakoski/ActiveData/blob/dev/docs/jx.md)
* [Nomenclature](https://github.com/mozilla/jx-sqlite/blob/master/docs/Nomenclature.md)
* [Snowflake](https://github.com/mozilla/jx-sqlite/blob/master/docs/Perspective.md)
* [JSON in Database](https://github.com/mozilla/jx-sqlite/blob/master/docs/JSON%20in%20Database.md)
* [The Future](https://github.com/mozilla/jx-sqlite/blob/master/docs/The%20Future.md)

## License

This project is licensed under Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.


## History

*Jan 2024* - Attempt to resurrect this project (118 of 334 tests ignored)

*Sep 2018* - Upgrade libs, start refactoring to work with other libs

*Dec 2017* - A number of tests were added, but they do not pass.

*Sep 2017* - GSoC work completed, all but a few tests pass.
 

## GSOC

Good work by Rohit Kumar.  You may see the end result on [gsoc branch](https://github.com/klahnakoski/jx-sqlite/tree/gsoc).  Installation requires python2.7,  and will require some version fixing to get running.

See [the demonstration video](https://www.youtube.com/watch?v=0_YLzb7BegI&list=PLSE8ODhjZXja7K1hjZ01UTVDnGQdx5v5U&index=26&t=260s)


Work done up to the deadline of GSoC'17:

* [Pull Requests](https://github.com/mozilla/jx-sqlite/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Arohit-rk)
* [Commits](https://github.com/mozilla/jx-sqlite/commits?author=rohit-rk)



