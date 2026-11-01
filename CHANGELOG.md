# 1.7.21-rc.1

## Dansk

- Læser automatisk svaret højt, når spørgsmålet sendes fra chatfeltet.
- Giver en vejledning til tastaturdiktat på telefoner, hvor browseren ikke understøtter robotten's taleinput.

## English

- Automatically reads the answer aloud when a question is submitted from the chat field.
- Guides phone users to keyboard dictation when the browser does not support the robot's speech input.

# 1.7.20-rc.1

## Dansk

- Dokumenterer, hvordan Siri på iPhone kan sende spørgsmål til en Home Assistant Assist-pipeline via Genveje.
- Forklarer, at man selv skal oprette Siri-genvejen på sin iPhone.

## English

- Documents how Siri on iPhone can send questions to a Home Assistant Assist pipeline through Shortcuts.
- Explains that each user creates the Siri shortcut on their own iPhone.

# 1.7.19-rc.1

## Dansk

- Retter en fejl, hvor robotten læste et tal fra vinduesindstillingerne i stedet for teksten i chatfeltet.
- Spørgsmål, genveje og taleinput bruger nu det rigtige chatfelt.

## English

- Fixes a bug where the robot read a number from the window settings instead of the text in the chat field.
- Questions, shortcuts and speech input now use the correct chat field.

# 1.7.18-rc.1

## Dansk

- Lader dig begynde at skrive et nyt spørgsmål, selvom AI'en stadig arbejder på det gamle.
- Afbryder den gamle ventende samtale ved første tastetryk, rydder dens gamle besked og beholder den nye tekst klar til afsendelse.

## English

- Lets you start typing a new question while the AI is still working on the previous one.
- Cancels the old pending conversation on the first keystroke, clears its stale message and keeps the new text ready to send.

# 1.7.17-rc.1

## Dansk

- Retter nulstilling af en samtale, så et gammelt spørgsmål ikke bliver gendannet.
- Gør knappen tydelig, når den afbryder et ventende svar og starter en ny samtale.
- Viser en særskilt besked, når Google Gemini melder om høj efterspørgsel.
- Rydder den gamle mikrofonstatus, når et spørgsmål sendes.

## English

- Fixes conversation reset so an old question is not restored.
- Clarifies that the button cancels a pending reply and starts a new conversation.
- Shows a specific message when Google Gemini reports high demand.
- Clears the stale microphone status when a question is sent.

# 1.7.16-rc.1

## Dansk

- Holder popup-vinduet inden for skærmens kanter, også med gemt placering.
- Tilpasser den valgte højde til skærmen, så vinduet ikke bliver skåret af.

## English

- Keeps the popup within the viewport, including when a saved position is used.
- Clamps the selected height to the available screen space.

# 1.7.15-rc.1

## Dansk

- Tilføjer valg af popup-højde: lav, normal eller høj.
- Popup-indholdet kan rulles, når det ikke kan være inden for den valgte højde.

## English

- Adds low, standard and tall popup height choices.
- Popup content scrolls when it does not fit within the selected height.

# 1.7.14-rc.1

## Dansk

- Tilføjer valg mellem lille, normal og stor popup.
- Tilføjer justerbar gennemsigtighed.
- Tilføjer mulighed for at flytte popup-vinduet og huske dets placering.
- Viser en tydelig kvittering, når indstillingerne er gemt.

## English

- Adds compact, standard and large popup sizes.
- Adds adjustable transparency.
- Lets you move the popup and remember its position.
- Shows a clear confirmation when settings are saved.

# 1.7.13-rc.1

## Dansk

- Gør robottens popup smallere på større skærme: 480 px i stedet for 600 px.
- Reducerer luft, overskrift og velkomstfelt, så vinduet også bliver lavere. Bevarer glasdesign og tydelige knapper.
- Lader længere samtaler rulle i et mindre historikfelt; på telefoner tilpasses bredden fortsat til skærmen.

## English

- Makes the robot popup narrower on larger screens: 480 px instead of 600 px.
- Reduces spacing, header and welcome area to make the window shorter while keeping the glass design and readable controls.
- Scrolls longer conversations in a smaller history area; phone width still adapts to the screen.

# 1.7.12-rc.1

## Dansk

- Retter glasdesignet på computere, hvor browseren melder reduceret gennemsigtighed: robottens popup forbliver nu gennemsigtig i stedet for at blive ensfarvet.
- Bevarer sløring, læselige tekstfelter og reservebaggrund til browsere uden understøttelse af sløring.

## English

- Fixes the glass design on computers whose browser reports reduced transparency: the robot popup now keeps its translucent appearance instead of switching to a solid background.
- Preserves backdrop blur, readable inputs and the fallback background for browsers without blur support.

# 1.7.11-rc.1

## Dansk

- Giver robottens popup et gennemsigtigt glasdesign med sløret dashboard bag vinduet, blød kant og diskret skygge.
- Tilpasser overskrift og samtalebobler til glasdesignet, mens tekstfelt og knapper fortsat er tydelige.
- Bruger en mere dækkende baggrund, hvis browseren ikke understøtter sløring, eller der er valgt reduceret gennemsigtighed.

## English

- Gives the robot popup a translucent glass design with a blurred dashboard behind it, a soft border and a subtle shadow.
- Restyles the header and conversation bubbles while keeping the input and buttons readable.
- Uses a more opaque background when backdrop blur is unsupported or reduced transparency is requested.

# 1.7.10-rc.1

## Dansk

- Oplæser priser som kroner og øre i stedet for tvetydige decimaltal: 2,29 DKK/kWh bliver til “to kroner og niogtyve øre pr. kilowatt-time”.
- Gælder både Piper og browserstemmer. Understøtter punktum/komma, negative priser og brændstofpriser pr. liter; teksten i chatten ændres ikke.
- Har sprogtilpassede valutaenheder på dansk, engelsk og tysk. Pakkenumre og temperaturer bevares.

## English

- Reads prices as whole kroner and øre rather than ambiguous decimal digits, including expanded per-kilowatt-hour and per-litre units.
- Applies to Piper and browser speech. Supports decimal dots/commas, negative prices and fuel prices; visible chat text is unchanged.
- Uses language-specific currency wording for Danish, English and German while preserving tracking numbers and temperatures.

# 1.7.9-rc.1

## Dansk

- Viser den aktive Piper-model eller giver valg mellem browserens stemmer til det valgte sprog. Bevarer prøveknap og taletempo.
- Husker op til 20 samtaletrin og AI-samtale-id i den aktuelle browserfane efter genindlæsning. Udløber efter 30 minutters inaktivitet; Ny samtale rydder historikken. Historik synkroniseres ikke mellem enheder.
- Tilføjer synlig status for lytning, tænkning og tale samt en stopknap til oplæsning.
- Tilføjer valg mellem talt velkomst, lydløs velkomst og ingen velkomst under Stemme og taletempo. Talt velkomst begrænses til én gang pr. 30 minutter i fanen.
- Giver mere konkrete fejl for adgang, tidsudløb, AI-grænser, tomme svar og lokal tale på dansk, engelsk og tysk.

## English

- Shows the active Piper model or lets you choose matching browser voices. Keeps voice testing and speech speed controls.
- Restores up to 20 conversation turns and the AI conversation ID after reloading the current browser tab. Expires after 30 minutes of inactivity; New conversation clears it. History is not synced across devices.
- Adds visible listening, thinking and speech status with a stop speech button.
- Adds spoken, silent and disabled greeting choices under Voice and speed. Spoken greetings occur at most once every 30 minutes in the tab.
- Adds actionable access, timeout, AI quota, empty response and local speech errors in Danish, English and German.

# 1.7.8-rc.1

## Dansk

- Tilføjer en komplet opsætningsvejledning til lokal dansk, engelsk og tysk Piper-tale uden Nabu Casa.
- Beskriver hentning af alle tre modeller: Talesyntese, Cori og Thorsten. Modeller hentes pr. Home Assistant-installation og er ikke inkluderet i robot-ZIP-filen.
- Bevarer sprogafhængigt stemmevalg fra 1.7.7-rc.1. Denne udgivelse ændrer dokumentation og versionsnummer, ikke afspilningskoden.

## English

- Adds full setup instructions for local Danish, English and German Piper speech without Nabu Casa.
- Documents downloading all three models: Talesyntese, Cori and Thorsten. Models are downloaded per Home Assistant installation and are not bundled in the robot ZIP.
- Keeps language-specific voice selection from 1.7.7-rc.1. This release updates documentation and version metadata, not playback code.

# 1.7.7-rc.1

## Dansk

- Vælger en særskilt Piper-stemme til hvert sprog: Talesyntese på dansk, Cori på engelsk og Thorsten på tysk.
- Sender både sprog og stemmemodel, så engelske og tyske svar ikke bruger den danske standardstemme.
- Gælder både velkomst og oplæsning af svar. Piper kan hente stemmemodellen ved første brug.

## English

- Selects a separate Piper voice for each language: Talesyntese for Danish, Cori for English and Thorsten for German.
- Sends both language and voice model so English and German no longer use the Danish default voice.
- Applies to greetings and answer playback. Piper may download the voice model on first use.

# 1.7.6-rc.1

## Dansk

- Understøtter lokal tale fra Piper via Home Assistant uden Nabu Casa-abonnement.
- Piper vælges automatisk, hvis tjenesten findes. En anden TTS-tjeneste kan vælges eksplicit under robotindstillingerne.
- Lyden afspilles på den enhed, dashboardet er åbnet på. Taletempo, stop og mundanimation virker også med lokal lyd.
- Installer og start Piper, vælg en passende stemme og tilføj Wyoming-integrationen først. Browseren kan kræve et tryk før lydafspilning. Den fysiske Shelly-skærm er endnu ikke afprøvet.

## English

- Supports local Piper speech through Home Assistant without a Nabu Casa subscription.
- Automatically selects Piper when available. Another TTS service may be explicitly selected in robot settings.
- Audio plays on the device displaying the dashboard. Speech speed, stop and mouth animation support local audio.
- Install and start Piper with a matching voice, then add the Wyoming integration. Browsers may require a user gesture before playback. Physical Shelly display playback has not yet been tested.

# 1.7.5-rc.1

## Dansk

- Skift af stemme eller taletempo genstarter igangværende tale med det nye valg.
- Prøv stemmen starter altid en ny prøve i stedet for kun at stoppe igangværende tale.
- Tilføjer 50 %, 130 % og 150 % samt lokal hukommelse, hvis browserlagring er blokeret.

## English

- Changing voice or speech speed restarts active speech with the new setting.
- Test voice always starts a fresh sample instead of merely stopping current speech.
- Adds 50%, 130% and 150% speeds and in-memory settings when browser storage is blocked.

# 1.7.4-rc.1

## Dansk

- Tilføjer Stemme og taletempo i chatvinduet med enhedens tilgængelige stemmer og en prøveknap. Valg gemmes lokalt pr. profil og sprog.
- Tilføjer foretrukken stemmetype og taletempo under robotindstillingerne. Standardtempo er 85 % for roligere oplæsning.
- Velkomst og svar bruger samme stemmevalg. En passende stemme skal være installeret på enheden.

## English

- Adds Voice and speed in the chat window with available device voices and a test button. Choices are saved locally per profile and language.
- Adds preferred voice type and speech speed to robot settings. Default speed is 85% for slower playback.
- Greetings and answers use the same voice settings. A matching voice must be installed on the device.

# 1.7.3-rc.1

## Dansk

- Tilføjer Robottens navn under Konfigurer → Robot. Navnet kan ændres uden at ændre opsætningsprofilens navn.
- Viser navnet i chatoverskriften og bruger det i den talte velkomst. Standardnavn: Huself Kræz.

## English

- Adds Robot name under Configure → Robot. Change it independently of the setup profile name.
- Uses the name in the chat heading and spoken greeting. Default name: Huself Kræz.

# 1.7.2-rc.1

## Dansk

- Gendanner Skjul robot-knappen i chatvinduet. Robotten kan skjules og åbnes igen med Vis robot-knappen i hjørnet.

## English

- Restores the Hide robot button in the chat window. Hide the robot and reopen it using the Show robot button in the corner.

# 1.7.1-rc.1

## Dansk

- Nyt versionsnummer, så opdateringen sorteres over de gamle 1.7.0-rc-versioner i HACS.
- Indeholder den nye robot, chatvindue, seks danse og velkomst på valgt sprog fra rc.15.

## English

- New version number so the update sorts above the older 1.7.0 release candidates in HACS.
- Includes the new robot, redesigned chat, six dances and localized greeting from rc.15.

# 1.7.0-rc.15

## Dansk

- Seks danse med tilfældige skift under musik: hop, svaj, twist, sidetrin, nik og vink.
- Automatisk velkomst på valgt dansk, engelsk eller tysk, når robotten tilsluttes dashboardet.
- Hvis browseren blokerer automatisk tale, forsøges igen efter brugerens næste interaktion. En passende talestemme skal være installeret.
- Velkomsten afbryder ikke en aktiv samtale, og dans respekterer reduceret bevægelse.

## English

- Six dances with randomized changes during music: bounce, sway, twist, step, nod and wave.
- Automatic greeting in the selected Danish, English or German language when the robot joins the dashboard.
- If the browser blocks automatic speech, the greeting is retried after the next user interaction. A matching system voice is required.
- The greeting does not interrupt an active conversation, and dancing respects reduced motion.

# 1.7.0-rc.14

## Dansk

- Nyt chatvindue med beskedbobler for spørgsmål og svar og historik for op til 20 spørgsmål i den åbne samtale.
- Større skrivefelt, tydelig mikrofonknap og oplæsning ved hvert svar.
- Fjerner de synlige genveje og pakkehjælpen fra chatvinduet. Du kan fortsat spørge om de valgte funktioner.

## English

- Redesigned chat window with question and answer bubbles and up to 20 turns in the current conversation.
- Larger text field, a prominent microphone button and a read-aloud button for each answer.
- Removes visible shortcuts and parcel help from the chat window. Configured features remain available through questions.

# 1.7.0-rc.13

## Dansk

- Robotten vinker ved åbning af dashboardet og bevæger munden under oplæsning.
- Bevarer den nye hvide robotfigur og lysglød ved tale og lytning.
- Respekterer enhedens indstilling for reduceret bevægelse.

## English

- The robot waves when the dashboard opens and moves its mouth during speech playback.
- Keeps the new white robot artwork and the glow while speaking and listening.
- Respects the device's reduced-motion preference.

# 1.7.0-rc.12

## Dansk

- Ny hvid robotfigur med blå øjne og gennemsigtig baggrund.
- Let svævende animation og lysglød ved tale og lytning. Figuren bruger et statisk billede uden separate mund- og øjenbevægelser.

## English

- New white robot character with blue eyes and a transparent background.
- Gentle floating animation and a glow while speaking or listening. The character uses a static image without separate mouth or eye movements.

# 1.7.0-rc.11

- Fjerner Se pakker-knappen helt fra robotvinduets handlingslinje. Pakkeoversigten kan fortsat åbnes via spørgsmål og Pakker-genvejen.

# 1.7.0-rc.10

- Taleboblen over robotten viser en neutral invitation i stedet for automatisk pakkestatus. Pakkestatus vises ved spørgsmål eller åbning af pakkeoversigten.

# 1.7.0-rc.9

- Viser en enkel Se pakker-knap uden pakketæller i velkomsten.
- Skjuler pakkefunktioner, når listen over valgte pakkekilder er tom, også ved gamle sensorvalg.
- Indeholder rettelsen af PostNord- og GLS-handlingerne fra rc.8.

# 1.7.0-rc.8

- Retter tilføjelse og fjernelse af PostNord- og GLS-pakkesporing: config_entry_id sendes kun, når den installerede handling understøtter feltet.
- Bevarer kontovalg for DHL og beskyttelsen mod flere valgte konti.

# 1.7.0-rc.7

- Retter pakkesvar til at bruge den transportør, der spørges om, og bede tydeligt om manglende pakkenummer på dansk, engelsk og tysk.
- Tilføjer DAO-visning og forklarer, at DAO og Bring importerer pakker fra kontoen uden manuel tilføjelse gennem robotten.
- Spørgsmål uden transportør viser kun brugerens valgte transportører.

# 1.7.0-rc.6

- Tilføjer visning af Bring- og DHL-pakker samt svar filtreret efter transportør.
- DHL-pakker kan tilføjes og fjernes gennem robotten. Bring hentes automatisk fra kontoen; robotten forklarer, at manuel tilføjelse ikke understøttes.
- Pakkekilder bruger integrationens identitet og sensorrolle, så omdøbte sensorer også genkendes.

# 1.7.0-rc.5

- Robotten starter med en generel velkomst, også når pakkesporing er valgt. Pakkestatus vises ved spørgsmål om pakker eller åbning af pakkeoversigten.

# 1.7.0-rc.4

- Retter automatisk oplæsning af brændstofpriser og andre lokale svar ved stemmespørgsmål. Skrevne spørgsmål starter ikke oplæsning.

# 1.7.0-rc.3

- Retter sammenblanding af benzin- og dieselpriser. Alle brændstofsensorer fra valgte integrationer medtages, og svaret angiver sensorens navn.
- Brændstofspørgsmål bruger aktuelle sensorværdier, også med en AI-assistent. Manglende typer erstattes aldrig af diesel.

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
