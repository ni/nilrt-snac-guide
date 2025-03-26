# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]


## [2.0.0] - 2025-03-26

First github release based on the new documentation build process. Corresponds to nilrt-snac v2.0.0, LV 2025Q2, and NILRT 11.1.


### Added

* Created a Sphinx-based build system to create the SNAC configuration guide from code.
* Add section for Configuring Remote Logging (#7)
* Added an appendix (Appendix 4), which tracks LVRT feature support.
* Added control section for 03.06.05. (#21)


### Changed

* Changed supported hardware configuration utility from MAX to HWCU, to reflect future development strategies. (#12)
* Marked SNAC as supporting DAQmx on all harwdare platforms. (#12)
* Changed the document title to "NI Linux RT SNAC Configuration Guide". (#22)
* Removed warnings about the user losing the ability to update software when in SNAC mode, since that is now supported. (#22)
* Revised many descriptive sections to be more clear and reduce duplicate information. (#22)


### Fixed

* Corrected some incorrect requirement headers leftover from the draft-1 release of NIST 800-171r3. (#15, #16, #17, #18, #19, #20)
