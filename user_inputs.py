import streamlit as st
import numpy as np


def inputs():
    st.sidebar.subheader('Give Details')


    cap_shape = st.sidebar.text_input("Cap Shape? (bell=b, conical=c, convex=x, flat=f, knobbed=k, sunken=s)")
    cap_shape = {'b':0,'c':1,'f':2,'k':3,'s':4,'x':5}.get(cap_shape)


    cap_surface = st.sidebar.text_input('Cap Surface? (fibrous=f, grooves=g, scaly=y, smooth=s)')
    cap_surface = {'f':0,'g':1,'s':2,'y':3}.get(cap_surface)


    cap_color = st.sidebar.text_input('Cap Color? (brown=n, buff=b, cinnamon=c, gray=g, green=r, pink=p, purple=u, red=e, white=w, yellow=y)')
    cap_color = {'b':0,'c':1,'e':2,'g':3,'n':4,'p':5,'r':6,'u':7,'w':8,'y':9}.get(cap_color)


    bruises = st.sidebar.text_input('Bruises? (bruises=t, no=f)')
    bruises = {'f':0,'t':1}.get(bruises)


    odor = st.sidebar.text_input('Odor? (almond=a, anise=l, creosote=c, fishy=y, foul=f, musty=m, none=n, pungent=p, spicy=s)')
    odor = {'a':0,'c':1,'f':2,'l':3,'m':4,'n':5,'p':6,'s':7,'y':8}.get(odor)


    gill_attachment = st.sidebar.text_input('Gill Attachment? (attached=a, descending=d, free=f, notched=n)')
    gill_attachment = {'a':0,'d':1,'f':2,'n':3}.get(gill_attachment)


    gill_spacing = st.sidebar.text_input('Gill Spacing? (close=c, crowded=w, distant=d)')
    gill_spacing = {'c':0,'d':1,'w':2}.get(gill_spacing)


    gill_size = st.sidebar.text_input('Gill Size (broad=b, narrow=n)')
    gill_size = {'b':0,'n':1}.get(gill_size)


    gill_color = st.sidebar.text_input('Gill Color? (black=k, brown=n, buff=b, chocolate=h, gray=g, green=r, orange=o, pink=p, purple=u, red=e, white=w, yellow=y)')
    gill_color = {'b':0,'e':1,'g':2,'h':3,'k':4,'o':5,'p':6,'r':7,'n':8,'u':9,'w':10,'y':11}.get(gill_color)


    stalk_shape = st.sidebar.text_input('Stalk Shape? (enlarging=e, tapering=t)')
    stalk_shape = {'e':0,'t':1}.get(stalk_shape)


    stalk_root = st.sidebar.text_input('Stalk Root? (bulbous=b, club=c, cup=u, equal=e, rhizomorphs=z, rooted=r, missing=?)')
    stalk_root = {'?':0,'b':1,'c':2,'e':3,'r':4,'u':5,'z':6}.get(stalk_root)


    stalk_surface_above_ring = st.sidebar.text_input('Stalk Surface Above Ring? (fibrous=f, scaly=y, silky=k, smooth=s)')
    stalk_surface_above_ring = {'f':0,'k':1,'s':2,'y':3}.get(stalk_surface_above_ring)


    stalk_surface_below_ring = st.sidebar.text_input('Stalk Surface Below Ring? (fibrous=f, scaly=y, silky=k, smooth=s)')
    stalk_surface_below_ring = {'f':0,'k':1,'s':2,'y':3}.get(stalk_surface_below_ring)


    stalk_color_above_ring = st.sidebar.text_input('Stalk Color Above Ring? (brown=n, buff=b, cinnamon=c, gray=g, orange=o, pink=p, red=e, white=w, yellow=y)')
    stalk_color_above_ring = {'b':0,'c':1,'e':2,'g':3,'n':4,'o':5,'p':6,'w':7,'y':8}.get(stalk_color_above_ring)


    stalk_color_below_ring = st.sidebar.text_input('Stalk Color Below Ring? (brown=n, buff=b, cinnamon=c, gray=g, orange=o, pink=p, red=e, white=w, yellow=y)')
    stalk_color_below_ring = {'b':0,'c':1,'e':2,'g':3,'n':4,'o':5,'p':6,'w':7,'y':8}.get(stalk_color_below_ring)


    veil_type = st.sidebar.text_input('Veil Type? (partial=p, universal=u)')
    veil_type = {'p':0,'u':1}.get(veil_type)


    veil_color = st.sidebar.text_input('Veil Color? (brown=n, orange=o, white=w, yellow=y)')
    veil_color = {'n':0,'o':1,'w':2,'y':3}.get(veil_color)


    ring_number = st.sidebar.text_input('Ring Number? (none=n, one=o, two=t)')
    ring_number = {'n':0,'o':1,'t':2}.get(ring_number)



    ring_type = st.sidebar.text_input('Ring Type? (cobwebby=c, evanescent=e, flaring=f, large=l, none=n, pendant=p, sheathing=s, zone=z)')
    ring_type = {'c':0,'e':1,'f':2,'l':3,'n':4,'p':5,'s':6,'z':7}.get(ring_type)


    spore_print_color = st.sidebar.text_input('Spore Print Color? (black=k, brown=n, buff=b, chocolate=h, green=r, orange=o, purple=u, white=w, yellow=y)')
    spore_print_color = {'b':0,'h':1,'k':2,'n':3,'o':4,'r':5,'u':6,'w':7,'y':8}.get(spore_print_color)


    population = st.sidebar.text_input('Population? (abundant=a, clustered=c, numerous=n, scattered=s, several=v, solitary=y)')
    population = {'a':0,'c':1,'n':2,'s':3,'v':4,'y':5}.get(population)


    habitat = st.sidebar.text_input('Habitat? (grasses=g, leaves=l, meadows=m, paths=p, urban=u, waste=w, woods=d)')
    habitat = {'d':0,'g':1,'l':2,'m':3,'p':4,'u':5,'w':6}.get(habitat)



    X_list = np.array([cap_shape, cap_surface, cap_color, bruises, odor , gill_attachment, gill_spacing, gill_size, gill_color, stalk_shape, stalk_root, stalk_surface_above_ring, stalk_surface_below_ring, stalk_color_above_ring, stalk_color_below_ring, veil_type, veil_color, ring_number, ring_type, spore_print_color, population, habitat])

    return np.reshape(X_list, (1, -1))
    
