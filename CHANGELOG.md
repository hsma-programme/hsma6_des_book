# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). Dates formatted as YYYY-MM-DD as per [ISO standard](https://www.iso.org/iso-8601-date-and-time-format.html).

## v0.2.0 - 2025-02-10

Updates to the book following review by and additions from Amy Heather.

### Added

* `CITATION.cff`.
* `downloadthis` quarto extension (used on `stress_des.qmd`).
* Page on debugging (`basic_debugging_tactics.qmd`).
* Page comparing model structures - by adapting and extending on `example_models.qmd`.
* Page on reproducibility when sharing models (`sharing_reproducible_models.qmd`).
* Page on STARS (`stars.qmd`)
* Page on STRESS-DES (`stress_des.qmd`).
* Page on testing (`tests.qmd`).

### Changed

* Embellished `README.md` with logo, badges, illustration, contribution instructions, instructions for rendering the book locally, and a citation and acknowledgements section.
* Likewise embellished `index.qmd` acknowledgements section.
* Updated citation for book to include Amy Heather.
* Add authors to the YAML header on each page.
* Consistent heading style ("Title Case For Titles", "Sentence case for all other headings") ([#3](https://github.com/hsma-programme/hsma6_des_book/issues/3)).
* Consistent sections and names where relevant (e.g. "Coding the model", "The full code - the full updated code for the model is given below" with the code then in a collapsible box) ([#3](https://github.com/hsma-programme/hsma6_des_book/issues/3)).
* Regarding the "##NEW" messages:
    * Add a callout about the "##NEW" convention used ([#8](https://github.com/hsma-programme/hsma6_des_book/issues/8)).
    * Ensured consistent use (removing "## NEW", "# NEW", "#MODIFIED", etc) ([#9](https://github.com/hsma-programme/hsma6_des_book/issues/9)).
* Consistent lists (with a ":", capitalisation and full stops).
* Minor spelling and grammar fixes - which include a few specified in issues ([#37](https://github.com/hsma-programme/hsma6_des_book/issues/37), [#24](https://github.com/hsma-programme/hsma6_des_book/issues/24)).
* Add an "Acknowledgements" callout at the start of any page with relevant authors, GitHubs and ORCIDs, when the page has used content from elsewhere ([#6](https://github.com/hsma-programme/hsma6_des_book/issues/6), [#42](https://github.com/hsma-programme/hsma6_des_book/issues/42)).
* Add `plotly.express`, `pytest` and `sim_tools` to environment.
* Add further explanation of code changes in `testing_large_numbers_scenarios.qmd` ([#53](https://github.com/hsma-programme/hsma6_des_book/issues/53)).

### Removed

* Unused file `intro.qmd`.

### Fixed

* Corrected `callout-info` to `callout-note` ([#12](https://github.com/hsma-programme/hsma6_des_book/issues/12))
* Links to streamlit book and display of app in `intro_creating_web_apps.qmd` ([#27](https://github.com/hsma-programme/hsma6_des_book/issues/27)), and to other pages in `appointment_style_booking_models.qmd` ([#26](https://github.com/hsma-programme/hsma6_des_book/issues/26)).
* Made installation of `pywin32` and `pywinpty` (as in `requirements.txt`) only relevant for Windows machines.
* Made book chapters visible in light mode (`theme-light.scss`) ([#17](https://github.com/hsma-programme/hsma6_des_book/issues/17)).
* Prevented cut-off of final chapters in sidebar (`theme-dark.scss`, `theme-light.scss`)

## v0.1.0 - 2025-01-24

🌱 First release of the HSMA6 DES Book.