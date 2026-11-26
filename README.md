# Hitster Card Generator 🎵

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20App-red?style=for-the-badge&logo=streamlit)](https://hitster-custom-card-generator.streamlit.app/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github)](https://github.com/Pineapple-Geek/hitster-card-generator)

**Generate custom Hitster-style music game cards from any Spotify playlist!**  
**Créez des cartes personnalisées pour un jeu musical de type Hitster à partir de vos playlists Spotify !**

Turn your favorite playlists into a physical card game. Generate cards with QR codes on the front and year-based coloured solutions on the back, then export everything as a print-ready PDF.  
Transformez vos playlists préférées en jeu de cartes. Créez des cartes avec des QR codes au recto et les années de sortie au verso, puis exportez le tout dans un PDF prêt à imprimer.

> [!IMPORTANT]
> **Spotify API update / Mise à jour de l'API Spotify (2026):** Spotify has temporarily disabled app creation for some new developer accounts. The web app and its scraper mode can work without API credentials.  
> Spotify a temporairement désactivé la création d'applications pour certains nouveaux comptes développeur. L'application web et son mode de récupération des données peuvent fonctionner sans identifiants API.

---

## 🌍 Language / Langue

The web interface includes a **Français / English** language selector. French is selected by default. The application title, **Hitster Card Generator**, always stays in English.  
L'interface web propose un sélecteur de langue **Français / English**. Le français est sélectionné par défaut. Le titre de l'application, **Hitster Card Generator**, reste toujours en anglais.

## 👀 Preview / Aperçu

| **Front — Scan to Play / Recto — Scanner pour jouer** | **Back — Solutions / Verso — Réponses** |
|:---:|:---:|
| <img src="example_pictures/qr_code_side.png" width="400" alt="QR code side / Recto QR code"> | <img src="example_pictures/solution_side.png" width="400" alt="Solution side / Verso réponses"> |
| *Neon QR design / QR code avec effet néon* | *Year-based colours / Couleurs selon l'année* |

---

## ✨ Features / Fonctionnalités

| Feature / Fonctionnalité | Details / Description |
|---|---|
| 🌐 **Bilingual web interface / Interface web bilingue** | Switch between French and English. / Passez du français à l'anglais. |
| 🔗 **No API key required / Aucune clé API nécessaire** | Imports public Spotify track and playlist links. / Récupère les titres et playlists Spotify publics. |
| 📋 **Playlist URL support / Import de playlists** | Import tracks from a playlist URL. / Importez les morceaux depuis le lien d'une playlist. |
| ✏️ **Year editing / Modification des années** | Review and correct release years before creating the PDF. / Vérifiez et corrigez les années avant de créer le PDF. |
| 🎨 **Neon QR design / QR codes néon** | Customizable neon rings and QR appearance. / Personnalisez les anneaux néon et l'apparence des QR codes. |
| 🎯 **Dynamic colours / Couleurs dynamiques** | Colour gradient based on release years. / Dégradé de couleurs basé sur les années de sortie. |
| 🖨️ **Custom PDF layout / Mise en page PDF personnalisable** | Adjust card size, number of columns and rows per page. / Réglez la taille des cartes ainsi que le nombre de colonnes et de lignes par page. |
| ↔️ **Card spacing / Espacement des cartes** | Set the gap between cards, from 0 to 1 cm. / Réglez l'espace entre les cartes, de 0 à 1 cm. |
| 🖨️ **Print-ready PDF / PDF prêt à imprimer** | A4 output with duplex-friendly card positioning. / Export A4 avec positionnement adapté à l'impression recto verso. |
| 💡 **Ink-saving mode / Mode économie d'encre** | White background and black text option. / Option fond blanc et texte noir. |
| ✂️ **Cutting borders / Traits de découpe** | Optional borders to make cutting easier. / Ajout facultatif de contours pour faciliter la découpe. |
| 🏷️ **Card labels / Étiquettes des cartes** | Add a custom label, such as an event or playlist name. / Ajoutez une étiquette personnalisée, par exemple le nom d'un événement ou d'une playlist. |
| 🖼️ **Custom backgrounds / Arrière-plans personnalisés** | Upload your own card background images. / Importez vos propres images d'arrière-plan. |
| 📱 **Scan-safe QR / QR codes faciles à scanner** | Choose transparent or solid QR backgrounds. / Choisissez un fond de QR code transparent ou uni. |
| 🔤 **Game titles / Titres personnalisés** | Add and position a title on your cards. / Ajoutez un titre et choisissez son emplacement sur les cartes. |

---

## 🚀 Quick Start / Démarrage rapide

### Option A — Web app / Application web (recommended / recommandée)

👉 **[Open Hitster Card Generator / Ouvrir Hitster Card Generator](https://hitster-custom-card-generator.streamlit.app/)**

1. **Copy links / Copier les liens** — In Spotify Desktop, open a playlist, select the tracks (`Ctrl+A`) and copy (`Ctrl+C`). You can also paste individual track links.  
   Dans Spotify Desktop, ouvrez une playlist, sélectionnez les morceaux (`Ctrl+A`) puis copiez-les (`Ctrl+C`). Vous pouvez aussi coller des liens de morceaux individuellement.
2. **Paste / Coller** — Paste the links or a playlist URL into the text area.  
   Collez les liens ou l'URL d'une playlist dans la zone de texte.
3. **Review / Vérifier** — Check the imported tracks and correct any release years.  
   Vérifiez les morceaux importés et corrigez les années de sortie si nécessaire.
4. **Customize / Personnaliser** — Choose the card size, page layout, spacing and visual design.  
   Choisissez la taille des cartes, la disposition sur la page, l'espacement et le design.
5. **Create and download / Créer et télécharger** — Click **Create My PDF**, then print the PDF double-sided.  
   Cliquez sur **Create My PDF**, puis imprimez le PDF en recto verso.

### Option B — Local CLI / Utilisation en ligne de commande

```bash
git clone https://github.com/Pineapple-Geek/hitster-card-generator.git
cd hitster-card-generator
pip install -r requirements.txt
```

**Scraper mode (no API key) / Mode récupération (sans clé API):**

1. Copy track links from Spotify Desktop (`Ctrl+A` → `Ctrl+C`).  
   Copiez les liens des morceaux depuis Spotify Desktop (`Ctrl+A` → `Ctrl+C`).
2. Save them in a file named `links.txt` in the project root.  
   Enregistrez-les dans un fichier nommé `links.txt` à la racine du projet.
3. Run the script / Lancez le script:

```bash
python src/hitster_card_creator.py
# Optional options / Options facultatives:
python src/hitster_card_creator.py --ink-save-mode --card-draw-border --card-label "Game Night"
python src/hitster_card_creator.py --qr-bg-mode solid --game-title "Hits"
```

**API mode (optional) / Mode API (facultatif):**

```bash
cp .env.example .env
# Add CLIENT_ID, CLIENT_SECRET and PLAYLIST_URL to .env
# Ajoutez CLIENT_ID, CLIENT_SECRET et PLAYLIST_URL dans le fichier .env
python src/hitster_card_creator.py
```

---

## 🎨 Card customization / Personnalisation des cartes

The web app provides visual settings in the sidebar.  
L'application web propose des réglages visuels dans la barre latérale.

### 📱 QR side design / Design du recto QR

- **Background type / Type d'arrière-plan:** choose `Neon Rings`, `Solid Color` or `Custom Image`. / Choisissez `Neon Rings`, `Solid Color` ou `Custom Image`.
- **Neon rings / Anneaux néon:** adjust their thickness, colours and number. / Réglez leur épaisseur, leurs couleurs et leur nombre.
- **QR background mode / Fond du QR code:**  
  - `Transparent`: the neon design remains visible through the QR code. / Le design néon reste visible à travers le QR code.
  - `Solid`: adds a solid square or rounded background for easier scanning. / Ajoute un fond uni carré ou arrondi pour faciliter la lecture.
- **QR colours and size / Couleurs et taille du QR code:** customize the QR modules, background and dimensions. / Personnalisez les modules, le fond et les dimensions du QR code.

### 🔤 Game titles and labels / Titres et étiquettes

- Add a custom title, such as `90s Party` or `Wedding 2026`. / Ajoutez un titre personnalisé, par exemple `Soirée années 90` ou `Mariage 2026`.
- Position it at the top, bottom or vertically on the sides. / Placez-le en haut, en bas ou verticalement sur les côtés.
- Adjust font size, colour and background boxes. / Réglez la taille de police, la couleur et le fond du texte.

### 🖼️ Custom background image / Image d'arrière-plan personnalisée

1. Select **Background Type: Image** in the sidebar. / Sélectionnez **Background Type: Image** dans la barre latérale.
2. Upload a square image (2000 × 2000 px recommended). / Importez une image carrée (2000 × 2000 px recommandé).
3. The image is automatically cropped and resized to fit the card. / L'image est automatiquement recadrée et redimensionnée.
4. For busy backgrounds, use **Solid QR Background Mode** to keep the QR code easy to scan. / Pour les images chargées, utilisez **Solid QR Background Mode** afin de conserver un QR code facile à scanner.

---

## 🖨️ PDF layout and printing / Mise en page PDF et impression

The custom web version adds layout controls so you can adapt the PDF to your paper, printer and cutting preferences.  
La version personnalisée ajoute des réglages de mise en page pour adapter le PDF à votre papier, votre imprimante et vos préférences de découpe.

- **Card size / Taille des cartes:** set the dimensions of each card. / Définissez les dimensions de chaque carte.
- **Columns and rows / Colonnes et lignes:** choose how many cards appear across and down each page. / Choisissez le nombre de cartes en largeur et en hauteur sur chaque page.
- **Space between cards / Espace entre les cartes:** set the gap between cards from 0 to 1 cm. / Réglez l'espace entre les cartes de 0 à 1 cm.
- The layout is centered on A4 pages and the back side is positioned for duplex printing. / La grille est centrée sur des pages A4 et le verso est positionné pour l'impression recto verso.

**Printing tips / Conseils d'impression:**

1. Print double-sided and select the flip direction that matches your printer and card layout. Check with a test sheet first.  
   Imprimez en recto verso et choisissez le sens de retournement adapté à votre imprimante et à la disposition des cartes. Faites d'abord un essai sur une feuille.
2. Cut along the spaces or optional cutting borders. / Découpez en suivant les espaces ou les contours de découpe facultatifs.
3. Select **Actual size / Taille réelle** in the printer settings rather than **Fit to page / Ajuster à la page**, to preserve the card dimensions and QR readability.  
   Sélectionnez **Taille réelle** dans les paramètres d'impression plutôt que **Ajuster à la page**, afin de conserver les dimensions des cartes et la lisibilité des QR codes.

---

## ⚙️ CLI configuration / Configuration CLI

The command-line options below are available for the local script. Web-only layout controls (card size, page rows/columns and spacing) are configured in the web interface.  
Les options ci-dessous concernent le script en ligne de commande. Les réglages de mise en page web (taille des cartes, lignes/colonnes et espacement) se configurent dans l'interface web.

| Setting / Réglage | CLI flag | `.env` variable | Default / Défaut |
|---|---|---|---|
| Ink saving mode / Économie d'encre | `--ink-save-mode` | `INK_SAVING_MODE=true` | `false` |
| Cutting borders / Contours de découpe | `--card-draw-border` | `CARD_DRAW_BORDER=true` | `false` |
| Card label / Étiquette | `--card-label "text"` | `CARD_LABEL=text` | *(none / aucun)* |
| QR background mode / Fond du QR | `--qr-bg-mode` | `QR_BG_MODE=solid` | `transparent` |
| QR module colour / Couleur du QR | `--qr-module-color` | `QR_MODULE_COLOR=#FFFFFF` | `#000000` |
| Background type / Type de fond | `--bg-type` | `BG_TYPE=neon_rings` | `neon_rings` |
| Game title / Titre du jeu | `--game-title` | `GAME_TITLE=MyGame` | *(none / aucun)* |

### Colour gradient / Dégradé de couleurs

Edit the `COLOR_GRADIENT` list in the configuration section of `src/hitster_card_creator.py`.  
Modifiez la liste `COLOR_GRADIENT` dans la section de configuration de `src/hitster_card_creator.py`.

```python
COLOR_GRADIENT = [
    "#7030A0",  # Purple / Violet (oldest / plus ancien)
    "#E31C79",  # Pink / Rose
    "#FF6B9D",  # Light pink / Rose clair
    "#FFA500",  # Orange
    "#FFD700",  # Gold / Doré
    "#87CEEB",  # Sky blue / Bleu ciel
    "#4169E1",  # Royal blue / Bleu roi (newest / plus récent)
]
```

---

## 🔑 Spotify API credentials (optional) / Identifiants API Spotify (facultatifs)

API credentials are only necessary if you need to retrieve playlists beyond the scraper's supported limit.  
Les identifiants API sont uniquement nécessaires si vous souhaitez récupérer des playlists dépassant la limite prise en charge par le mode de récupération sans API.

1. Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard). / Rendez-vous sur le [tableau de bord Spotify Developer](https://developer.spotify.com/dashboard).
2. Create an app if your account is allowed to, using `https://localhost` as the Redirect URI and enabling **Web API**. / Créez une application si votre compte le permet, avec `https://localhost` comme URI de redirection et **Web API** activée.
3. Copy your **Client ID** and **Client Secret**. / Copiez votre **Client ID** et votre **Client Secret**.
4. Enter them in the web app sidebar or in your `.env` file. / Saisissez-les dans la barre latérale de l'application web ou dans votre fichier `.env`.

---

## 🔧 Fixing incorrect years / Corriger les années incorrectes

Spotify metadata may show a remaster or re-release year instead of the original release year.  
Les métadonnées Spotify peuvent afficher l'année d'une remastérisation ou d'une réédition plutôt que l'année de sortie originale.

**Web app / Application web:** edit the **Year** column directly in the review table.  
Modifiez directement la colonne **Year** dans le tableau de vérification.

**CLI:**

1. Run the script once; it saves `output/hitster_cards/songs.json`. / Lancez le script une première fois ; il crée `output/hitster_cards/songs.json`.
2. Edit the years in the JSON file manually, or ask an AI assistant to correct the original release years while preserving valid JSON. / Modifiez les années dans le fichier JSON ou demandez à un assistant IA de corriger les années de sortie originales en conservant un JSON valide.
3. Run the script again without `--fetch` to reuse the corrected file. / Relancez le script sans `--fetch` pour réutiliser le fichier corrigé.

---

## 📂 Output files / Fichiers générés

| File / Fichier | Description |
|---|---|
| `output/hitster_cards/card_NNN_qr.png` | QR-side card images / Images du recto avec QR code |
| `output/hitster_cards/card_NNN_solution.png` | Solution-side card images / Images du verso avec les réponses |
| `output/hitster_cards/songs.json` | Editable song metadata / Métadonnées des morceaux modifiables |
| `output/hitster_cards.pdf` | Print-ready PDF / PDF prêt à imprimer |

---

## 🐛 Troubleshooting / Dépannage

| Problem / Problème | Fix / Solution |
|---|---|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt`. / Lancez `pip install -r requirements.txt`. |
| Playlist not found (404) / Playlist introuvable (404) | Make sure the playlist is public. / Vérifiez que la playlist est publique. |
| QR codes won't scan / Les QR codes ne se scannent pas | Print at actual size and use high-quality settings. / Imprimez à taille réelle avec une qualité élevée. |
| Download button does not respond on mobile / Le téléchargement ne fonctionne pas sur mobile | Try using a desktop browser. / Essayez avec un navigateur sur ordinateur. |
| Card spacing does not appear / L'espacement n'apparaît pas | Generate a new PDF after changing the spacing setting; the gap is visible in the PDF, not in the single-card preview. / Après avoir modifié l'espacement, générez un nouveau PDF ; l'espace est visible dans le PDF et non dans l'aperçu d'une carte seule. |

---

## 🤝 Contributing / Contribuer

Pull requests and suggestions are welcome. Ideas include new card designs, support for other music platforms and improved release-year accuracy.  
Les contributions et suggestions sont les bienvenues : nouveaux designs de cartes, prise en charge d'autres plateformes musicales et amélioration de la précision des années de sortie.

## 🤝 Contributors / Contributeurs

Thanks to everyone who has helped improve the original project.  
Merci à toutes les personnes qui ont contribué à améliorer le projet d'origine.

- **[cdaller](https://github.com/cdaller)** — Ink-saving mode, improved QR code logic and year accuracy. / Mode économie d'encre, amélioration des QR codes et de la précision des années.
- **[thommy86](https://github.com/thommy86)** — Streamlit interface overhaul, game titles and custom backgrounds. / Refonte de l'interface Streamlit, titres de jeu et arrière-plans personnalisés.

---

## 📜 License / Licence

MIT License — see [LICENSE](LICENSE).  
Licence MIT — consultez le fichier [LICENSE](LICENSE).

## Credits / Crédits

- Inspired by the original [Hitster game](https://www.jumbodiset.com/hitster). / Inspiré du jeu original [Hitster](https://www.jumbodiset.com/hitster).
- [Montserrat](https://github.com/JulietaUla/Montserrat) font by Julieta Ulanovsky. / Police [Montserrat](https://github.com/JulietaUla/Montserrat) créée par Julieta Ulanovsky.
