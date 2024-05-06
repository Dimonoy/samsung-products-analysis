#!/bin/bash

_=$(which tmux)
[[ $? == 1 ]] && echo "tmux was not found. Make sure tmux is installed and is located in PATH"

TMUX_SESSION_NAME="samsung"
TMUX_WINDOWS=($(ls -I LICENSE -I README.md -I requirements.txt -I setup-dev-env.sh -I venv))
TMUX_WINDOWS_SELECTED=()

print_usage() {
    local ORIG_IFS=$IFS
    IFS=","

    cat << EOF
A script to setup the development environment using tmux

USAGE:
    $(basename $0) [FLAGS]

FLAGS:
    -h       Prints help information
    -e       Specifies a development environments separated by space and enclosed in quotes.
             Following development environments are available:
                 ${TMUX_WINDOWS[*]}
             Shortcuts can also be passed:
             'all', 'default' (no environments, empty DE setup)
EXAMPLES:
    $(basename $0) -e "scraper notebooks"
    $(basename $0) -e "all"
    $(basename $0) -h
    $(basename $0)
EOF

    IFS=$ORIG_IFS
}

arg_parse() {
    local opt

    while getopts ":he:" opt; do
        case $opt in
            h)
                print_usage
                exit 0
                ;;
            e)
                TMUX_WINDOWS_SELECTED=$OPTARG
                ;;
            :)
                TMUX_WINDOWS_SELECTED=()
                break
                ;;
            \?)
                echo "[ERROR] Invalid arguments."
                print_usage
                exit 2
                ;;
        esac
    done
    shift $(( OPTIND - 1 ))

    local ALL_POSSIBLE_TMUX_WINDOWS=(${TMUX_WINDOWS[@]} default all)
    for workspace in ${TMUX_WINDOWS_SELECTED[@]}; do
        if [[ ! "${ALL_POSSIBLE_TMUX_WINDOWS[@]}" =~ "$workspace" ]]; then
            echo "[ERROR] No workspace '$workspace' available."
            print_usage
            exit 2
        fi
    done
}

pane_setup() {
    local WORKDIR=$1

    tmux send-keys "[ -d venv ] && source venv/bin/activate" C-m
    tmux send-keys "cd $WORKDIR" C-m
    tmux send-keys "[ -e .env ] && source .env" C-m
    tmux send-keys "clear" C-m
}

window_setup() {
    local TMUX_WINDOW=$1
    local TMUX_WINDOW_INDEX=$2

    tmux select-window -t $TMUX_WINDOW_INDEX
    tmux rename-window -t $TMUX_WINDOW_INDEX $TMUX_WINDOW

    pane_setup $TMUX_WINDOW

    tmux split-window -t $TMUX_WINDOW_INDEX -h -p 20

    pane_setup $TMUX_WINDOW
}

tmux_setup() {
    local TMUX_WINDOW TMUX_WINDOW_INDEX

    tmux new-session -s $TMUX_SESSION_NAME -d

    [[ "${TMUX_WINDOWS_SELECTED[@]}" =~ "default" ]] && TMUX_WINDOWS_SELECTED=()
    [[ "${TMUX_WINDOWS_SELECTED[@]}" =~ "all" ]] && TMUX_WINDOWS_SELECTED=${TMUX_WINDOWS[@]}

    TMUX_WINDOW_INDEX=0
    for TMUX_WINDOW in ${TMUX_WINDOWS_SELECTED[@]}; do
        [[ $TMUX_WINDOW_INDEX -gt 0 ]] && tmux new-window

        window_setup $TMUX_WINDOW $TMUX_WINDOW_INDEX
        TMUX_WINDOW_INDEX=$(( $TMUX_WINDOW_INDEX + 1 ))
    done

    tmux a -t $TMUX_SESSION_NAME
}

arg_parse "$@"
tmux_setup
