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
## keyboard shortcuts
there are currently two keyoboard shortcurts:  
`d` makes the select different fortune teller window apear.  
`c` copies the current fortune to the clipboard

