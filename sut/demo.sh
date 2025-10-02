
function message() {
    echo "* --------------------------------- *"
    for line in "${@}"; do
        echo -e "> ${line}"
    done
    echo "* --------------------------------- *"
    checkpoint
}


function checkpoint() {
    echo -e "[waiting]"
    read
}

#1 Run compounds tests
message "Running compounds test(s) on a working SUT"\
        "NOTE: Everything green, nice. Another job well done :)"
pytest --tb=no tests/compound
checkpoint

#2 Run compounds tests with bug -> hard to debug
message "Running compounds test(s) on a bugged SUT"\
        "NOTE: problem is hard to identify without accessing logs"
SUT_BUG="True" pytest --tb=no tests/compound
checkpoint

#3 Run atomic tests

message "Running Atomic tests on working SUT"\
        "NOTE: again everything is green, more tests though"\
        "might have additional time penalty, but should be small"
pytest --tb=no tests/test_auth
checkpoint


#4 Run atomic tests with bug -> easier to debug
message "Running Atomic tests on bugged SUT"\
        "NOTE: Now it should be easier to pinpoint the failure case"
SUT_BUG=True pytest --tb=no tests/test_auth
checkpoint
