# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]


## [2.1.0] - 2025-06-24

Minor update to represent changes that have gone into the SNAC v2.1 release (NILRT 11.2, LV 2025Q3).

Representing github changes through PR 31.


### Added
* Added optional instructions giving guidance on using `cryptsetup` to encrypt non-runtime partitions. (#24)
* Added support for EAPOL authentication of systems using `wpa_supplicant`. (#27)
	* Upgraded 03.05.02 compliance to USER. (#27)

### Changed
* Updated the 03.13.08 solution. (#24)
* Changed the remote syslog configuration instructions to use UDP, instead of TCP. (#25)

### Fixed
* Fixed typographical errors in the firewall configuration instructions. (#26)
* Fixed a broken hyperlink in control 03.13.08. (#29)


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
