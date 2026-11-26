import streamlit as st
from PIL import Image
import pandas as pd
import src.utils as utils

# Per-session default for the year-color gradient. Settings are kept in
# st.session_state (per user) rather than a shared module global to avoid
# cross-session bleed when multiple users hit the same Streamlit server.
DEFAULT_COLOR_GRADIENT = [
    "#7030A0", "#E31C79", "#FF6B9D", "#FFA500",
    "#FFD700", "#87CEEB", "#4169E1",
]

OUTPUT_DIR = "output"
LINKS_FILE = "links.txt"


# French translations for the interface. The main title remains in English.
TRANSLATIONS = {
    "⚙️ Settings": "⚙️ Paramètres",
    "Customize your print layout": "Personnalisez la mise en page de vos cartes",
    "Global": "Général",
    "QR Side (Front)": "Face QR (recto)",
    "Solution Side (Back)": "Face réponses (verso)",
    "📄 Print & Layout": "📄 Impression et mise en page",
    "Card size (cm)": "Taille des cartes (cm)",
    "Square card size. The available rows and columns adapt to A4.": "La taille des cartes est carrée. Le nombre de lignes et de colonnes s'adapte au format A4.",
    "Space between cards (cm)": "Espacement entre les cartes (cm)",
    "Adds the same gap horizontally and vertically between cards.": "Ajoute le même espace horizontalement et verticalement entre les cartes.",
    "The spacing is visible in the generated PDF, not in the single-card preview.": "L'espacement est visible dans le PDF généré, pas dans l'aperçu d'une carte seule.",
    "Columns per page": "Colonnes par page",
    "Rows per page": "Lignes par page",
    "Ink Saving Mode": "Mode économie d'encre",
    "Use white background and black text to save ink.": "Utilise un fond blanc et du texte noir pour économiser l'encre.",
    "Draw Cutting Borders": "Afficher les traits de découpe",
    "Draw a line around each card for easier cutting.": "Trace un contour autour de chaque carte pour faciliter la découpe.",
    "Font Selection": "Choix de la police",
    "Custom...": "Personnalisée…",
    "Custom Google Font Name": "Nom de la police Google personnalisée",
    "Type any font name from Google Fonts.": "Saisissez le nom d'une police disponible sur Google Fonts.",
    "[🔍 Browse Google Fonts here](https://fonts.google.com/)": "[🔍 Parcourir les polices Google Fonts](https://fonts.google.com/)",
    "🔑 Spotify API Credentials (optional)": "🔑 Identifiants API Spotify (facultatif)",
    "Only needed when pasting a playlist URL. Without credentials, playlist URLs are limited to ~100 tracks. Pasting individual track links works without limits.": "Nécessaire uniquement pour importer une playlist. Sans identifiants, l'import est limité à environ 100 titres. Les liens de titres individuels ne sont pas soumis à cette limite.",
    "Client ID": "Identifiant client",
    "Client Secret": "Clé secrète client",
    "🖼️ Background": "🖼️ Arrière-plan",
    "Background Type": "Type d'arrière-plan",
    "Background Color": "Couleur de l'arrière-plan",
    "Upload Image (QR Side)": "Importer une image (face QR)",
    "Image Scale": "Échelle de l'image",
    "X Offset": "Décalage horizontal (X)",
    "Y Offset": "Décalage vertical (Y)",
    "Ring Thickness": "Épaisseur des anneaux",
    "Ring Count": "Nombre d'anneaux",
    "Neon Ring Colors": "Couleurs des anneaux néon",
    "➕ Add Color": "➕ Ajouter une couleur",
    "📱 QR Settings": "📱 Réglages du QR code",
    "QR Background Mode": "Fond du QR code",
    "QR Module Color": "Couleur des modules du QR code",
    "QR Backplate Color": "Couleur du support du QR code",
    "Backplate Padding": "Marge intérieure du support",
    "Backplate Corner Radius": "Arrondi des coins du support",
    "QR Size Ratio (%)": "Taille du QR code (%)",
    "🔤 Title": "🔤 Titre",
    "Enable Title": "Activer le titre",
    "Title Text": "Texte du titre",
    "Position": "Position",
    "Font Size": "Taille de la police",
    "Title Color": "Couleur du titre",
    "Draw Background Box": "Ajouter un fond au titre",
    "🎨 Color Gradient": "🎨 Dégradé de couleurs",
    "Year Color Gradient": "Dégradé de couleurs des années",
    "Colors map to the oldest to newest years.": "Les couleurs correspondent aux années, de la plus ancienne à la plus récente.",
    "Upload Image (Solution Side)": "Importer une image (face réponses)",
    "Ink Saving Border Thickness": "Épaisseur de la bordure d'économie d'encre",
    "Disclaimer, Accuracy & Support": "ℹ️ Informations et précision",
    "Generate custom music game cards from any Spotify playlist or track links.": "Créez des cartes personnalisées pour votre jeu musical à partir d'une playlist Spotify ou de liens de titres.",
    "How do I get links?": "Comment récupérer les liens ?",
    "**Option A — Individual Tracks:**": "**Option A — Titres individuels :**",
    "1. Open **Spotify Desktop**.": "1. Ouvrez **Spotify sur ordinateur**.",
    "2. Go to your playlist.": "2. Ouvrez votre playlist.",
    "3. Select songs (**Ctrl+A**).": "3. Sélectionnez les titres (**Ctrl+A**).",
    "4. Copy (**Ctrl+C**).": "4. Copiez (**Ctrl+C**).",
    "5. Paste below!": "5. Collez les liens ci-dessous !",
    "**Option B — Playlist URL:**": "**Option B — Lien d'une playlist :**",
    "1. Right-click your playlist → **Share** → **Copy link**.": "1. Faites un clic droit sur votre playlist → **Partager** → **Copier le lien**.",
    "2. Paste the playlist URL below!": "2. Collez le lien de la playlist ci-dessous !",
    "**Supported formats:**": "**Formats acceptés :**",
    "- Track links:": "- Liens de titres :",
    "- Playlist links:": "- Liens de playlists :",
    "Input": "Liens Spotify",
    "✨ Load Example Tracks": "✨ Charger des exemples de titres",
    "📋 Load Example Playlist": "📋 Charger une playlist d'exemple",
    "Paste Spotify links here:": "Collez vos liens Spotify ici :",
    "🎶 Spotify **playlist** URL detected!": "🎶 Lien de **playlist Spotify** détecté !",
    "No valid Spotify links detected yet.": "Aucun lien Spotify valide détecté pour le moment.",
    "🔍 Fetch Song Metadata": "🔍 Récupérer les informations des titres",
    "Please paste some valid Spotify links first!": "Veuillez d'abord coller des liens Spotify valides !",
    "Fetching metadata...": "Récupération des informations…",
    "Starting...": "Démarrage…",
    "Using Spotify API to fetch playlist...": "Utilisation de l'API Spotify pour récupérer la playlist…",
    "Done!": "Terminé !",
    "Scraping playlist page for track links (no API key)...": "Récupération des liens de titres depuis la page de la playlist (sans clé API)…",
    "Could not extract tracks from the playlist page. ": "Impossible d'extraire les titres depuis la page de la playlist. ",
    "Try adding Spotify API credentials in the sidebar, ": "Ajoutez vos identifiants API Spotify dans les paramètres ou ",
    "or paste individual track links instead.": "collez directement les liens des titres.",
    "Scraping track metadata...": "Récupération des informations des titres…",
    "📝 Review & Edit Songs": "📝 Vérifier et modifier les titres",
    "Fix any incorrect years before generating cards. ": "Corrigez les années incorrectes avant de créer les cartes. ",
    "Songs with unknown years show as empty — fill them in!": "Les titres dont l'année est inconnue sont laissés vides : renseignez-les !",
    "Artist": "Artiste",
    "Song": "Titre",
    "Year": "Année",
    "Source": "Origine",
    "Link": "Lien",
    "Edit this to fix incorrect years!": "Modifiez cette valeur pour corriger une année incorrecte !",
    "Where the year came from": "Origine de l'année indiquée",
    "👀 Card Preview": "👀 Aperçu des cartes",
    "Preview card for:": "Afficher la carte de :",
    "QR Side": "Face QR",
    "Solution Side": "Face réponses",
    "🎴 Create My PDF": "🎴 Créer mon PDF",
    "Generating cards...": "Création des cartes…",
    "Starting PDF generation...": "Démarrage de la création du PDF…",
    "✅ All Cards Generated!": "✅ Toutes les cartes ont été créées !",
    "💾 Download Printable PDF": "💾 Télécharger le PDF prêt à imprimer",
    "Found {count} tracks. Scraping metadata...": "{count} titres trouvés. Récupération des informations…",
    "✅ Fetched {count} songs!": "✅ {count} titre(s) récupéré(s) !",
    "🎵 {count} Spotify **track link(s)** detected.": "🎵 {count} lien(s) de **titre Spotify** détecté(s).",
    "⚠️ {count} song(s) have no year. Please fill them in above, or they will show as '????' on the cards.": "⚠️ {count} titre(s) n'ont pas d'année. Renseignez-les ci-dessus, sinon « ???? » apparaîtra sur les cartes.",
    "{count} cards per page ({cols} columns × {rows} rows)": "{count} cartes par page ({cols} colonnes × {rows} lignes)",
    "neon_rings": "Anneaux néon",
    "solid": "Couleur unie",
    "image": "Image",
    "gradient": "Dégradé",
    "transparent": "Transparent",
    "top": "En haut",
    "bottom": "En bas",
    "top_left": "En haut à gauche",
    "top_right": "En haut à droite",
    "bottom_left": "En bas à gauche",
    "bottom_right": "En bas à droite",
    "center_above_qr": "Centré au-dessus du QR code",
    "center_below_qr": "Centré sous le QR code",
    "in_border_bottom_right": "Dans la bordure, en bas à droite",
    "in_border_bottom_left": "Dans la bordure, en bas à gauche",
    "in_border_top_right": "Dans la bordure, en haut à droite",
    "in_border_top_left": "Dans la bordure, en haut à gauche"
}
def tr(value):
    if st.session_state.get("interface_language", "Français") != "Français":
        return value
    if value.startswith("Color ") and value[6:].isdigit():
        return "Couleur " + value[6:]
    return TRANSLATIONS.get(value, value)

# --- STATE INITIALIZATION ---
if "songs" not in st.session_state:
    st.session_state.songs = []
if "pdf_data" not in st.session_state:
    st.session_state.pdf_data = None

def reset_generation():
    st.session_state.pdf_data = None

def set_example_playlist():
    st.session_state.user_input = "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"
    reset_generation()

def set_example_links():
    st.session_state.user_input = (
        "https://open.spotify.com/track/4PTG3Z6ehGkBFwjybzWkR8?si=44d4b8822cac4dc8\n"
        "https://open.spotify.com/track/0Bo5fjMtTfCD8vHGebivqc?si=5bc94c4aadf84bca\n"
        "https://open.spotify.com/track/6Sy9BUbgFse0n0LPA5lwy5?si=ac74b629e3834310"
    )
    reset_generation()

def parse_input(text):
    if not text or not text.strip():
        return 'empty', None
    
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    if not lines:
        return 'empty', None

    if len(lines) == 1 and '/playlist/' in lines[0]:
        return 'playlist', lines[0]
    
    track_lines = [l for l in lines if '/track/' in l]
    if track_lines:
        return 'tracks', track_lines
    
    return 'empty', None

import uuid

def add_color_cb(key_prefix):
    st.session_state[f"{key_prefix}_items"].append({"id": str(uuid.uuid4()), "color": "#FFFFFF"})

def del_color_cb(key_prefix, index):
    st.session_state[f"{key_prefix}_items"].pop(index)

def move_up_cb(key_prefix, index):
    items = st.session_state[f"{key_prefix}_items"]
    items[index], items[index-1] = items[index-1], items[index]

def move_down_cb(key_prefix, index):
    items = st.session_state[f"{key_prefix}_items"]
    items[index], items[index+1] = items[index+1], items[index]

def dynamic_color_list(key_prefix, title, default_colors, help_text=""):
    """Renders a collapsible dynamic list of color pickers using UUIDs and callbacks to preserve state."""
    if f"{key_prefix}_items" not in st.session_state:
        st.session_state[f"{key_prefix}_items"] = [{"id": str(uuid.uuid4()), "color": c} for c in default_colors]
        
    items = st.session_state[f"{key_prefix}_items"]
    
    with st.expander(tr(title), expanded=False):
        if help_text:
            st.caption(tr(help_text))
            
        st.button(tr("➕ Add Color"), key=f"add_{key_prefix}", on_click=add_color_cb, args=(key_prefix,))
            
        for i, item in enumerate(items):
            color = item["color"]
            item_id = item["id"]
            
            # Parse color string
            hex_c = color[:7] if len(color) >= 7 else "#000000"
            alpha = int(color[7:9], 16) if len(color) == 9 else 255
            
            col1, col2, col3, col4 = st.columns([5, 1, 1, 1])
            with col1:
                new_hex = st.color_picker(tr(f"Color {i+1}"), value=hex_c, key=f"{key_prefix}_c_{item_id}")
                items[i]["color"] = new_hex
            
            with col2:
                st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
                st.button("🗑️", key=f"{key_prefix}_del_{item_id}", on_click=del_color_cb, args=(key_prefix, i))
            with col3:
                st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
                if i > 0:
                    st.button("⬆️", key=f"{key_prefix}_up_{item_id}", on_click=move_up_cb, args=(key_prefix, i))
            with col4:
                st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
                if i < len(items) - 1:
                    st.button("⬇️", key=f"{key_prefix}_down_{item_id}", on_click=move_down_cb, args=(key_prefix, i))
                    
        st.session_state[f"{key_prefix}_items"] = items
        return [item["color"] for item in items]

# --- UI INTERFACE ---
st.set_page_config(page_title="Hitster Card Generator", page_icon="🎵", layout="wide", initial_sidebar_state="expanded")

with st.sidebar:
    st.selectbox("Langue / Language", ["Français", "English"], key="interface_language")
    st.header(tr("⚙️ Settings"))
    st.caption(tr("Customize your print layout"))
    
    tabs = st.tabs([tr("Global"), tr("QR Side (Front)"), tr("Solution Side (Back)")])
    
    with tabs[0]:
        st.subheader(tr("📄 Print & Layout"))

        # Configurable square-card layout for A4 printing.
        card_size_cm = st.slider(
            "Card size (cm)", min_value=3.0, max_value=8.0,
            value=5.0, step=0.5, key="print_card_size_cm",
            help=tr("Square card size. The available rows and columns adapt to A4.")
        )
        card_spacing_cm = st.slider(
            "Space between cards (cm)", min_value=0.0, max_value=1.0,
            value=0.0, step=0.1, key="print_card_spacing_cm",
            help=tr("Adds the same gap horizontally and vertically between cards."),
            on_change=reset_generation
        )
        st.caption(tr("The spacing is visible in the generated PDF, not in the single-card preview."))
        max_cols = max(1, int((21.0 + card_spacing_cm) // (card_size_cm + card_spacing_cm)))
        max_rows = max(1, int((29.7 + card_spacing_cm) // (card_size_cm + card_spacing_cm)))
        st.session_state["print_cols"] = min(
            max(1, int(st.session_state.get("print_cols", 4))), max_cols
        )
        st.session_state["print_rows"] = min(
            max(1, int(st.session_state.get("print_rows", 5))), max_rows
        )
        cards_per_row = st.slider(
            "Columns per page", min_value=1, max_value=max_cols,
            key="print_cols"
        )
        cards_per_col = st.slider(
            "Rows per page", min_value=1, max_value=max_rows,
            key="print_rows"
        )
        st.caption(
            tr("{count} cards per page ({cols} columns × {rows} rows)").format(count=cards_per_row * cards_per_col, cols=cards_per_row, rows=cards_per_col)
        )
        ink_mode = st.toggle(tr("Ink Saving Mode"), value=st.session_state.get('ink_mode', False), 
                            help=tr("Use white background and black text to save ink."))
        border_mode = st.toggle(tr("Draw Cutting Borders"), value=st.session_state.get('border_mode', False),
                               help=tr("Draw a line around each card for easier cutting."))
        
        font_choice = st.selectbox(tr("Font Selection"), ["Montserrat", "Oswald", "Roboto", "Dancing Script", "Pacifico", "Custom..."])
        if font_choice == "Custom...":
            google_font = st.text_input(tr("Custom Google Font Name"), value=st.session_state.get('google_font', "Montserrat"),
                                        help=tr("Type any font name from Google Fonts."))
            st.markdown(tr("[🔍 Browse Google Fonts here](https://fonts.google.com/)"), unsafe_allow_html=True)
        else:
            google_font = font_choice
            
        st.divider()

        with st.expander(tr("🔑 Spotify API Credentials (optional)")):
            st.caption(tr("Only needed when pasting a playlist URL. Without credentials, playlist URLs are limited to ~100 tracks. Pasting individual track links works without limits."))
            spotify_client_id = st.text_input(tr("Client ID"), type="password")
            spotify_client_secret = st.text_input(tr("Client Secret"), type="password")
        

        st.session_state.ink_mode = ink_mode
        st.session_state.border_mode = border_mode
        st.session_state.google_font = google_font

    with tabs[1]:
        st.subheader(tr("🖼️ Background"))
        qr_bg_type = st.selectbox(tr("Background Type"), ["neon_rings", "solid", "image"], key="qr_bg_type", format_func=tr)
        qr_bg_color = st.color_picker(tr("Background Color"), value="#000000", key="qr_bg_color")
        
        if qr_bg_type == "image":
            qr_bg_upload = st.file_uploader(tr("Upload Image (QR Side)"), type=["png", "jpg", "jpeg"], key="qr_bg_up")
            if qr_bg_upload:
                st.session_state.qr_bg_img = Image.open(qr_bg_upload)
            else:
                st.session_state.qr_bg_img = None
            
            st.session_state.qr_bg_scale = st.slider(tr("Image Scale"), 0.1, 3.0, 1.0, 0.1, key="qr_scale")
            st.session_state.qr_bg_x = st.slider(tr("X Offset"), -1.0, 1.0, 0.0, 0.05, key="qr_x")
            st.session_state.qr_bg_y = st.slider(tr("Y Offset"), -1.0, 1.0, 0.0, 0.05, key="qr_y")
        
        if qr_bg_type == "neon_rings":
            st.session_state.neon_ring_thickness = st.slider(tr("Ring Thickness"), 1, 50, 12, key="neon_thick")
            st.session_state.neon_ring_count = st.slider(tr("Ring Count"), 1, 20, 8, key="neon_count")
            
            neon_hex_list = dynamic_color_list("neon", tr("Neon Ring Colors"), ["#FF0064", "#00C8FF", "#00FF78", "#FFFF00"])
            try:
                st.session_state.neon_colors = [tuple(int(val * 255) for val in utils.to_rgba(c)) for c in neon_hex_list]
            except:
                st.session_state.neon_colors = [(255, 0, 100), (0, 200, 255), (0, 255, 120), (255, 255, 0)]
                
        st.subheader(tr("📱 QR Settings"))
        qr_bg_mode = st.selectbox(tr("QR Background Mode"), ["solid", "transparent"], key="qr_bg_mode", format_func=tr)
        qr_module_color = st.color_picker(tr("QR Module Color"), value="#000000", key="qr_mod_c")
        if qr_bg_mode == "solid":
            st.session_state.qr_backplate_color = st.color_picker(tr("QR Backplate Color"), value="#FFFFFF", key="qr_bp_c")
            st.session_state.qr_padding = st.slider(tr("Backplate Padding"), 0, 200, 40, key="qr_pad")
            st.session_state.qr_radius = st.slider(tr("Backplate Corner Radius"), 0, 100, 20, key="qr_rad")
        st.session_state.qr_size_ratio = st.slider(tr("QR Size Ratio (%)"), 10, 80, 45, key="qr_size") / 100.0
        
        st.subheader(tr("🔤 Title"))
        st.session_state.qr_title_en = st.toggle(tr("Enable Title"), key="qr_t_en")
        if st.session_state.qr_title_en:
            st.session_state.qr_title = st.text_input(tr("Title Text"), value="HITSTER", key="qr_t_t")
            pos_options = ["top", "bottom", "top_left", "top_right", "bottom_left", "bottom_right", "center_above_qr", "center_below_qr"]
            st.session_state.qr_title_pos = st.selectbox(tr("Position"), pos_options, key="qr_t_p", format_func=tr)
            st.session_state.qr_title_size = st.slider(tr("Font Size"), 20, 200, 80, key="qr_t_s")
            st.session_state.qr_title_color = st.color_picker(tr("Title Color"), value="#FFFFFF", key="qr_t_c")
            st.session_state.qr_title_bg = st.toggle(tr("Draw Background Box"), key="qr_t_bg")

    with tabs[2]:
        st.subheader(tr("🎨 Color Gradient"))
        default_grad = DEFAULT_COLOR_GRADIENT
        st.session_state.color_gradient = dynamic_color_list(
            "gradient", 
            "Year Color Gradient", 
            default_grad, 
            help_text=tr("Colors map to the oldest to newest years.")
        )

        st.subheader(tr("🖼️ Background"))
        sol_bg_type = st.selectbox(tr("Background Type"), ["gradient", "image"], key="sol_bg_type", format_func=tr)
        if sol_bg_type == "image":
            sol_bg_upload = st.file_uploader(tr("Upload Image (Solution Side)"), type=["png", "jpg", "jpeg"], key="sol_bg_up")
            if sol_bg_upload:
                st.session_state.sol_bg_img = Image.open(sol_bg_upload)
            else:
                st.session_state.sol_bg_img = None
                
            st.session_state.sol_bg_scale = st.slider(tr("Image Scale"), 0.1, 3.0, 1.0, 0.1, key="sol_scale")
            st.session_state.sol_bg_x = st.slider(tr("X Offset"), -1.0, 1.0, 0.0, 0.05, key="sol_x")
            st.session_state.sol_bg_y = st.slider(tr("Y Offset"), -1.0, 1.0, 0.0, 0.05, key="sol_y")
        
        st.session_state.sol_border_width = st.slider(tr("Ink Saving Border Thickness"), 10, 500, 100, key="sol_bw")

        st.subheader(tr("🔤 Title"))
        st.session_state.sol_title_en = st.toggle(tr("Enable Title"), key="sol_t_en")
        if st.session_state.sol_title_en:
            st.session_state.sol_title = st.text_input(tr("Title Text"), value="HITSTER", key="sol_t_t")
            pos_options_sol = [
                "in_border_bottom_right", "in_border_bottom_left", "in_border_top_right", "in_border_top_left",
                "top", "bottom", "top_left", "top_right", "bottom_left", "bottom_right"
            ]
            st.session_state.sol_title_pos = st.selectbox(tr("Position"), pos_options_sol, key="sol_t_p", format_func=tr)
            st.session_state.sol_title_size = st.slider(tr("Font Size"), 20, 200, 80, key="sol_t_s")
            st.session_state.sol_title_color = st.color_picker(tr("Title Color"), value="#000000", key="sol_t_c")
            st.session_state.sol_title_bg = st.toggle(tr("Draw Background Box"), key="sol_t_bg")

    # Build this session's settings. Kept in st.session_state (per user) and
    # passed explicitly into utils functions, never written to a shared global.
    st.session_state.design_settings = {
        "card_size_cm": card_size_cm,
        "card_spacing_cm": card_spacing_cm,
        "cards_per_row": cards_per_row,
        "cards_per_col": cards_per_col,
        "ink_saving_mode": ink_mode,
        "card_draw_border": border_mode,
        "card_background_color": "#FFFFFF" if ink_mode else qr_bg_color,
        "google_font": google_font,
        "color_gradient": st.session_state.get('color_gradient', DEFAULT_COLOR_GRADIENT),

        "qr_bg_type": qr_bg_type,
        "qr_bg_color": qr_bg_color,
        "qr_bg_image": st.session_state.get('qr_bg_img'),
        "qr_bg_scale": st.session_state.get('qr_scale', 1.0),
        "qr_bg_offset_x": st.session_state.get('qr_x', 0.0),
        "qr_bg_offset_y": st.session_state.get('qr_y', 0.0),
        "neon_colors": st.session_state.get('neon_colors', utils.DEFAULT_DESIGN_SETTINGS['neon_colors']),
        "neon_ring_thickness": st.session_state.get('neon_thick', 12),
        "neon_ring_count": st.session_state.get('neon_count', 8),
        "qr_background_mode": qr_bg_mode,
        "qr_module_color": qr_module_color,
        "qr_background_color": st.session_state.get('qr_backplate_color', "#FFFFFF"),
        "qr_backplate_padding": st.session_state.get('qr_pad', 40),
        "qr_backplate_radius": st.session_state.get('qr_rad', 20),
        "qr_size_ratio": st.session_state.get('qr_size', 45) / 100.0 if 'qr_size' in st.session_state else 0.45,
        "qr_title_enabled": st.session_state.get('qr_t_en', False),
        "qr_title": st.session_state.get('qr_t_t', ""),
        "qr_title_pos": st.session_state.get('qr_t_p', "top"),
        "qr_title_size": st.session_state.get('qr_t_s', 80),
        "qr_title_color": st.session_state.get('qr_title_color', "#FFFFFF"),
        "qr_title_bg": st.session_state.get('qr_t_bg', False),
        
        "sol_bg_type": sol_bg_type,
        "sol_bg_image": st.session_state.get('sol_bg_img'),
        "sol_bg_scale": st.session_state.get('sol_scale', 1.0),
        "sol_bg_offset_x": st.session_state.get('sol_x', 0.0),
        "sol_bg_offset_y": st.session_state.get('sol_y', 0.0),
        "sol_border_width": st.session_state.get('sol_bw', 100),
        "sol_title_enabled": st.session_state.get('sol_t_en', False),
        "sol_title": st.session_state.get('sol_t_t', ""),
        "sol_title_pos": st.session_state.get('sol_t_p', "in_border_bottom_right"),
        "sol_title_size": st.session_state.get('sol_t_s', 80),
        "sol_title_color": st.session_state.get('sol_title_color', "#000000"),
        "sol_title_bg": st.session_state.get('sol_t_bg', False),
    }
with st.expander(tr("Disclaimer, Accuracy & Support")):
    st.info(tr("""
    **Why are some years wrong?**
    Metadata providers often list the date a song was added to a digital album (like a 'Greatest Hits' or 'Remaster') rather than the original single release date.
    You can now **manually correct years** in the table below after scraping!
    
    **📱 Mobile User Note:**
    If the download button doesn't respond on your phone, please try a desktop browser. Mobile browsers sometimes struggle with large in-memory PDF streams.
    """))

# --- MAIN PAGE ---
col1, col2 = st.columns([2, 1])
with col1:
    st.title("🎵 Hitster Card Generator")
    st.markdown(tr("Generate custom music game cards from any Spotify playlist or track links."))
with col2:
    pass

st.divider()

# Instructions and Preview Columns
info_col, preview_col = st.columns([1, 1])

with info_col:
    with st.expander(tr("How do I get links?"), expanded=True):
        st.write(tr("**Option A — Individual Tracks:**"))
        st.write(tr("1. Open **Spotify Desktop**."))
        st.write(tr("2. Go to your playlist."))
        st.write(tr("3. Select songs (**Ctrl+A**)."))
        st.write(tr("4. Copy (**Ctrl+C**)."))
        st.write(tr("5. Paste below!"))
        st.write("")
        st.write(tr("**Option B — Playlist URL:**"))
        st.write(tr("1. Right-click your playlist → **Share** → **Copy link**."))
        st.write(tr("2. Paste the playlist URL below!"))

with preview_col:
    st.info(tr("**Supported formats:**\n- Track links: `https://open.spotify.com/track/...`\n- Playlist links: `https://open.spotify.com/playlist/...`"))

# Input Area
st.subheader(tr("Input"))

btn_col1, btn_col2 = st.columns(2)
with btn_col1:
    st.button(tr("✨ Load Example Tracks"), on_click=set_example_links)
with btn_col2:
    st.button(tr("📋 Load Example Playlist"), on_click=set_example_playlist)

user_input = st.text_area(
    tr("Paste Spotify links here:"), 
    height=200, 
    key="user_input",
    placeholder="https://open.spotify.com/track/...\nor\nhttps://open.spotify.com/playlist/...",
    on_change=reset_generation,
)

# Detect input type
input_type, input_data = parse_input(user_input)

if input_type == 'playlist':
    st.success(tr("🎶 Spotify **playlist** URL detected!"))
elif input_type == 'tracks':
    st.success(tr("🎵 {count} Spotify **track link(s)** detected.").format(count=len(input_data)))
else:
    st.warning(tr("No valid Spotify links detected yet."))


# --- STEP 1: SCRAPE / FETCH METADATA ---
if st.button(tr("🔍 Fetch Song Metadata"), type="primary"):
    if input_type == 'empty':
        st.error(tr("Please paste some valid Spotify links first!"))
    else:
        with st.status(tr("Fetching metadata..."), expanded=True) as status:
            progress_bar = st.progress(0, text=tr("Starting..."))

            if input_type == 'playlist':
                playlist_url = input_data
                if spotify_client_id and spotify_client_secret:
                    st.write(tr("Using Spotify API to fetch playlist..."))
                    playlist_data = utils.fetch_spotify_playlist(
                        playlist_url, spotify_client_id, spotify_client_secret
                    )
                    songs = utils.parse_playlist_data(playlist_data)
                    progress_bar.progress(1.0, text=tr("Done!"))
                else:
                    st.write(tr("Scraping playlist page for track links (no API key)..."))
                    track_links = utils.scrape_playlist_track_links(playlist_url)
                    if not track_links:
                        st.error(tr("Could not extract tracks from the playlist page. Try adding Spotify API credentials in the sidebar, or paste individual track links instead."))
                        st.stop()
                    st.write(tr("Found {count} tracks. Scraping metadata...").format(count=len(track_links)))
                    songs = utils.fetch_no_api_data_from_list(track_links, progress_bar)
            else:
                st.write(tr("Scraping track metadata..."))
                songs = utils.fetch_no_api_data_from_list(input_data, progress_bar)

            status.update(label=tr("✅ Fetched {count} songs!").format(count=len(songs)), state="complete")
            progress_bar.empty()

        st.session_state.songs = songs
        st.session_state.pdf_data = None  # reset PDF when songs change

# --- REVIEW AND GENERATE ---
# --- STEP 2: REVIEW & EDIT SONGS TABLE ---
songs = st.session_state.songs
if songs:
    st.divider()
    st.subheader(tr("📝 Review & Edit Songs"))
    st.caption(tr("Fix any incorrect years before generating cards. "
               "Songs with unknown years show as empty — fill them in!")

    # Build an editable dataframe
    import pandas as pd
    df = pd.DataFrame([
        {
            "Artist": s['artist'],
            "Song": s['name'],
            "Year": s['year'] if s['year'] is not None else None,
            "Source": s.get('year_source', ''),
            "Link": s['link'],
        }
        for s in songs
    ])

    edited_df = st.data_editor(
        df,
        column_config={
            "Artist": st.column_config.TextColumn(tr("Artist"), disabled=False),
            "Song": st.column_config.TextColumn(tr("Song"), disabled=False),
            "Year": st.column_config.NumberColumn(tr("Year"), min_value=1900, max_value=2030, step=1,
                                                   help=tr("Edit this to fix incorrect years!")),
            "Source": st.column_config.TextColumn(tr("Source"), disabled=True, 
                                                   help=tr("Where the year came from")),
            "Link": st.column_config.TextColumn(tr("Link"), disabled=False),
        },
        width="stretch",
        num_rows="fixed",
        hide_index=True,
    )

    # Count problems
    unknown_count = edited_df['Year'].isna().sum()
    if unknown_count > 0:
        st.warning(tr("⚠️ {count} song(s) have no year. Please fill them in above, or they will show as '????' on the cards.").format(count=unknown_count))

    # --- CARD PREVIEW ---
    st.divider()
    st.subheader(tr("👀 Card Preview"))
    
    # Pick a sample song for preview
    preview_idx = st.selectbox(
        "Preview card for:", 
        range(len(edited_df)),
        format_func=lambda i: f"{edited_df.iloc[i]['Artist']} — {edited_df.iloc[i]['Song']}",
    )
    
    preview_song = edited_df.iloc[preview_idx]
    preview_year = int(preview_song['Year']) if pd.notna(preview_song['Year']) else None
    all_preview_years = [int(y) if pd.notna(y) else None for y in edited_df['Year']]
    valid_preview_years = [y for y in all_preview_years if y is not None]
    if not valid_preview_years:
        valid_preview_years = [2000]

    settings = st.session_state.get('design_settings')

    pcol1, pcol2 = st.columns(2)
    with pcol1:
        st.caption(tr("QR Side"))
        link_str = str(preview_song['Link']) if pd.notna(preview_song['Link']) else "https://open.spotify.com/"
        qr_img = utils.create_qr_code(link_str)
        qr_card = utils.create_qr_with_neon_rings_in_memory(qr_img, seed=hash(link_str), settings_override=settings)
        st.image(qr_card, width="stretch")
    with pcol2:
        st.caption(tr("Solution Side"))
        sol_card = utils.create_solution_side_in_memory(
            str(preview_song['Song']), str(preview_song['Artist']),
            preview_year, valid_preview_years, settings_override=settings
        )
        st.image(sol_card, width="stretch")

    # --- STEP 3: GENERATE PDF ---
    st.divider()
    
    if st.button(tr("🎴 Create My PDF"), type="primary"):
        # Apply edited years back to songs
        for i, song in enumerate(songs):
            new_artist = edited_df.iloc[i]['Artist']
            new_song_name = edited_df.iloc[i]['Song']
            new_year = edited_df.iloc[i]['Year']
            new_link = edited_df.iloc[i]['Link']
            
            if pd.notna(new_artist):
                song['artist'] = str(new_artist)
            if pd.notna(new_song_name):
                song['name'] = str(new_song_name)
            if pd.notna(new_link):
                song['link'] = str(new_link)

            if pd.notna(new_year):
                song['year'] = int(new_year)
                if int(new_year) != (songs[i].get('year') or 0):
                    song['year_source'] = 'Manual'
            else:
                song['year'] = None

        with st.status(tr("Generating cards..."), expanded=True) as status:
            progress_bar = st.progress(0, text=tr("Starting PDF generation..."))
            pdf_data = utils.create_pdf_in_memory(songs, progress_bar, settings_override=st.session_state.get('design_settings'))
            status.update(label=tr("✅ All Cards Generated!"), state="complete")
            progress_bar.empty()

        st.session_state.pdf_data = pdf_data
        st.balloons()

    # Show download button if PDF exists
    if st.session_state.pdf_data:
        st.download_button(
            label=tr("💾 Download Printable PDF"),
            data=st.session_state.pdf_data,
            file_name="my_hitster_cards.pdf",
            mime="application/pdf",
            width="stretch"
        )