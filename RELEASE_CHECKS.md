# Release checks

Completed locally:

- Python source/JSON parsing and six Python tests.
- Five JavaScript test files covering controls, parcel actions, languages, live text rendering and profile routing.
- JavaScript syntax check.
- Personal identifier scan.
- PNG icon dimension verification.
- ZIP integrity check and clean extraction.

Before public release:

1. Install on a clean Home Assistant 2026.10+ test instance; test config flow, reload, removal and update from the previous version.
2. Test dashboard behavior and speech on intended desktop/mobile/wall-display browsers.
3. Choose/create the GitHub repository; run `python scripts/prepare_repository.py OWNER/REPOSITORY` before committing.
4. Run the included HACS and hassfest workflows and resolve any findings.
5. Review the MIT license and privacy documentation; publish a prerelease first.

This package does not claim HACS acceptance or a completed hardware test.
