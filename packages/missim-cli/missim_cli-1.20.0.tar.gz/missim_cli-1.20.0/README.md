# MISSIM CLI

![MISSIM CLI](./docs/missim_cli.png)

Publicly available on [PyPi](https://pypi.org/project/missim-cli/) for convenience but if you don't work at Greenroom Robotics, you probably don't want to use this.

## Install

* For development:
  * `pip install -e ./packages/missim_config`
  * `pip install -e ./tools/missim_cli`
* For production: `pip install missim-cli`
* You may also need to `export PATH=$PATH:~/.local/bin` if you don't have `~/.local/bin` in your path
* Install autocomplete:
  * bash: `echo 'eval "$(_MISSIM_COMPLETE=bash_source missim)"' >> ~/.bashrc`
  * zsh: `echo 'eval "$(_MISSIM_COMPLETE=zsh_source missim)"' >> ~/.zshrc` (this is much nicer)
  * If using zsh, the git checker plugin make terminal slow. Suggest you run `git config oh-my-zsh.hide-info 1` in the zsh terminal inside the repo

## Usage

* `missim --help` to get help with the CLI

## Dev mode

MISSIM CLI can be ran in dev mode. This will happen if it is installed with `pip install -e ./tools/missim` or if the environment variable `MISSIM_CLI_DEV_MODE` is set to `true`.