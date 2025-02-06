#! /usr/bin/env bash

function blue_sbc_unicorn_16x16() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ] ; then
        abcli_show_usage "blue_sbc unicorn_16x16 validate" \
            "validate unicorn_16x16."
        return
    fi

    if [ "$task" == "validate" ] ; then
        pushd $abcli_path_git/unicorn-hat-hd/examples > /dev/null
        python3 rainbow.py
        popd > /dev/null
        return
    fi

    abcli_log_error "-blue-sbc: unicorn_16x16: $task: command not found."
}