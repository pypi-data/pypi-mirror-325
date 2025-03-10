import argparse
import subprocess
import tempfile
import os
from pathlib import Path

VIM_CONFIG = """
let s:watched_dir = expand('~/watched_dir')

function! Monitor()
    write
    let response_path = s:watched_dir . '/response.md'
    rightbelow vsplit | execute 'view ' . response_path
    setlocal autoread
    setlocal readonly
    setlocal nobuflisted
    filetype detect
    syntax on
    wincmd h
    let s:monitor_timer = timer_start(1000, 'CheckForUpdates', {'repeat': -1})
endfunction

function! CheckForUpdates(timer)
    let bufnum = bufnr(s:watched_dir . '/response.md')
    if bufnum == -1
        call timer_stop(s:monitor_timer)
        return
    endif
    silent! checktime
endfunction

function! SaveUserInput()
    let user_input = input('Ask LLM: ')
    let user_file = s:watched_dir . '/user'
    call writefile([user_input], user_file, 'w')
    let current_file = expand('%:t')
    let tree_file = s:watched_dir . '/tree'
    call writefile([current_file], tree_file, 'w')
endfunction

vnoremap <c-l> :w! ~/watched_dir/yank<CR>:w! ~/watched_dir/context<CR>:call SaveUserInput()<CR>
nnoremap <c-l> V:w! ~/watched_dir/yank<CR>:w! ~/watched_dir/context<CR>:call SaveUserInput()<CR>

call Monitor()
"""

def main():
    parser = argparse.ArgumentParser(description="VimLM - LLM-powered Vim assistant")
    parser.add_argument("vim_args", nargs=argparse.REMAINDER, help="Additional Vim arguments")
    args = parser.parse_args()
    watch_dir = Path.home() / "watched_dir"
    watch_dir.mkdir(exist_ok=True)
    with tempfile.NamedTemporaryFile(mode='w', suffix='.vim', delete=False) as f:
        f.write(VIM_CONFIG)
        vim_script = f.name
    try:
        watcher = subprocess.Popen(
            ["python", "-m", "vimlm.watcher"],
            stdout=(watch_dir / "response.md").open("w"),
            stderr=subprocess.STDOUT,
        )
        vim_command = ["vim", "-c", f"source {vim_script}"]
        if args.vim_args:
            vim_command.extend(args.vim_args)
        subprocess.run(vim_command)
    finally:
        watcher.terminate()
        watcher.wait()
        os.unlink(vim_script)

if __name__ == "__main__":
    main()
