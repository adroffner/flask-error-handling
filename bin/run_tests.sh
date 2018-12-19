#! /bin/bash
#
# Run Unit Tests
# ============================================================================
# Run the unittests with nose & coverage.py
# ============================================================================

PYTHON=python3

# $PYTHON ./setup.py test
$PYTHON -m coverage run ./setup.py test
$PYTHON -m coverage html
$PYTHON -m coverage xml

echo
echo 'See unit test coverage:'
echo "file://$PWD/htmlcov/index.html"
echo
