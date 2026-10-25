# Flask-SQLAlchemy Validations Lab

## Scenario

You've been brought in as a junior developer to help maintain a blog platform for a publishing company. The editorial team recently complained that the system is accepting poorly formatted data: posts with missing content, authors with duplicate entries, and even spammy or incomplete titles. Your job is to strengthen the backend validation layer so only clean, accurate, and editorial-ready data is stored in the database.

To accomplish this, you'll add attribute-level validations directly to your SQLAlchemy models using Python property decorators and `@validates()` methods. You'll enforce field constraints such as uniqueness, length, and conditional logic, all of which align with typical business rules you'd encounter in production.

## Tools & Resources

- [GitHub Repo](https://github.com/learn-co-curriculum/flask-sqlalchemy-validations-lab)
- [Changing Attribute Behavior - SQLAlchemy](https://docs.sqlalchemy.org/en/14/orm/mapped_attributes.html#simple-validators)

## Set Up

This is a **test-driven lab**.

Run `pipenv install` to create your virtual environment and `pipenv shell` to enter the virtual environment.

```console
pipenv install && pipenv shell