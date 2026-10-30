# Dashboard Robot

A floating Home Assistant dashboard companion with text chat, optional voice input and an optional AI conversation agent.

**First public preview: v1.7.0-rc.9.** Tested by the author in an existing Home Assistant installation; broader clean-install and browser testing is still welcome.

## Screenshots / Billeder

### Chat with your home / Tal med dit hjem

Text chat, voice input and shortcuts in the robot panel.

<a href="https://github.com/user-attachments/assets/d729f5f3-c2ec-4e4e-aeab-6705753ff2df"><img src="https://github.com/user-attachments/assets/d729f5f3-c2ec-4e4e-aeab-6705753ff2df" alt="Dashboard Robot chat panel with text input, voice input and feature shortcuts" width="760" /></a>

### Floating dashboard companion / Robot på dashboardet

Tap the robot to open the chat panel.

<a href="https://github.com/user-attachments/assets/db884a8f-18b4-4b69-afb1-7ce118b2917e"><img src="https://github.com/user-attachments/assets/db884a8f-18b4-4b69-afb1-7ce118b2917e" alt="Floating robot in the corner of a Home Assistant dashboard" width="560" /></a>

<details>
<summary><strong>Setup screenshots / Se billeder af opsætningen</strong></summary>

The screenshots show a Danish example installation. Labels and layout may vary between versions.

#### 1. Add the integration / Tilføj integrationen

<a href="https://github.com/user-attachments/assets/6124183b-a269-4d0b-a49d-1805dc0c20a2"><img src="https://github.com/user-attachments/assets/6124183b-a269-4d0b-a49d-1805dc0c20a2" alt="Find Dashboard Robot in Home Assistant integrations" width="560" /></a>

<table>
<tr>
<td width="50%" valign="top">

<strong>2. Choose rooms / Vælg rum</strong><br><br>
<a href="https://github.com/user-attachments/assets/cf96d87f-f4b7-4741-94d0-84546c175f5d"><img src="https://github.com/user-attachments/assets/cf96d87f-f4b7-4741-94d0-84546c175f5d" alt="Select the rooms available to Dashboard Robot" width="360" /></a>

</td>
<td width="50%" valign="top">

<strong>3. Language and AI / Sprog og AI</strong><br><br>
<a href="https://github.com/user-attachments/assets/31356d9d-cf8f-481d-8e68-334c3fd4ec91"><img src="https://github.com/user-attachments/assets/31356d9d-cf8f-481d-8e68-334c3fd4ec91" alt="Choose language and an AI conversation agent" width="360" /></a>

</td>
</tr>
<tr>
<td width="50%" valign="top">

<strong>4. Choose dashboards / Vælg dashboards</strong><br><br>
<a href="https://github.com/user-attachments/assets/96f67fce-4bbd-484e-ada2-80f377e26f67"><img src="https://github.com/user-attachments/assets/96f67fce-4bbd-484e-ada2-80f377e26f67" alt="Select the dashboards where the robot should appear" width="360" /></a>

</td>
<td width="50%" valign="top">

<strong>5. Installed integrations / Installerede integrationer</strong><br><br>
<a href="https://github.com/user-attachments/assets/4f60817f-684a-4a45-a735-a53936b4e78f"><img src="https://github.com/user-attachments/assets/4f60817f-684a-4a45-a735-a53936b4e78f" alt="Choose installed integrations as information sources" width="360" /></a>

</td>
</tr>
<tr>
<td width="50%" valign="top">

<strong>6. Optional settings / Valgfrie indstillinger</strong><br><br>
<a href="https://github.com/user-attachments/assets/1a0be629-06a5-443c-95eb-a6c3697ebfa5"><img src="https://github.com/user-attachments/assets/1a0be629-06a5-443c-95eb-a6c3697ebfa5" alt="Enable optional device and extra sensor settings" width="360" /></a>

</td>
<td width="50%" valign="top">

<strong>7. Manual device selection / Manuelle enhedsvalg</strong><br><br>
<a href="https://github.com/user-attachments/assets/3d4e5d7a-b834-4aef-8edb-76405b626006"><img src="https://github.com/user-attachments/assets/3d4e5d7a-b834-4aef-8edb-76405b626006" alt="Select lights, speakers and cameras available to the robot" width="360" /></a>

</td>
</tr>
</table>

</details>

## Features

- Danish, English and German interface.
- Multiple dashboard profiles and optional view restrictions.
- Room selection finds lights, speakers and all room cameras.
- Optional manual device choices, including speakers and cameras without an area.
- Camera chooser and room/name questions.
- Choose installed integrations and review sensor suggestions for electricity, power, fuel, waste, weather and compatible parcels.
- Optional extra sensor readings; optional existing Home Assistant conversation agent.
- Drag the robot, hide/show it, and use keyboard movement and reduced-motion preferences.

Installed integrations are discovered through registered entities. Suggestions use domains, units, device classes and names; unknown integrations are not automatically understood or controlled. Device commands support selected lights and media players. Camera viewing opens Home Assistant's entity dialog. No heating or lock control is implemented.

## Requirements

Home Assistant 2026.10 or newer and a modern browser. Voice input requires HTTPS, microphone permission and browser speech-recognition support. Reading aloud requires a suitable voice installed on the device. AI requires your own configured conversation integration. Text and supported local commands can be used without AI.

## AI chat: set up Google Gemini first

**For free-form AI conversation, first add Google Gemini (Google Generative AI) or another compatible conversation integration to Home Assistant.** Dashboard Robot does not install an AI provider or include an API key.

1. Open **Settings → Devices & services → Add integration → Google Gemini**.
2. Follow the setup instructions using your own Google AI API key. See the [official Gemini setup guide](https://www.home-assistant.io/integrations/google_generative_ai_conversation/).
3. Open **Dashboard Robot → Configure → Robot** and select its conversation entity under **AI assistant**, for example **Google AI Conversation**.
4. Complete the setup and save.

Without an AI assistant, supported basic commands and configured sensor answers still work; general AI chat is unavailable.

**Dansk:** Vil du bruge fri AI-samtale, skal du først tilføje **Google Gemini / Google Generative AI** eller en anden kompatibel AI-assistent i Home Assistant. Vælg derefter **Google AI Conversation** under **Dashboard Robot → Konfigurer → Robot → AI-assistent**, og gem opsætningen. Grundfunktionerne virker uden AI. Du skal bruge din egen API-nøgle til Gemini.

## Install with HACS

This is a **custom repository**, not an entry in the HACS default catalogue.

1. Open HACS and its custom repositories menu.
2. Add `https://github.com/DarkPayload1/dashboard-robot-for-Home-assistant` with category **Integration**.
3. Download Dashboard Robot. Enable prerelease versions if the preview is not offered.
4. Restart Home Assistant.
5. Open **Settings → Devices & services → Add integration → Dashboard Robot**.
6. Follow setup and refresh your dashboard browser.

The repository must be public for other users to download it through HACS.

## Manual installation

Download `dashboard_robot.zip` from [Releases](https://github.com/DarkPayload1/dashboard-robot-for-Home-assistant/releases). Extract its contents into `config/custom_components/dashboard_robot/`, so that `manifest.json` is directly inside that folder. Restart Home Assistant, add the integration and refresh the dashboard.

Alternatively, copy `custom_components/dashboard_robot` from this repository into your configuration's `custom_components` folder.

## Setup

1. **Rooms:** choose rooms; lights, media players and cameras are detected. Media players without areas are included too; remove unwanted ones through manual settings.
2. **Robot:** choose language, dashboards and an optional AI assistant.
3. **Integrations:** choose sources, then review function sensors once. Ambiguous suggestions need your choice.

Manual devices and extra sensor readings each have an optional separate page. Existing extra readings are preserved when that page is skipped. A sensor's value and unit are used as provided; VAT and currency are not inferred.

Leave **View paths** empty to show the robot on all views of selected dashboards. A restricted path must match the URL segment, not the visible title: a view titled “Overblik” might have the path `oversigt`. Matching view-specific profiles take priority over dashboard-wide ones; the first profile wins ties.

On selected dashboards this robot temporarily hides older embedded parcel/wall robots, restoring their display when leaving. Their resources and settings are not deleted.

## Examples

- `Tænd lyset i stuen`
- `Hvad koster strømmen nu?`
- `Vis kamera i stue`
- `Pause musik i stuen`
- `Turn on lights in living room`
- `Zeige mir die Kamera`

Use your actual Home Assistant room/device names. Music resumes existing playback; it does not search for new music. Assign speakers an area for room commands; otherwise use their name.

Compatible GLS/PostNord parcel sensors must expose a `parcels` attribute. Adding tracking uses their integration's supported service. Deleting tracking requires confirmation. Other parcel providers are not guaranteed to support tracking commands.

## Privacy

No credentials, personal addresses or user-specific entity IDs are bundled. Only configured sources are read. With an AI agent, selected readings and parcel/music information are sent as context to that agent; its provider's retention policy applies. Browser voice recognition may use the browser vendor's online service. No analytics are included.

Device commands use the signed-in user's Home Assistant permissions. Selected entities define the robot's control scope, not an access-control boundary for other clients.

## Updates and feedback

Install updates through HACS or replace the same integration folder, then restart Home Assistant and refresh browsers. Existing configuration entries are retained. Preview releases may change; report reproducible problems through [Issues](https://github.com/DarkPayload1/dashboard-robot-for-Home-assistant/issues), without credentials or private sensor data.

## Development

```sh
python -m unittest discover -s tests
node --test tests/*.test.cjs
```

GitHub Actions runs tests, hassfest and HACS validation. A separate release workflow creates a prerelease and `dashboard_robot.zip` when the manifest version changes on `main`. Publishing does not imply acceptance into HACS's default catalogue.

MIT licensed. See [LICENSE](LICENSE).

### Bring and DHL / Bring og DHL

Select the Bring or DHL integration and its incoming, awaiting-pickup and delivered parcel sensors in Dashboard Robot settings. Ask about one carrier or all parcels. DHL supports adding and removing tracking numbers through the robot; removal requires confirmation. The Posten Bring account integration imports parcels automatically and does not support manual tracking changes.

Vælg Bring- eller DHL-integrationen og dens pakkesensorer i robotindstillingerne. Robotten kan vise pakker fra begge transportører og tilføje/fjerne DHL-sporing. Bring-pakker hentes automatisk fra din konto; manuel tilføjelse og fjernelse understøttes ikke.

DAO is also supported for reading account parcels. Like Bring, its account integration does not offer manual tracking changes through the robot. Select its parcel sensors in robot settings. / DAO-pakker kan også vises, når DAO-pakkesensorerne er valgt. Manuel tilføjelse foretages i DAO-appen.
