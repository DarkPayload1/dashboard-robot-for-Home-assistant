# 1.7.0-rc.1

- Remove repeated setup fields across steps.
- Keep AI, language and dashboard choices on the Robot page only.
- Separate optional manual devices and extra readings from normal source review.
- Preserve choices on skipped pages and share setup behavior between initial and options flows.

# 1.6.0-rc.1

- Select all in-room cameras and allow manual selection of any registered camera.
- Camera chooser with labels and room matching; no silent first-camera selection.
- Preserve compatibility with earlier single-camera settings.

# 1.5.0-rc.6

- Include unassigned media players in automatic room selection.
- List all enabled registered media players in the manual speaker picker.
- Preserve manual media choices and expose selected players without areas by name.

# 1.5.0-rc.5

- Preserve an independently selected AI assistant across source review pages without conversation entities.
- Removing sensor integrations no longer resets the separate AI selection.
- Explicit AI selection remains clearable on the advanced page.

# 1.5.0-rc.4

- Prioritize configured standalone robot over legacy embedded robots on selected dashboards.
- Restore legacy robot display on leaving configured routes.

# 1.5.0-rc.3

- Prioritize configured price/power/waste/weather answers over generic sensor matches.
- Format current electricity price with two localized decimals.
- Keep broad sensor lists for explicit overview questions.

# 1.5.0-rc.2

- Prefer explicit current electricity price among multiple price components.
- Persist unambiguous suggested sources as real schema defaults.

# 1.5.0-rc.1

- Choose installed integrations by their actual titles.
- Review detected source suggestions with generic read-only sensor support.
- Keep ambiguous choices explicit and isolate selected integration sources.

# 1.4.0-rc.3

- Include a camera automatically when saving selected rooms.
- Preserve a selected in-room camera; clear cameras when moving to rooms without one.

# 1.4.0-rc.2

- Automatically select lights and speakers from chosen rooms.
- Simple placement page; manual entities and shared sensors are optional advanced settings.
- Localized new setup page.

# 1.4.0-rc.1

- Room-first two-step setup with filtered device selectors.
- Clear devices outside selected rooms on save.

# Changelog

## 1.3.0-rc.3

- Hide parcel, camera, music, power and waste shortcuts until their entities are selected.
- Hide parcel tracking controls when no parcel sensors are selected.
- No parcel sensors now means unconfigured, never zero parcels.
- Music shortcut uses an actually selected speaker room.


## 1.3.0-rc.2

- Load a content-versioned browser module to avoid reusing an older robot asset.
- Add a regression check: no configured sensor means no sensor value may be read or reported.


## 1.3.0-rc.1

- Remove personal sensor IDs and location-specific facts.
- Add configurable price, power, fuel, waste, weather and parcel sensors.
- Preserve sensor units instead of assuming DKK, VAT or watt values.
- Require parcel source selection and distinguish missing configuration from an empty parcel list.
- Expand Danish/English/German interface, status, errors and local answers.
- Separate browser visibility/position preferences by profile and user.
- Add local brand icons, documentation, privacy information and MIT license.
- Include Python/JavaScript tests and HACS/hassfest workflow preparation.

This is a release candidate. Clean Home Assistant installation, real browser speech input and wall-display testing remain outstanding. HACS/hassfest have not been run against a published repository.
