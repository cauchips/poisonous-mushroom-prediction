import streamlit as st
import joblib
import numpy as np

# Memuat model yang telah disimpan
model = joblib.load('model.pkl')

# Judul aplikasi
st.title('Mushroom Prediction')

# Membuat form input untuk fitur-fitur yang dibutuhkan model
st.subheader('Input Mushroom\'s Features:')

# Mengatur layout ke dalam 2 kolom
col1, col2 = st.columns(2)

with col1:
    cap_shape = st.selectbox('Cap Shape', ['bell (b)', 'conical (c)', 'convex (x)', 'flat (f)', 'knobbed (k)', 'sunken (s)'])
    cap_surface = st.selectbox('Cap Surface', ['fibrous (f)', 'grooves (g)', 'scaly (y)', 'smooth (s)'])
    cap_color = st.selectbox('Cap Color', ['brown (n)', 'buff (b)', 'cinnamon (c)', 'gray (g)', 'green (r)', 'pink (p)', 'purple (u)', 'red (e)', 'white (w)', 'yellow (y)'])
    bruises = st.radio('Bruises', ['Yes (bruises)', 'No (no)'])
    odor = st.selectbox('Odor', ['almond (a)', 'anise (l)', 'creosote (c)', 'fishy (y)', 'foul (f)', 'musty (m)', 'none (n)', 'pungent (p)', 'spicy (s)'])
    gill_attachment = st.selectbox('Gill Attachment', ['attached (a)', 'descending (d)', 'free (f)', 'notched (n)'])
    gill_spacing = st.selectbox('Gill Spacing', ['close (c)', 'crowded (w)', 'distant (d)'])
    gill_size = st.radio('Gill Size', ['broad (b)', 'narrow (n)'])
    veil_color = st.selectbox('Veil Color', ['brown (n)', 'orange (o)', 'white (w)', 'yellow (y)'])
    gill_color = st.selectbox('Gill Color', ['black (k)', 'brown (n)', 'buff (b)', 'chocolate (h)', 'gray (g)', 'green (r)', 'orange (o)', 'pink (p)', 'purple (u)', 'red (e)', 'white (w)', 'yellow (y)'])

with col2:
    ring_number = st.radio('Ring Number', ['none (n)', 'one (o)', 'two (t)'])
    ring_type = st.selectbox('Ring Type', ['cobwebby (c)', 'evanescent (e)', 'flaring (f)', 'large (l)', 'none (n)', 'pendant (p)', 'sheathing (s)', 'zone (z)'])
    stalk_shape = st.selectbox('Stalk Shape', ['enlarging (e)', 'tapering (t)'])
    stalk_root = st.selectbox('Stalk Root', ['bulbous (b)', 'club (c)', 'cup (u)', 'equal (e)', 'rhizomorphs (z)', 'rooted (r)', 'missing (?)'])
    stalk_surface_above_ring = st.selectbox('Stalk Surface Above Ring', ['fibrous (f)', 'scaly (y)', 'silky (k)', 'smooth (s)'])
    stalk_surface_below_ring = st.selectbox('Stalk Surface Below Ring', ['fibrous (f)', 'scaly (y)', 'silky (k)', 'smooth (s)'])
    stalk_color_above_ring = st.selectbox('Stalk Color Above Ring', ['brown (n)', 'buff (b)', 'cinnamon (c)', 'gray (g)', 'orange (o)', 'pink (p)', 'red (e)', 'white (w)', 'yellow (y)'])
    stalk_color_below_ring = st.selectbox('Stalk Color Below Ring', ['brown (n)', 'buff (b)', 'cinnamon (c)', 'gray (g)', 'orange (o)', 'pink (p)', 'red (e)', 'white (w)', 'yellow (y)'])
    spore_print_color = st.selectbox('Spore Print Color', ['black (k)', 'brown (n)', 'buff (b)', 'chocolate (h)', 'green (r)', 'orange (o)', 'purple (u)', 'white (w)', 'yellow (y)'])
    population = st.selectbox('Population', ['abundant (a)', 'clustered (c)', 'numerous (n)', 'scattered (s)', 'several (v)', 'solitary (y)'])

habitat = st.selectbox('Habitat', ['grasses (g)', 'leaves (l)', 'meadows (m)', 'paths (p)', 'urban (u)', 'waste (w)', 'woods (d)'])

# Mapping pilihan ke nilai label-encoded
mapping = {
    'cap_shape': {'bell (b)': 0, 'conical (c)': 1, 'convex (x)': 2, 'flat (f)': 3, 'knobbed (k)': 4, 'sunken (s)': 5},
    'cap_surface': {'fibrous (f)': 0, 'grooves (g)': 1, 'scaly (y)': 2, 'smooth (s)': 3},
    'cap_color': {'brown (n)': 0, 'buff (b)': 1, 'cinnamon (c)': 2, 'gray (g)': 3, 'green (r)': 4, 'pink (p)': 5, 'purple (u)': 6, 'red (e)': 7, 'white (w)': 8, 'yellow (y)': 9},
    'bruises': {'Yes (bruises)': 1, 'No (no)': 0},
    'odor': {'almond (a)': 0, 'anise (l)': 1, 'creosote (c)': 2, 'fishy (y)': 3, 'foul (f)': 4, 'musty (m)': 5, 'none (n)': 6, 'pungent (p)': 7, 'spicy (s)': 8},
    'gill_attachment': {'attached (a)': 0, 'descending (d)': 1, 'free (f)': 2, 'notched (n)': 3},
    'gill_spacing': {'close (c)': 0, 'crowded (w)': 1, 'distant (d)': 2},
    'gill_size': {'broad (b)': 0, 'narrow (n)': 1},
    'gill_color': {'black (k)': 0, 'brown (n)': 1, 'buff (b)': 2, 'chocolate (h)': 3, 'gray (g)': 4, 'green (r)': 5, 'orange (o)': 6, 'pink (p)': 7, 'purple (u)': 8, 'red (e)': 9, 'white (w)': 10, 'yellow (y)': 11},
    'stalk_shape': {'enlarging (e)': 0, 'tapering (t)': 1},
    'stalk_root': {'bulbous (b)': 0, 'club (c)': 1, 'cup (u)': 2, 'equal (e)': 3, 'rhizomorphs (z)': 4, 'rooted (r)': 5, 'missing (?)': 6},
    'stalk_surface_above_ring': {'fibrous (f)': 0, 'scaly (y)': 1, 'silky (k)': 2, 'smooth (s)': 3},
    'stalk_surface_below_ring': {'fibrous (f)': 0, 'scaly (y)': 1, 'silky (k)': 2, 'smooth (s)': 3},
    'stalk_color_above_ring': {'brown (n)': 0, 'buff (b)': 1, 'cinnamon (c)': 2, 'gray (g)': 3, 'orange (o)': 4, 'pink (p)': 5, 'red (e)': 6, 'white (w)': 7, 'yellow (y)': 8},
    'stalk_color_below_ring': {'brown (n)': 0, 'buff (b)': 1, 'cinnamon (c)': 2, 'gray (g)': 3, 'orange (o)': 4, 'pink (p)': 5, 'red (e)': 6, 'white (w)': 7, 'yellow (y)': 8},
    'veil_color': {'brown (n)': 0, 'orange (o)': 1, 'white (w)': 2, 'yellow (y)': 3},
    'ring_number': {'none (n)': 0, 'one (o)': 1, 'two (t)': 2},
    'ring_type': {'cobwebby (c)': 0, 'evanescent (e)': 1, 'flaring (f)': 2, 'large (l)': 3, 'none (n)': 4, 'pendant (p)': 5, 'sheathing (s)': 6, 'zone (z)': 7},
    'spore_print_color': {'black (k)': 0, 'brown (n)': 1, 'buff (b)': 2, 'chocolate (h)': 3, 'green (r)': 4, 'orange (o)': 5, 'purple (u)': 6, 'white (w)': 7, 'yellow (y)': 8},
    'population': {'abundant (a)': 0, 'clustered (c)': 1, 'numerous (n)': 2, 'scattered (s)': 3, 'several (v)': 4, 'solitary (y)': 5},
    'habitat': {'grasses (g)': 0, 'leaves (l)': 1, 'meadows (m)': 2, 'paths (p)': 3, 'urban (u)': 4, 'waste (w)': 5, 'woods (d)': 6}
}

# Konversi input pengguna ke nilai label-encoded
user_input = np.array([[mapping['cap_shape'][cap_shape],
                        mapping['cap_surface'][cap_surface],
                        mapping['cap_color'][cap_color],
                        mapping['bruises'][bruises],
                        mapping['odor'][odor],
                        mapping['gill_attachment'][gill_attachment],
                        mapping['gill_spacing'][gill_spacing],
                        mapping['gill_size'][gill_size],
                        mapping['gill_color'][gill_color],
                        mapping['stalk_shape'][stalk_shape],
                        mapping['stalk_root'][stalk_root],
                        mapping['stalk_surface_above_ring'][stalk_surface_above_ring],
                        mapping['stalk_surface_below_ring'][stalk_surface_below_ring],
                        mapping['stalk_color_above_ring'][stalk_color_above_ring],
                        mapping['stalk_color_below_ring'][stalk_color_below_ring],
                        mapping['veil_color'][veil_color],
                        mapping['ring_number'][ring_number],
                        mapping['ring_type'][ring_type],
                        mapping['spore_print_color'][spore_print_color],
                        mapping['population'][population],
                        mapping['habitat'][habitat]]])

# Menjalankan prediksi saat tombol ditekan
if st.button('Prediction'):
    prediction = model.predict(user_input)
    st.write(f'Prediction Result: {"Poisonous" if prediction[0] == 1 else "Edible"}')
