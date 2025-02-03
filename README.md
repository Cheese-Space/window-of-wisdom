# window-of-wisdom

This is a simple program that displays the output of the `fortune` command in a Tkinter window.

## Requirements

This program requires both `cowsay` and `fortune` to be installed. Currently, Windows is not supported because this program relies on `cowsay` and `fortune`, which are typically available on Unix-based systems.

To install `fortune` and `cowsay`, you can use one of the following commands:

On debian based distros:
```bash
sudo apt install cowsay fortune-mod
```
on fedora based distros:
```bash
sudo dnf install cowsay fortune-mod
```
on arch linux based-distros:
```bash
sudo pacman -S cowsay fortune-mod
```
on macOS:
```bash
brew install cowsay fortune
```
## flags
this program currently has 4 flags:
--help, --skip_nt_error, --tux and --cow. the tux and cow command replaces the stegosaurus in the tkinter window. And the --skip_nt_error flag skips the error that you would get if you ran this program on windows

