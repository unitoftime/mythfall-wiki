[![Mythfall](./src/images/logo.png)](https://mythfall.com)
# Mythfall Wiki
This repository is for the [Wiki](https://wiki.mythfall.com/) for the 2d game [Mythfall](https://mythfall.com/).


# How to contribute

* [Install the mdbook tool](https://rust-lang.github.io/mdBook/guide/installation.html) which is used to generate the wiki.
The wiki uses normal markdown formatting.
* Edit files within the `src` folder and submit a pull request.
* Use the command `mdbook serve` while in the root folder to see changes locally.

### Contributions
For contributions, check:
1. Any frequently changing pages have a version warning at the bottom:
	``` html
		<div class="warning">
		Values correct for patch 0.0.9
		</div>
	```
2. New pages are added to the "summary": '[./src/SUMMARY.md](./src/SUMMARY.md)
