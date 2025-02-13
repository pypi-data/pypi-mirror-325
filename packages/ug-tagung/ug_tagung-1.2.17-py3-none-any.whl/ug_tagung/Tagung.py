"""Tagung.py - Tagung Adressverwaltung GUI

"""

import logging
from ugbib_werkzeug.bibWerkzeug import log_init
log_init('Tagung')
logger = logging.getLogger()

import os, sys
sys.path.append('/home/ulrich/PythonHobby/bibs/bibtkinter/src/ugbib_tkinter/')

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import tkinter.font as tkFont
import tkinter.messagebox as dialog
import tkinter.filedialog as filedialog

from ugbib_divers.bibGlobal import glb
from ugbib_tkinter.bibForm import (
        ButtonWithEnter,
        TkIcons,
        Validator,
        Form, FormListe, BasisFormListe,
        NaviForm, NaviWidget, NaviListe,
        Notify, notify,
        Tooltip,
        BearbVonAm,
        DialogLogin, DialogGemeindeAuswahl,
        DialogHilfeNaviButtons,
        yScrolledFrame,
        FormListeUnterformular,
        FrameScrolledListbox, FrameScrolledListboxValueLabel,
        ComboboxValueLabel,
        )

from ugbib_modell.bibModell import setSearchPath

from .Tagung_Def import *
from .Tagung_Modelle import (
    Person, PersonJugend, PersonStatus, PersonFinanzen, PersonFinanzenListe,
    Veranstaltung,
    DozentListe, RaumbelegungListe,
    Gruppe, GruppeListe, Farbe, Laender, Mailart, Raumart, Veranstaltungart,
    PersonGruppeListe,
    Tagung, Status, StatusListe, Mail,
    AnmWSListe, PersonWSAnmListe, PersonWSListe,
    Jobs, JobsListe
    )
for M in [
        Person, PersonJugend, PersonStatus, PersonFinanzen, PersonFinanzenListe,
        Veranstaltung,
        DozentListe, RaumbelegungListe,
        Gruppe, GruppeListe, Farbe, Laender, Mailart, Raumart, Veranstaltungart,
        PersonGruppeListe,
        Tagung, Status, StatusListe, Mail,
        AnmWSListe, PersonWSAnmListe, PersonWSListe,
        Jobs, JobsListe
        ]:
    M.Init(M)

class Hauptprogramm(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.style = ttk.Style()
        glb.icons = TkIcons()
        self.baueMenuBar()
        self.basics()
        self.baueLayout()
        self.baueValidatoren()
        self.baueWidgets()
        self.nbkMain.config(takefocus=False)
        self.disableMainNotebook()
        self.activateLogin()
    
    def basics(self):
        self.title('Tagung Adressverwaltung')
        self.bind_all('<Control-q>', self.handleQuit)
        self.style.theme_use('classic')    # Nur damit wird PanedWindows Trenner sichtbar
        #
        # Schriftgröße
        tkFont.nametofont('TkDefaultFont').configure(size=8)
        tkFont.nametofont('TkTextFont').configure(size=8)
        tkFont.nametofont('TkMenuFont').configure(size=8)
        tkFont.nametofont('TkFixedFont').configure(size=8)
        
        
    def handleQuit(self, event):
        """handleQuit - Beendet das Programm nach HotKey
        
            Ruft einfach nur ende auf.
        """
        self.ende()
    
    def ende(self):
        self.logout(tolerant=True)
        self.quit()
    
    def handleLogin(self):
        glb.PSQL_USER = self.varGlbUser.get()
        glb.PSQL_PASSWORD = self.varGlbPassword.get()
        if checkLogin():
            tagungAuswahl = [T['schema'] for T in glb.tagungen]
            self.activateTagung()
            self.cmbGlbTagung['values'] = tagungAuswahl
            notify(f'Erfolgreich angemeldet als: {glb.PSQL_USER}', 'Erfolg')
            notify('Bitte Tagung auswählen', 'Hinweis')
            self.cmbGlbTagung.event_generate('<Down>')
        else:
            self.activateLogin()
    
    def handleLogout(self):
        self.disableMainNotebook()
        self.activateLogin()
        self.logout()
    
    def handleTagungAusgewaehlt(self, event):
        glb.setvalue('schema', self.varGlbTagung.get())
        for T in glb.tagungen:
            if T['schema'] == glb.schema:
                glb.setvalue('aktuelleTagung', T)
                break
        logger.debug(f'{glb.aktuelleTagung["schema"]}, public')
        if not setSearchPath(f'{glb.aktuelleTagung["schema"]}, public'):
            sys.exit(f'Auswahl der Tagung fehlgeschlagen. Einzelheiten s. Tagung.log.')
        notify('Tagung erfolgreich ausgewählt.', 'Erfolg')
        Form.resetForms()
        self.enableMainNotebook()
    
    def activateLogin(self):
        """activateLogin - Hält den User auf den Login-Feldern
        
            Aktiviert die Login-Widgets und deaktiviert die Gemeinde-Auswahl
        """
        self.entGlbUser['state'] = tk.NORMAL
        self.entGlbUser.focus()
        self.entGlbPassword['state'] = tk.NORMAL
        self.btnGlbLogin.configure(state=tk.NORMAL)
        self.entGlbUser.focus()
        
        self.btnGlbLogout.configure(state=tk.DISABLED)
    
    def activateTagung(self):
        """activateTagung - Hält den User auf der Tagungs-Auswahl
        
            Aktiviert die Tagungs-Auswahl und deaktiviert die Login-Widgets
        """
        self.btnGlbLogout.configure(state=tk.NORMAL)
        self.cmbGlbTagung.focus()
        
        self.entGlbUser.configure(state=tk.DISABLED)
        self.entGlbPassword.config(state=tk.DISABLED)
        self.btnGlbLogin.config(state=tk.DISABLED)

    def baueMenuBar(self):
        #
        # Menu Bar anlegen und zeigen
        top = self.winfo_toplevel()
        self.mnuBar = tk.Menu(top)
        top['menu'] = self.mnuBar
        #
        # Menüs anlegen
        self.mnuDatei = tk.Menu(self.mnuBar, tearoff=0)
        self.mnuDB = tk.Menu(self.mnuDatei, tearoff=0)
        self.mnuHilfe = tk.Menu(self.mnuBar, tearoff=0)
        #
        # Menüs füllen
        #
        # Menü Bar füllen
        self.mnuBar.add_cascade(label='Datei', menu=self.mnuDatei)
        self.mnuBar.add_cascade(label='Hilfe', menu=self.mnuHilfe)
        # Menü Datei füllen
        self.mnuDatei.add_cascade(
            label='Datenbank',
            image=glb.icons.getIcon('database'),
            menu=self.mnuDB)
        self.mnuDatei.add_separator()
        self.mnuDatei.add_command(
            label='Beenden',
            accelerator='Strg-Q',
            image=glb.icons.getIcon('quit'),
            command=lambda : self.ende())
        # Menü DB (Datenbank) füllen
        # Menü Hilfe füllen
        self.mnuHilfe.add_command(
            label='Navi Buttons',
            command=lambda: DialogHilfeNaviButtons(self)
            )
    
    
    def logout(self, tolerant=False):
        """handleMnuLogout - Behandelt Menü Logout Button
        """
        # Falls DB Connector existiert, versuche zu schließen
        try:
            glb.DB.close()
            notify('Verbindung zur DB geschlossen', 'Erfolg')
            logging.info(f'Verbindung zur DB geschlossen.')
            glb.PSQL_PASSWORD = ''
        except Exception as e:
            if not tolerant:
                notify(e, 'Fehler')
                logging.info(f'Fehler beim Logout: {e}')
        # Koptzeile leeren
        self.varGlbDB.set('')
        self.varGlbUser.set('')
        self.varGlbPassword.set('')
        self.varGlbTagung.set('')
        glb.PSQL_PASSWORD = ''
        glb.PSQL_USER = ''
    
    def baueValidatoren(self):
      
        def invalidHoldFocus(widgetName):
            widget = self.nametowidget(widgetName)
            widget.focus_force()
            notify('Wert ungültig', 'Warnung')
        #
        # Validatoren
        self.valDate = self.register(Validator.valDate)
        self.valTime = self.register(Validator.valTime)
        self.valInt = self.register(Validator.valInt)
        #
        # Funktionen für invalidcommand
        self.invalidHoldFocus = self.register(invalidHoldFocus)
    
    def baueWidgets(self):
        #
        # Kopfzeile (Top) - Information über DB-Verbindung
        #
        # Variablen
        self.varGlbDB = tk.StringVar()
        self.varGlbUser = tk.StringVar()
        self.varGlbPassword = tk.StringVar()
        self.varGlbTagung = tk.StringVar()
        
        self.varGlbDB.set(glb.PSQL_DATABASE)
        self.varGlbUser.set(glb.PSQL_USER)
        self.varGlbPassword.set(glb.PSQL_PASSWORD)
        #
        # User, Password, Tagung, Datenbank
        self.lblGlbUser = ttk.Label(self.frmTop, text='Benutzer:')
        self.lblGlbUser.pack(side=tk.LEFT)
        self.entGlbUser = ttk.Entry(
            self.frmTop,
            textvariable=self.varGlbUser)
        Tooltip(self.entGlbUser, 'Username PostgreSQL Datenbank')
        self.entGlbUser.pack(side=tk.LEFT)
        
        self.lblGlbPassword = ttk.Label(self.frmTop, text='Passwort:')
        self.lblGlbPassword.pack(side=tk.LEFT)
        self.entGlbPassword = ttk.Entry(
            self.frmTop,
            textvariable=self.varGlbPassword,
            show='*'
            )
        Tooltip(self.entGlbPassword, 'Passwort PostgreSQL Datenbank')
        self.entGlbPassword.pack(side=tk.LEFT)
        
        self.btnGlbLogin = ButtonWithEnter(
            self.frmTop,
            text='Login',
            image=glb.icons.getIcon('connect'),
            compound=tk.LEFT,
            command=self.handleLogin
            )
        self.btnGlbLogin.pack(side=tk.LEFT)
        
        self.btnGlbLogout = ButtonWithEnter(
            self.frmTop,
            text='Logout',
            image=glb.icons.getIcon('disconnect'),
            compound=tk.LEFT,
            command=self.handleLogout
            )
        self.btnGlbLogout.pack(side=tk.LEFT)
        
        self.lblGlbTagung = ttk.Label(self.frmTop, text='Tagung:')
        self.lblGlbTagung.pack(side=tk.LEFT)
        self.cmbGlbTagung = ttk.Combobox(
            self.frmTop,
            textvariable=self.varGlbTagung,
            state='readonly',
            exportselection=0)
        self.cmbGlbTagung.bind('<<ComboboxSelected>>', self.handleTagungAusgewaehlt)
        self.cmbGlbTagung.pack(side=tk.LEFT)
        
        self.lblGlbDB = ttk.Label(self.frmTop, text='Datenbank:')
        self.lblGlbDB.pack(side=tk.LEFT)
        self.entGlbDB = ttk.Entry(
            self.frmTop,
            textvariable=self.varGlbDB,
            state=tk.DISABLED)
        self.entGlbDB.pack(side=tk.LEFT)
        #
        # Notify Widget in Fußbereich
        self.wdgNotify = Notify(self.frmBottom)
        self.wdgNotify.pack(expand=tk.YES, fill=tk.BOTH)
        for art in Notify.arten:
            notify(f'Test: {art=}', art)
        ttk.Label(self.frmBottom, text='Platzhalter Bottom').pack()
        #
        # Personen Jugend Einzelheiten
        with Form() as form:
            glb.formPersJuEinzel = form
            #
            # Frames für Navi, Formular und Unterformulare
            self.frmPersJuEinzelNavi = ttk.Frame(self.frmPersJuEinzel)
            self.frmPersJuEinzelDaten = ttk.Frame(self.frmPersJuEinzel)
            self.frmPersJuEinzelUnterformulare = ttk.Frame(self.frmPersJuEinzel)
            
            self.frmPersJuEinzelNavi.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            ttk.Separator(self.frmPersJuEinzel, orient=tk.VERTICAL).pack(
                side=tk.LEFT,
                fill=tk.BOTH,
                expand=True)
            self.frmPersJuEinzelDaten.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            ttk.Separator(self.frmPersJuEinzel, orient=tk.VERTICAL).pack(
                side=tk.LEFT,
                fill=tk.BOTH,
                expand=True)
            self.frmPersJuEinzelUnterformulare.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            
            self.sfrPersJuEinzelGruppen = yScrolledFrame(self.frmPersJuEinzelUnterformulare)
            self.frmPersJuEinzelGruppen = self.sfrPersJuEinzelGruppen.innerFrame
            ttk.Label(self.frmPersJuEinzelUnterformulare, text='Gruppen').pack(
                  side=tk.TOP,
                  anchor=tk.W)
            self.sfrPersJuEinzelGruppen.pack(side=tk.TOP, fill=tk.BOTH)
            
            #
            # Navi herstellen und einsetzen
            navi = NaviForm(self.frmPersJuEinzelNavi)
            form.setNavi(navi)
            navi.pack(fill=tk.BOTH, expand=True)
            #
            # Navi konfigurieren
            navi.connectToModell(
                PersonJugend,
                selects=('g_ansprechpartner_id', 'status'),
                keyFeldNavi='id',
                labelFelder=('name', 'vorname', 'id',),
                filterFelder=('name', 'vorname', 'strasse', 'ort',),
                Sort='name, vorname')
            #
            # Unterformulare herstellen und an Navi hängen
            #
            # ... für Gruppen
            def FactoryFormPersJuEinzelGruppe():
                uform = Form()
                #
                # Navi herstellen und einsetzen
                unavi = NaviForm(self.frmPersJuEinzelGruppen, elemente=('save', 'delete'))
                uform.setNavi(unavi)
                #
                # Navi konfigurieren
                unavi.connectToModell(
                    PersonGruppeListe,
                    selects=('gruppe_kurz_bez',))
                #
                # Widgets
                uform.addWidget(
                    'id',
                    ttk.Entry(self.frmPersJuEinzelGruppen, state=tk.DISABLED, width=6),
                    'int',
                    label='ID')
                uform.addWidget(
                    'person_id',
                    ttk.Entry(self.frmPersJuEinzelGruppen, state=tk.DISABLED, width=6),
                    'int',
                    label='P-ID')
                uform.addWidget(
                    'gruppe_kurz_bez',
                    ttk.Combobox(self.frmPersJuEinzelGruppen, width=10),
                    'text',
                    label='Gruppe'
                    )
                #
                # Formular zurückgeben
                return uform
            
            FL = FormListeUnterformular(
                self.frmPersJuEinzelGruppen,
                FactoryFormPersJuEinzelGruppe,
                linkFeld='person_id',
                linkFeldHauptformular='id'
                )
            FL.setGetterDicts(PersonGruppeListe().FactoryGetterDicts(
                keyFeld='person_id',
                Sort='gruppe_kurz_bez'))
            FL.setHauptformular(form)
            navi.formListen['gruppen'] = FL
            #
            # Widgets herstellen, zeigen und in Formular aufnehmen
            form.addWidget(
                'id',
                ttk.Entry(self.frmPersJuEinzelDaten, state=tk.DISABLED, width=6),
                'int',
                label='ID')
            form.lbl_id.grid(column=0, row=0, sticky=tk.W)
            form.id.grid(column=0, row=1, sticky=tk.W)
            
            form.addWidget(
                'name',
                ttk.Entry(self.frmPersJuEinzelDaten),
                'text',
                label='Name'
                )
            form.lbl_name.grid(column=0, row=2, sticky=tk.W)
            form.name.grid(column=0, row=3, sticky=tk.W)
            
            form.addWidget(
                'vorname',
                ttk.Entry(self.frmPersJuEinzelDaten),
                'text',
                label='Vorname'
                )
            form.lbl_vorname.grid(column=1, row=2, columnspan=2, sticky=tk.W)
            form.vorname.grid(column=1, row=3, columnspan=2, sticky=tk.W)
            
            form.addWidget(
                'gebdat',
                ttk.Entry(self.frmPersJuEinzelDaten,
                      width=15,
                      validate='focusout',
                      validatecommand=(self.valDate, '%P'),
                      invalidcommand=(self.invalidHoldFocus, '%W')
                      ),
                'date',
                label='Geb.-Dat.'
                )
            form.lbl_gebdat.grid(column=3, row=2, sticky=tk.W)
            form.gebdat.grid(column=3, row=3, sticky=tk.W)
            
            form.addWidget(
                'geschlecht',
                ComboboxValueLabel(self.frmPersJuEinzelDaten, width=20),
                'text',
                label='Geschlecht'
                )
            form.getWidget('geschlecht').fill((
                ('m', 'männlich'),
                ('w', 'weiblich'),
                ('d', 'divers'),
                ('?', 'nicht erfasst')
                ))
            form.lbl_geschlecht.grid(column=4, row=2, sticky=tk.W)
            form.geschlecht.grid(column=4, row=3, sticky=tk.W)
            
            form.addWidget(
                'strasse',
                ttk.Entry(self.frmPersJuEinzelDaten),
                'text',
                label='Straße'
                )
            form.lbl_strasse.grid(column=0, row=4, sticky=tk.W)
            form.strasse.grid(column=0, row=5, sticky=tk.W)
            
            form.addWidget(
                'plz',
                ttk.Entry(self.frmPersJuEinzelDaten, width=6),
                'text',
                label='PLZ'
                )
            form.lbl_plz.grid(column=1, row=4, sticky=tk.W)
            form.plz.grid(column=1, row=5, sticky=tk.W)
            
            form.addWidget(
                'ort',
                ttk.Entry(self.frmPersJuEinzelDaten),
                'text',
                label='Ort'
                )
            form.lbl_ort.grid(column=2, row=4, columnspan=2, sticky=tk.W)
            form.ort.grid(column=2, row=5, columnspan=2, sticky=tk.W)
            
            form.addWidget(
                'land',
                ttk.Entry(self.frmPersJuEinzelDaten),
                'text',
                label='Land'
                )
            form.lbl_land.grid(column=4, row=4, columnspan=2, sticky=tk.W)
            form.land.grid(column=4, row=5, columnspan=2, sticky=tk.W)
            
            form.addWidget(
                'land_kurz',
                ttk.Entry(self.frmPersJuEinzelDaten, state=tk.DISABLED, width=4),
                'text',
                label='kurz'
                )
            form.lbl_land_kurz.grid(column=6, row=4, sticky=tk.W)
            form.land_kurz.grid(column=6, row=5, sticky=tk.W)
            
            form.addWidget(
                'email',
                ttk.Entry(self.frmPersJuEinzelDaten, width=40),
                'text',
                label='eMail'
                )
            form.lbl_email.grid(column=0, row=6, columnspan=2, sticky=tk.W+tk.N)
            form.email.grid(column=0, row=7, columnspan=2, sticky=tk.W+tk.N)
            
            form.addWidget(
                'tel_heimat',
                ttk.Entry(self.frmPersJuEinzelDaten),
                'text',
                label='Tel. Heimat'
                )
            form.lbl_tel_heimat.grid(column=2, row=6, columnspan=2, sticky=tk.W)
            form.tel_heimat.grid(column=2, row=7, columnspan=2, sticky=tk.W)
            
            form.addWidget(
                'tel_mobil',
                ttk.Entry(self.frmPersJuEinzelDaten),
                'text',
                label='Tel. mobil'
                )
            form.lbl_tel_mobil.grid(column=4, row=6, columnspan=2, sticky=tk.W)
            form.tel_mobil.grid(column=4, row=7, columnspan=2, sticky=tk.W)
            
            self.frmPersJuEinzelReisegruppe = ttk.LabelFrame(
                self.frmPersJuEinzelDaten,
                text='Reisegruppe'
                )
            self.frmPersJuEinzelReisegruppe.grid(column=0, row=8, columnspan=6, sticky=tk.W)
            
            form.addWidget(
                'g_ansprechpartner',
                ttk.Checkbutton(self.frmPersJuEinzelReisegruppe),
                'bool',
                label='Gr-Leiter'
                )
            Tooltip(form.g_ansprechpartner, 'Person ist Ansprechpartner für eine Reisegruppe,\nz.B. Konfirmandengruppe')
            form.lbl_g_ansprechpartner.grid(column=0, row=0, sticky=tk.W)
            form.g_ansprechpartner.grid(column=0, row=1, sticky=tk.W)
            
            form.addWidget(
                'g_beschreibung',
                ttk.Entry(self.frmPersJuEinzelReisegruppe, width=50),
                'text',
                label='Beschreibung'
                )
            Tooltip(form.g_beschreibung, 'Z.B. Konfirmandengruppe Hintertupfingen')
            form.lbl_g_beschreibung.grid(column=1, row=0, sticky=tk.W)
            form.g_beschreibung.grid(column=1, row=1, sticky=tk.W)
            
            form.addWidget(
                'g_anzahl',
                ttk.Entry(
                    self.frmPersJuEinzelReisegruppe,
                    width=8,
                    justify='right',
                    validate='key',
                    validatecommand=(self.valInt, '%P')
                    ),
                'int',
                label='Anzahl TN'
                )
            form.lbl_g_anzahl.grid(column=2, row=0, sticky=tk.W)
            form.g_anzahl.grid(column=2, row=1, sticky=tk.W)
            
            form.addWidget(
                'g_ansprechpartner_id',
                ComboboxValueLabel(self.frmPersJuEinzelReisegruppe, width=50),
                'text',
                label=ttk.Label(self.frmPersJuEinzelReisegruppe, text='Gehört zur Gruppe:')
                )
            Tooltip(form.g_ansprechpartner_id, 'Person gehört zu einer Reisegruppe\nvon...')
            form.lbl_g_ansprechpartner_id.grid(column=0, row=2, columnspan=2, sticky=tk.W)
            form.g_ansprechpartner_id.grid(column=0, row=3, columnspan=2, sticky=tk.W)
            
            form.addWidget(
                'sprachen',
                ttk.Entry(self.frmPersJuEinzelDaten),
                'text',
                label='Sprachen'
                )
            Tooltip(form.sprachen, 'Spricht diese Sprachen')
            form.lbl_sprachen.grid(column=0, row=9, sticky=tk.W)
            form.sprachen.grid(column=0, row=10, sticky=tk.W)
            
            form.addWidget(
                'aufgabe',
                ttk.Entry(self.frmPersJuEinzelDaten),
                'text',
                label='Aufgabe'
                )
            Tooltip(form.aufgabe, 'Aufgabe(n) auf der Tagung, z.B. "Di spülen"')
            form.lbl_aufgabe.grid(column=1, row=9, columnspan=2, sticky=tk.W)
            form.aufgabe.grid(column=1, row=10, columnspan=2, sticky=tk.W)
            
            form.addWidget(
                'vegetarier',
                ttk.Checkbutton(self.frmPersJuEinzelDaten),
                'bool',
                label='vegetarisch'
                )
            form.lbl_vegetarier.grid(column=0, row=11, sticky=tk.E)
            form.vegetarier.grid(column=1, row=11, sticky=tk.W)
            
            form.addWidget(
                'vegan',
                ttk.Checkbutton(self.frmPersJuEinzelDaten),
                'bool',
                label='vegan'
                )
            form.lbl_vegan.grid(column=0, row=12, sticky=tk.E)
            form.vegan.grid(column=1, row=12, sticky=tk.W)
            
            form.addWidget(
                'glutenfrei',
                ttk.Checkbutton(self.frmPersJuEinzelDaten),
                'bool',
                label='glutenfrei'
                )
            form.lbl_glutenfrei.grid(column=0, row=13, sticky=tk.E)
            form.glutenfrei.grid(column=1, row=13, sticky=tk.W)
            
            form.addWidget(
                'lactosefrei',
                ttk.Checkbutton(self.frmPersJuEinzelDaten),
                'bool',
                label='lactosefrei'
                )
            form.lbl_lactosefrei.grid(column=0, row=14, sticky=tk.E)
            form.lactosefrei.grid(column=1, row=14, sticky=tk.W)
            
            form.addWidget(
                'ws_a',
                ttk.Entry(self.frmPersJuEinzelDaten, width=8),
                'text',
                label='WS A:'
                )
            form.lbl_ws_a.grid(column=2, row=11, sticky=tk.E)
            form.ws_a.grid(column=3, row=11, sticky=tk.W)
            
            form.addWidget(
                'ws_b',
                ttk.Entry(self.frmPersJuEinzelDaten, width=8),
                'text',
                label='WS B:'
                )
            form.lbl_ws_b.grid(column=2, row=12, sticky=tk.E)
            form.ws_b.grid(column=3, row=12, sticky=tk.W)
            
            form.addWidget(
                'ws_c',
                ttk.Entry(self.frmPersJuEinzelDaten, width=8),
                'text',
                label='WS C:'
                )
            form.lbl_ws_c.grid(column=2, row=13, sticky=tk.E)
            form.ws_c.grid(column=3, row=13, sticky=tk.W)
            
            form.addWidget(
                'ws_d',
                ttk.Entry(self.frmPersJuEinzelDaten, width=8),
                'text',
                label='WS D:'
                )
            form.lbl_ws_d.grid(column=2, row=14, sticky=tk.E)
            form.ws_d.grid(column=3, row=14, sticky=tk.W)
            
            ttk.Label(self.frmPersJuEinzelDaten, text='Beitrag').grid(
                  column=4,
                  row=10,
                  columnspan=2,
                  sticky=tk.E)
            
            form.addWidget(
                'beitr_anm',
                ttk.Entry(
                    self.frmPersJuEinzelDaten,
                    width=6,
                    justify='right',
                    validate='key',
                    validatecommand=(self.valInt, '%P')
                    ),
                'int',
                label='Anm.'
                )
            Tooltip(form.beitr_anm, 'TN-Beitrag, wie bei\nder Anmeldung angegeben')
            form.lbl_beitr_anm.grid(column=4, row=11, sticky=tk.E)
            form.beitr_anm.grid(column=5, row=11, sticky=tk.W)
            
            form.addWidget(
                'beitr_erm',
                ttk.Entry(
                    self.frmPersJuEinzelDaten,
                    width=6,
                    justify='right',
                    validate='key',
                    validatecommand=(self.valInt, '%P')
                    ),
                'int',
                label='Erm.'
                )
            Tooltip(form.beitr_erm, 'Ermäßigter TN-Beitrag,\nwie verabredet.\n1 für vollständigen Nachlass')
            form.lbl_beitr_erm.grid(column=4, row=12, sticky=tk.E)
            form.beitr_erm.grid(column=5, row=12, sticky=tk.W)
            
            form.addWidget(
                'beitr_gez',
                ttk.Entry(
                    self.frmPersJuEinzelDaten,
                    width=6,
                    justify='right',
                    validate='key',
                    validatecommand=(self.valInt, '%P')
                    ),
                'int',
                label='Bez.'
                )
            Tooltip(form.beitr_gez, 'TN-Beitrag, der\ntatsächlich gezahlt\nund schon verbucht wurde')
            form.lbl_beitr_gez.grid(column=4, row=13, sticky=tk.E)
            form.beitr_gez.grid(column=5, row=13, sticky=tk.W)
            
            form.addWidget(
                'beitr_dat',
                ttk.Entry(
                    self.frmPersJuEinzelDaten,
                    width=6,
                    validate='focusout',
                    validatecommand=(self.valDate, '%P'),
                    invalidcommand=(self.invalidHoldFocus, '%W')
                    ),
                'date',
                label='Datum'
                )
            Tooltip(form.beitr_dat, 'Wann der TN-Beitrag\nbezahlt wurde')
            form.lbl_beitr_dat.grid(column=4, row=14, sticky=tk.E)
            form.beitr_dat.grid(column=5, row=14, sticky=tk.W)
            
            form.addWidget(
                'status',
                ComboboxValueLabel(
                    self.frmPersJuEinzelDaten,
                    width=20,
                    state='readonly'
                    ),
                'text',
                label='Status'
                )
            Tooltip(form.status, 'Anmelde-Status')
            form.lbl_status.grid(column=0, row=15, sticky=tk.W)
            form.status.grid(column=0, row=16, sticky=tk.W)
            
            form.addWidget(
                'status_gesetzt_am',
                ttk.Entry(self.frmPersJuEinzelDaten, width=15, state=tk.DISABLED),
                'date',
                label='... gesetzt am'
                )
            form.status_gesetzt_am.grid(column=0, row=17, sticky=tk.W)
            
            form.addWidget(
                'anm_am_um',
                ttk.Entry(self.frmPersJuEinzelDaten, width=20, state=tk.DISABLED),
                'datetime',
                label='Anm. am/um'
                )
            form.lbl_anm_am_um.grid(column=0, row=18, sticky=tk.W)
            form.anm_am_um.grid(column=0, row=19, sticky=tk.W)
            
            form.addWidget(
                'nachricht',
                scrolledtext.ScrolledText(self.frmPersJuEinzelDaten, width=35, height=6),
                'text',
                label=ttk.Label(self.frmPersJuEinzelDaten, text='Nachricht')
                )
            Tooltip(form.nachricht, 'Nachricht des TN\naus der Online-Anmeldung')
            form.lbl_nachricht.grid(column=1, row=15, columnspan=3, sticky=tk.W)
            form.nachricht.grid(column=1, row=16, columnspan=3, rowspan=4, sticky=tk.W)
            
            form.addWidget(
                'bemerkung',
                scrolledtext.ScrolledText(self.frmPersJuEinzelDaten, width=35, height=6),
                'text',
                label=ttk.Label(self.frmPersJuEinzelDaten, text='Bemerkung')
                )
            Tooltip(form.bemerkung, 'Bemerkung(en) des TB')
            form.lbl_bemerkung.grid(column=4, row=15, columnspan=3, sticky=tk.W)
            form.bemerkung.grid(column=4, row=16, columnspan=3, rowspan=4, sticky=tk.W)
            
            bearbVonAm = BearbVonAm(self.frmPersJuEinzelDaten)
            bearbVonAm.grid(column=0, row=20, columnspan=3, sticky=tk.W)
            bearbVonAm.connectToForm(form)
        #
        # Personen Anmeldestatus
        def FactoryPersonStatusListe():
            form = Form()
            #
            # Navi herstellen und einsetzen
            navi = NaviForm(self.frmPersonenStatusListeInhalt.innerFrame, elemente=('save', 'delete'))
            form.setNavi(navi)
            #
            # Navi konfigurieren
            navi.connectToModell(
                PersonStatus,
                selects=('status',))
            #
            # Widgets
            form.addWidget(
                'id',
                ttk.Entry(
                    self.frmPersonenStatusListeInhalt.innerFrame,
                    state=tk.DISABLED,
                    width=6),
                'int',
                label='ID')
            form.addWidget(
                'status',
                ComboboxValueLabel(
                    self.frmPersonenStatusListeInhalt.innerFrame,
                    width=10),
                'text',
                label='Status')
            form.addWidget(
                'name',
                ttk.Entry(
                    self.frmPersonenStatusListeInhalt.innerFrame,
                    state=tk.DISABLED,
                    width=12),
                'text',
                label='Name')
            form.addWidget(
                'vorname',
                ttk.Entry(
                    self.frmPersonenStatusListeInhalt.innerFrame,
                    state=tk.DISABLED,
                    width=12),
                'text',
                label='Vorname')
            form.addWidget(
                'gebdat',
                ttk.Entry(
                    self.frmPersonenStatusListeInhalt.innerFrame,
                    state=tk.DISABLED,
                    width=12),
                'date',
                label='Geb.-Dat.')
            form.addWidget(
                'geschlecht',
                ComboboxValueLabel(
                    self.frmPersonenStatusListeInhalt.innerFrame,
                    state=tk.DISABLED,
                    width=12),
                'text',
                label='Geschlecht'
                )
            form.getWidget('geschlecht').fill((
                ('m', 'männlich'),
                ('w', 'weiblich'),
                ('d', 'divers'),
                ('?', 'nicht erfasst')
                ))
            form.addWidget(
                'ort',
                ttk.Entry(
                    self.frmPersonenStatusListeInhalt.innerFrame,
                    stat=tk.DISABLED,
                    width=12),
                'text',
                label='Ort')
            form.addWidget(
                'land',
                ttk.Entry(
                    self.frmPersonenStatusListeInhalt.innerFrame,
                    stat=tk.DISABLED,
                    width=10),
                'text',
                label='Land')
            form.addWidget(
                'email',
                ttk.Entry(
                    self.frmPersonenStatusListeInhalt.innerFrame,
                    stat=tk.DISABLED,
                    width=15),
                'text',
                label='eMail')
            form.addWidget(
                'beitr_anm',
                ttk.Entry(
                    self.frmPersonenStatusListeInhalt.innerFrame,
                    stat=tk.DISABLED,
                    justify='right',
                    width=5),
                'int',
                label='Beitr.')
            form.addWidget(
                'nachricht',
                ttk.Entry(
                    self.frmPersonenStatusListeInhalt.innerFrame,
                    stat=tk.DISABLED,
                    width=15),
                'text',
                label='Nachricht')
            #
            # Formular zurückgeben
            return form
                
        with FormListe(self.frmPersonenStatusListeInhalt.innerFrame, FactoryPersonStatusListe) as form:
            glb.formPersonStatusListe = form
            #
            # Navi herstellen und einsetzen
            navi = NaviListe(self.frmPersonenStatusListeNavi)
            form.setNavi(navi)
            #
            # Navi konfigurieren
            P = PersonStatus()
            navi.setGetterDicts(P.FactoryGetterDicts(
                    FilterFelder=('name', 'vorname', 'ort'),
                    Sort='status, name, vorname'))
            #
            # Form Navi packen
            form.getNavi().pack(anchor=tk.W)
        #
        # Personen WS-Anm zuordnen Liste
        def FactoryWSAnmZuordnenListe():
            form = Form()
            #
            # Navi herstellen und einsetzen
            navi = NaviForm(
                self.frmWSAnmZuordnenListeInhalt.innerFrame,
                elemente=('save', 'delete'))
            form.setNavi(navi)
            #
            # Navi konfigurieren
            navi.connectToModell(AnmWSListe)
            #
            # Widgets
            form.addWidget(
                'id',
                ttk.Entry(self.frmWSAnmZuordnenListeInhalt.innerFrame,
                    state=tk.DISABLED,
                    justify='right',
                    width=6),
                'int',
                label='ID')
            form.addWidget(
                'tn_id',
                ttk.Entry(self.frmWSAnmZuordnenListeInhalt.innerFrame,
                    justify='right',
                    width=6),
                'int',
                label='TN-ID')
            form.addWidget(
                'name',
                ttk.Entry(self.frmWSAnmZuordnenListeInhalt.innerFrame,
                    width=15),
                'text',
                label='Name')
            form.addWidget(
                'vorname',
                ttk.Entry(self.frmWSAnmZuordnenListeInhalt.innerFrame,
                    width=15),
                'text',
                label='Vorname')
            form.addWidget(
                'email',
                ttk.Entry(self.frmWSAnmZuordnenListeInhalt.innerFrame,
                    width=25),
                'text',
                label='eMail')
            form.addWidget(
                'ws_a_i',
                ttk.Entry(self.frmWSAnmZuordnenListeInhalt.innerFrame,
                    width=8),
                'text',
                label='1. Wahl')
            form.addWidget(
                'ws_a_ii',
                ttk.Entry(self.frmWSAnmZuordnenListeInhalt.innerFrame,
                    width=8),
                'text',
                label='2. Wahl')
            form.addWidget(
                'ws_a_iii',
                ttk.Entry(self.frmWSAnmZuordnenListeInhalt.innerFrame,
                    width=8),
                'text',
                label='3. Wahl')
            form.addWidget(
                'nachricht',
                ttk.Entry(self.frmWSAnmZuordnenListeInhalt.innerFrame,
                    width=25),
                'text',
                label='Nachricht')
            #
            # Formular zurückgeben
            return form
        
        with FormListe(self.frmWSAnmZuordnenListeInhalt.innerFrame, FactoryWSAnmZuordnenListe) as form:
            glb.formWSAnmZuordnen = form
            #
            # Navi herstellen und einsetzen
            navi = NaviListe(self.frmWSAnmZuordnenListeNavi)
            form.setNavi(navi)
            #
            # Navi konfigurieren
            W = AnmWSListe()
            navi.setGetterDicts(W.FactoryGetterDicts(
                    FilterFelder=('name', 'vorname', 'ort'),
                    Sort='tn_id, name, vorname'))
            #
            # Form Navi packen
            form.getNavi().pack(anchor=tk.W)
        
        def FactoryWSAnmZuordnenPersonen():
            form = Form()
            #
            # Navi herstellen und einsetzen
            navi = NaviForm(
                self.frmWSAnmZuordnenPersInhalt.innerFrame,
                elemente=('refresh',))
            form.setNavi(navi)
            #
            # Navi konfigurieren
            navi.connectToModell(PersonWSAnmListe)
            #
            # Widgets
            form.addWidget(
                'id',
                ttk.Entry(self.frmWSAnmZuordnenPersInhalt.innerFrame,
                    state=tk.DISABLED,
                    justify='right',
                    width=6),
                'int',
                label='ID')
            form.addWidget(
                'name',
                ttk.Entry(self.frmWSAnmZuordnenPersInhalt.innerFrame,
                    state=tk.DISABLED,
                    width=15),
                'text',
                label='Name')
            form.addWidget(
                'vorname',
                ttk.Entry(self.frmWSAnmZuordnenPersInhalt.innerFrame,
                    state=tk.DISABLED,
                    width=15),
                'text',
                label='Vorname')
            form.addWidget(
                'email',
                ttk.Entry(self.frmWSAnmZuordnenPersInhalt.innerFrame,
                    state=tk.DISABLED,
                    width=25),
                'text',
                label='eMail')
            form.addWidget(
                'ort',
                ttk.Entry(self.frmWSAnmZuordnenPersInhalt.innerFrame,
                    state=tk.DISABLED,
                    width=15),
                'text',
                label='Ort')
            #
            # Formular zurückgeben
            return form
        
        with FormListe(self.frmWSAnmZuordnenPersInhalt.innerFrame, FactoryWSAnmZuordnenPersonen) as form:
            glb.formWSAnmPersonen = form
            #
            # Navi herstellen und einsetzen
            navi = NaviListe(self.frmWSAnmZuordnenPersNavi)
            form.setNavi(navi)
            #
            # Navi konfigurieren
            P = PersonWSAnmListe()
            navi.setGetterDicts(P.FactoryGetterDicts(
                    FilterFelder=('name', 'vorname', 'email', 'ort'),
                    Sort='name, vorname'))
            #
            # Form Navi packen
            form.getNavi().pack(anchor=tk.W)
        #
        # Personen WS festlegen
        def FactoryWSFestlegenListe():
            form = Form()
            #
            # Navi herstellen und einsetzen
            navi = NaviForm(
                self.frmWSFestlegenInhalt.innerFrame,
                elemente=('save', 'delete'))
            form.setNavi(navi)
            #
            # Navi konfigurieren
            navi.connectToModell(PersonWSListe)
            #
            # Widgets
            form.addWidget(
                'id',
                ttk.Entry(self.frmWSFestlegenInhalt.innerFrame,
                    state=tk.DISABLED,
                    justify='right',
                    width=6),
                'int',
                label='ID')
            form.addWidget(
                'name',
                ttk.Entry(self.frmWSFestlegenInhalt.innerFrame,
                    width=15),
                'text',
                label='Name')
            form.addWidget(
                'vorname',
                ttk.Entry(self.frmWSFestlegenInhalt.innerFrame,
                    width=15),
                'text',
                label='Vorname')
            form.addWidget(
                'ort',
                ttk.Entry(self.frmWSFestlegenInhalt.innerFrame,
                    width=15),
                'text',
                label='Ort')
            form.addWidget(
                'ws_a',
                ttk.Entry(self.frmWSFestlegenInhalt.innerFrame,
                    width=8),
                'text',
                label='WS A')
            form.addWidget(
                'ws_b',
                ttk.Entry(self.frmWSFestlegenInhalt.innerFrame,
                    width=8),
                'text',
                label='WS B')
            form.addWidget(
                'ws_c',
                ttk.Entry(self.frmWSFestlegenInhalt.innerFrame,
                    width=8),
                'text',
                label='WS C')
            form.addWidget(
                'ws_d',
                ttk.Entry(self.frmWSFestlegenInhalt.innerFrame,
                    width=8),
                'text',
                label='WS D')
            #
            # Formular zurückgeben
            return form
        
        with FormListe(self.frmWSFestlegenInhalt.innerFrame, FactoryWSFestlegenListe) as form:
            glb.formWSFestlegen = form
            #
            # Navi herstellen und einsetzen
            navi = NaviListe(self.frmWSFestlegenNavi)
            form.setNavi(navi)
            #
            # Navi konfigurieren
            P = PersonWSListe()
            navi.setGetterDicts(P.FactoryGetterDicts(
                    FilterFelder=('name', 'vorname', 'ort'),
                    Sort='name, vorname, ort'))
            #
            # Form Navi packen
            form.getNavi().pack(anchor=tk.W)
        #
        # Personen Finanzen Einzelheiten
        with Form() as form:
            glb.formPersFinanzenEinzel = form
            #
            # Frames für Navi, Formular und Unterformulare
            self.frmPersFinanzenEinzelNavi = ttk.Frame(self.frmPersonenFinanzenEinzel)
            self.frmPersFinanzenEinzelDaten = ttk.Frame(self.frmPersonenFinanzenEinzel)
            
            self.frmPersFinanzenEinzelNavi.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            ttk.Separator(self.frmPersonenFinanzenEinzel, orient=tk.VERTICAL).pack(
                side=tk.LEFT,
                fill=tk.BOTH,
                expand=True)
            self.frmPersFinanzenEinzelDaten.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            #
            # Navi herstellen und einsetzen
            navi = NaviForm(self.frmPersFinanzenEinzelNavi)
            form.setNavi(navi)
            navi.pack(fill=tk.BOTH, expand=True)
            #
            # Navi konfigurieren
            navi.connectToModell(
                PersonFinanzen,
                selects=('status',),
                keyFeldNavi='id',
                labelFelder=('name', 'vorname', 'id',),
                filterFelder=('name', 'vorname', 'ort',),
                Sort='name, vorname')
            #
            # Widgets herstellen, zeigen und in Formular aufnehmen
            form.addWidget(
                'id',
                ttk.Entry(self.frmPersFinanzenEinzelDaten, state=tk.DISABLED, width=6),
                'int',
                label='ID')
            form.lbl_id.grid(column=0, row=0, sticky=tk.W)
            form.id.grid(column=0, row=1, sticky=tk.W)
            
            form.addWidget(
                'name',
                ttk.Entry(self.frmPersFinanzenEinzelDaten, state=tk.DISABLED),
                'text',
                label='Name'
                )
            form.lbl_name.grid(column=0, row=2, sticky=tk.W)
            form.name.grid(column=0, row=3, sticky=tk.W)
            
            form.addWidget(
                'vorname',
                ttk.Entry(self.frmPersFinanzenEinzelDaten, state=tk.DISABLED),
                'text',
                label='Vorname'
                )
            form.lbl_vorname.grid(column=1, row=2, sticky=tk.W)
            form.vorname.grid(column=1, row=3, sticky=tk.W)
            
            form.addWidget(
                'ort',
                ttk.Entry(self.frmPersFinanzenEinzelDaten, state=tk.DISABLED),
                'text',
                label='Ort'
                )
            form.lbl_ort.grid(column=0, row=4, sticky=tk.W)
            form.ort.grid(column=0, row=5, sticky=tk.W)
            
            form.addWidget(
                'land_kurz',
                ttk.Entry(self.frmPersFinanzenEinzelDaten, state=tk.DISABLED, width=4),
                'text',
                label='kurz'
                )
            form.lbl_land_kurz.grid(column=1, row=4, sticky=tk.W)
            form.land_kurz.grid(column=1, row=5, sticky=tk.W)
            
            form.addWidget(
                'email',
                ttk.Entry(self.frmPersFinanzenEinzelDaten, state=tk.DISABLED, width=40),
                'text',
                label='eMail'
                )
            form.lbl_email.grid(column=0, row=6, columnspan=2, sticky=tk.W+tk.N)
            form.email.grid(column=0, row=7, columnspan=2, sticky=tk.W+tk.N)
            
            ttk.Label(self.frmPersFinanzenEinzelDaten, text='TN-Beitrag').grid(
                column=2,
                row=2,
                columnspan=2,
                sticky=tk.W)
            
            form.addWidget(
                'beitr_anm',
                ttk.Entry(
                    self.frmPersFinanzenEinzelDaten,
                    state=tk.DISABLED,
                    width=6,
                    justify='right',
                    validate='key',
                    validatecommand=(self.valInt, '%P')
                    ),
                'int',
                label='Bei Anm.:'
                )
            form.lbl_beitr_anm.grid(column=2, row=3, sticky=tk.E)
            form.beitr_anm.grid(column=3, row=3, sticky=tk.W)
            
            form.addWidget(
                'beitr_erm',
                ttk.Entry(
                    self.frmPersFinanzenEinzelDaten,
                    width=6,
                    justify='right',
                    validate='key',
                    validatecommand=(self.valInt, '%P')
                    ),
                'int',
                label='Ermäßigt:'
                )
            form.lbl_beitr_erm.grid(column=2, row=4, sticky=tk.E)
            form.beitr_erm.grid(column=3, row=4, sticky=tk.W)
            
            form.addWidget(
                'beitr_gez',
                ttk.Entry(
                    self.frmPersFinanzenEinzelDaten,
                    width=6,
                    justify='right',
                    validate='key',
                    validatecommand=(self.valInt, '%P')
                    ),
                'int',
                label='Gezahlt:'
                )
            form.lbl_beitr_gez.grid(column=2, row=5, sticky=tk.E)
            form.beitr_gez.grid(column=3, row=5, sticky=tk.W)
            
            form.addWidget(
                'beitr_dat',
                ttk.Entry(
                    self.frmPersFinanzenEinzelDaten,
                    width=8,
                    validate='focusout',
                    validatecommand=(self.valDate, '%P'),
                    invalidcommand=(self.invalidHoldFocus, '%W')
                    ),
                'date',
                label='am:'
                )
            form.lbl_beitr_dat.grid(column=2, row=6, sticky=tk.E)
            form.beitr_dat.grid(column=3, row=6, sticky=tk.W)
            
            form.addWidget(
                'status',
                ComboboxValueLabel(
                    self.frmPersFinanzenEinzelDaten,
                    state=tk.DISABLED,
                    width=20
                    ),
                'text',
                label='Status'
                )
            form.lbl_status.grid(column=0, row=8, sticky=tk.W)
            form.status.grid(column=0, row=9, sticky=tk.W)
            
            form.addWidget(
                'bemerkung',
                scrolledtext.ScrolledText(self.frmPersFinanzenEinzelDaten, width=35, height=6),
                'text',
                label=ttk.Label(self.frmPersFinanzenEinzelDaten, text='Bemerkung')
                )
            form.lbl_bemerkung.grid(column=0, row=10, columnspan=4, sticky=tk.W)
            form.bemerkung.grid(column=0, row=11, columnspan=4, sticky=tk.W)
            
            bearbVonAm = BearbVonAm(self.frmPersFinanzenEinzelDaten)
            bearbVonAm.grid(column=0, row=12, columnspan=4, sticky=tk.W)
            bearbVonAm.connectToForm(form)
        #
        # Personen Finanzen als Liste
        def FactoryPersonenFinanzenListe():
            form = Form()
            #
            # Navi herstellen und einsetzen
            navi = NaviForm(
                self.frmPersonenFinanzenListeInhalt.innerFrame,
                elemente=('save', 'delete'))
            form.setNavi(navi)
            #
            # Navi konfigurieren
            navi.connectToModell(
                PersonFinanzenListe,
                selects=('status',))
            #
            # Widgets
            form.addWidget(
                'id',
                ttk.Entry(self.frmPersonenFinanzenListeInhalt.innerFrame,
                    state=tk.DISABLED,
                    width=6),
                'int',
                label='ID')
            form.addWidget(
                'name',
                ttk.Entry(
                    self.frmPersonenFinanzenListeInhalt.innerFrame,
                    width=15,
                    state=tk.DISABLED),
                'text',
                label='Name')
            form.addWidget(
                'vorname',
                ttk.Entry(
                    self.frmPersonenFinanzenListeInhalt.innerFrame,
                    width=15,
                    state=tk.DISABLED),
                'text',
                label='Vorname')
            form.addWidget(
                'ort',
                ttk.Entry(
                    self.frmPersonenFinanzenListeInhalt.innerFrame,
                    width=15,
                    state=tk.DISABLED),
                'text',
                label='Ort')
            form.addWidget(
                'status',
                ComboboxValueLabel(
                    self.frmPersonenFinanzenListeInhalt.innerFrame,
                    state=tk.DISABLED,
                    width=15),
                'text',
                label='Status')
            form.addWidget(
                'beitr_anm',
                ttk.Entry(
                    self.frmPersonenFinanzenListeInhalt.innerFrame,
                    state=tk.DISABLED,
                    width=5,
                    justify='right'),
                'int',
                label='B Anm')
            form.addWidget(
                'beitr_erm',
                ttk.Entry(
                    self.frmPersonenFinanzenListeInhalt.innerFrame,
                    validate='key',
                    validatecommand=(self.valInt, '%P'),
                    width=5,
                    justify='right'),
                'int',
                label='B Erm')
            form.addWidget(
                'beitr_gez',
                ttk.Entry(
                    self.frmPersonenFinanzenListeInhalt.innerFrame,
                    validate='key',
                    validatecommand=(self.valInt, '%P'),
                    width=5,
                    justify='right'),
                'int',
                label='B Gez')
            form.addWidget(
                'beitr_dat',
                ttk.Entry(
                    self.frmPersonenFinanzenListeInhalt.innerFrame,
                    width=12,
                    validate='focusout',
                    validatecommand=(self.valDate, '%P'),
                    invalidcommand=(self.invalidHoldFocus, '%W')
                    ),
                'date',
                label='B Dat'
                )
            form.addWidget(
                'bemerkung',
                scrolledtext.ScrolledText(
                    self.frmPersonenFinanzenListeInhalt.innerFrame,
                    width=20,
                    height=2),
                'text',
                label=ttk.Label(self.frmPersonenFinanzenListeInhalt.innerFrame, text='Bemerkung'))
            #
            # Formular zurückgeben
            return form
                
        with FormListe(self.frmPersonenFinanzenListeInhalt.innerFrame, FactoryPersonenFinanzenListe) as form:
            glb.formPersonenFinanzenListe = form
            #
            # Navi herstellen und einsetzen
            navi = NaviListe(self.frmPersonenFinanzenListeNavi)
            form.setNavi(navi)
            #
            # Navi konfigurieren
            P = PersonFinanzenListe()
            navi.setGetterDicts(P.FactoryGetterDicts(
                    FilterFelder=('name', 'vorname', 'ort'),
                    Sort='beitr_gez, name, vorname, id'))
            #
            # Form Navi packen
            form.getNavi().pack(anchor=tk.W)
        #
        # Veranstaltungen Einzelheiten
        with Form() as form:
            glb.formVAEinzelheiten = form
            #
            # Frames für Navi, Formular und Unterformulare
            self.frmVAEinzelNavi = ttk.Frame(self.frmVAEinzelheiten)
            self.frmVAEinzelInhalt = ttk.Frame(self.frmVAEinzelheiten)
            self.frmVAEinzelheiten.add(self.frmVAEinzelNavi)
            self.frmVAEinzelheiten.add(self.frmVAEinzelInhalt)
            
            self.frmVAEinzelDaten = ttk.Frame(self.frmVAEinzelInhalt)
            self.frmVAEinzelUnterformulare = ttk.Frame(self.frmVAEinzelInhalt)
            self.frmVAEinzelDaten.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            ttk.Separator(self.frmVAEinzelInhalt, orient=tk.VERTICAL).pack(
                      side=tk.LEFT, fill=tk.BOTH, expand=True)
            self.frmVAEinzelUnterformulare.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            
            self.sfrVAEinzelDozenten = yScrolledFrame(self.frmVAEinzelUnterformulare)
            self.frmVAEinzelDozenten = self.sfrVAEinzelDozenten.innerFrame
            ttk.Label(self.frmVAEinzelUnterformulare, text='Dozenten').pack(
                  side=tk.TOP,
                  anchor=tk.W)
            self.sfrVAEinzelDozenten.pack(side=tk.TOP, fill=tk.BOTH)
            
            self.sfrVAEinzelRaum = yScrolledFrame(self.frmVAEinzelUnterformulare)
            self.frmVAEinzelRaum = self.sfrVAEinzelRaum.innerFrame
            ttk.Label(self.frmVAEinzelUnterformulare, text='Raum').pack(
                  side=tk.TOP,
                  anchor=tk.W)
            self.sfrVAEinzelRaum.pack(side=tk.TOP, fill=tk.BOTH)
            
            #
            # Navi herstellen und einsetzen
            navi = NaviForm(self.frmVAEinzelNavi)
            form.setNavi(navi)
            navi.pack(fill=tk.BOTH, expand=True)
            #
            # Navi konfigurieren
            navi.connectToModell(
                Veranstaltung,
                selects=('art',),
                keyFeldNavi='id',
                labelFelder=('art', 'nr', 'titel'),
                filterFelder=('art', 'titel', 'untertitel'),
                Sort='art, nr')
            #
            # Unterformulare herstellen und an Navi hängen
            #
            # ... für Dozenten
            def FactoryFormVAEinzelDozent():
                uform = Form()
                #
                # Navi herstellen und einsetzen
                unavi = NaviForm(self.frmVAEinzelDozenten, elemente=('save', 'delete'))
                uform.setNavi(unavi)
                #
                # Navi konfigurieren
                unavi.connectToModell(
                    DozentListe,
                    selects=('person_id',))
                #
                # Widgets
                uform.addWidget(
                    'id',
                    ttk.Entry(self.frmVAEinzelDozenten, state=tk.DISABLED, width=4),
                    'int',
                    label='ID')
                uform.addWidget(
                    'veranstaltung_id',
                    ttk.Entry(self.frmVAEinzelDozenten, state=tk.DISABLED, width=5),
                    'int',
                    label='VA-ID')
                uform.addWidget(
                    'person_id',
                    ComboboxValueLabel(
                        self.frmVAEinzelDozenten,
                        width=20,
                        state='readonly'),
                    'int',
                    label='Person')
                uform.addWidget(
                    'funktion',
                    ttk.Entry(self.frmVAEinzelDozenten, width=15),
                    'text',
                    label='Funktion')
                #
                # Formular zurückgeben
                return uform
            
            FL = FormListeUnterformular(
                self.frmVAEinzelDozenten,
                FactoryFormVAEinzelDozent,
                linkFeld='veranstaltung_id',
                linkFeldHauptformular='id')
            FL.setGetterDicts(DozentListe().FactoryGetterDicts(
                keyFeld='veranstaltung_id'))
            FL.setHauptformular(form)
            navi.formListen['dozenten'] = FL
            #
            # ... für Raumbelegung
            def FactoryFormVAEinzelRaum():
                uform = Form()
                #
                # Navi herstellen und einsetzen
                unavi = NaviForm(self.frmVAEinzelRaum, elemente=('save', 'delete'))
                uform.setNavi(unavi)
                #
                # Navi konfigurieren
                unavi.connectToModell(
                    RaumbelegungListe,
                    selects=('raum_kurz_bez',))
                #
                # Widgets
                uform.addWidget(
                    'id',
                    ttk.Entry(self.frmVAEinzelRaum, state=tk.DISABLED, width=6),
                    'int',
                    label='ID')
                uform.addWidget(
                    'veranstaltung_id',
                    ttk.Entry(self.frmVAEinzelRaum, state=tk.DISABLED, width=6),
                    'int',
                    label='VA-ID')
                uform.addWidget(
                    'raum_kurz_bez',
                    ComboboxValueLabel(
                        self.frmVAEinzelRaum,
                        width=10),
                    'text',
                    label='Kurz-Bez.')
                uform.addWidget(
                    'datum',
                    ttk.Entry(
                        self.frmVAEinzelRaum,
                        width=10,
                        validate='focusout',
                        validatecommand=(self.valDate, '%P'),
                        invalidcommand=(self.invalidHoldFocus, '%W')
                        ),
                    'date',
                    label='Datum')
                uform.addWidget(
                    'zeit_von',
                    ttk.Entry(
                        self.frmVAEinzelRaum,
                        width=5,
                        justify='right',
                        validate='focusout',
                        validatecommand=(self.valTime, '%P'),
                        invalidcommand=(self.invalidHoldFocus, '%W')
                        ),
                    'time',
                    label='Start')
                uform.addWidget(
                    'zeit_bis',
                    ttk.Entry(
                        self.frmVAEinzelRaum,
                        width=5,
                        justify='right',
                        validate='focusout',
                        validatecommand=(self.valTime, '%P'),
                        invalidcommand=(self.invalidHoldFocus, '%W')
                        ),
                    'time',
                    label='Ende')
                #
                # Formualr zurückgeben
                return uform
            
            FL = FormListeUnterformular(
                self.frmVAEinzelRaum,
                FactoryFormVAEinzelRaum,
                linkFeld='veranstaltung_id',
                linkFeldHauptformular='id')
            FL.setGetterDicts(RaumbelegungListe().FactoryGetterDicts(
                keyFeld='veranstaltung_id'))
            FL.setHauptformular(form)
            navi.formListen['raumbelegung'] = FL
                
            #
            # Widgets
            form.addWidget(
                'id',
                ttk.Entry(self.frmVAEinzelDaten, state=tk.DISABLED),
                'int',
                label='ID')
            form.lbl_id.grid(column=0, row=0, sticky=tk.E)
            form.id.grid(column=0, row=1, sticky=tk.W)
            
            form.addWidget(
                'art',
                ComboboxValueLabel(
                    self.frmVAEinzelDaten,
                    width=25),
                'text',
                label='Art')
            form.lbl_art.grid(column=0, row=10, sticky=tk.W)
            form.art.grid(column=0, row=11, sticky=tk.W)
            
            form.addWidget(
                'nr',
                ttk.Entry(self.frmVAEinzelDaten, width=6),
                'text',
                label='Nr')
            form.lbl_nr.grid(column=1, row=10, sticky=tk.W)
            form.nr.grid(column=1, row=11, sticky=tk.W)
            
            ttk.Label(self.frmVAEinzelDaten, text='TN').grid(column=2, row=11, sticky=tk.W)
            form.addWidget(
                'tn_min',
                ttk.Entry(
                    self.frmVAEinzelDaten,
                    width=6,
                    justify='right',
                    validate='key',
                    validatecommand=(self.valInt, '%P')
                    ),
                'int',
                label='min')
            form.lbl_tn_min.grid(column=2, row=20, sticky=tk.W)
            form.tn_min.grid(column=2, row=21, sticky=tk.W)
            
            form.addWidget(
                'tn_max',
                ttk.Entry(
                    self.frmVAEinzelDaten,
                    width=6,
                    justify='right',
                    validate='key',
                    validatecommand=(self.valInt, '%P')
                    ),
                'int',
                label='max')
            form.lbl_tn_max.grid(column=3, row=20, sticky=tk.W)
            form.tn_max.grid(column=3, row=21, sticky=tk.W)
            
            ttk.Label(self.frmVAEinzelDaten, text='Alter').grid(column=4, row=11, sticky=tk.W)
            form.addWidget(
                'alter_min',
                ttk.Entry(
                    self.frmVAEinzelDaten,
                    width=6,
                    justify='right',
                    validate='key',
                    validatecommand=(self.valInt, '%P')
                    ),
                'int',
                label='min')
            form.lbl_alter_min.grid(column=4, row=20, sticky=tk.W)
            form.alter_min.grid(column=4, row=21, sticky=tk.W)
            
            form.addWidget(
                'alter_max',
                ttk.Entry(
                    self.frmVAEinzelDaten,
                    width=6,
                    justify='right',
                    validate='key',
                    validatecommand=(self.valInt, '%P')
                    ),
                'int',
                label='max')
            form.lbl_alter_max.grid(column=5, row=20, sticky=tk.W)
            form.alter_max.grid(column=5, row=21, sticky=tk.W)
            
            form.addWidget(
                'titel',
                ttk.Entry(self.frmVAEinzelDaten, width=40),
                'text',
                label='Titel')
            form.lbl_titel.grid(column=0, row=20, columnspan=2, sticky=tk.W)
            form.titel.grid(column=0, row=21, columnspan=2, sticky=tk.W)
            
            form.addWidget(
                'untertitel',
                ttk.Entry(self.frmVAEinzelDaten, width=40),
                'text',
                label='Untertitel')
            form.lbl_untertitel.grid(column=0, row=30, columnspan=2, sticky=tk.W)
            form.untertitel.grid(column=0, row=31, columnspan=2, sticky=tk.W)
            
            form.addWidget(
                'sprachen',
                ttk.Entry(self.frmVAEinzelDaten),
                'text',
                label='Sprachen')
            form.lbl_sprachen.grid(column=2, row=30, columnspan=4, sticky=tk.W)
            form.sprachen.grid(column=2, row=31, columnspan=4, sticky=tk.W)
            
            form.addWidget(
                'beschreibung',
                scrolledtext.ScrolledText(self.frmVAEinzelDaten, width=40, height=6),
                'text',
                label=ttk.Label(self.frmVAEinzelDaten, text='Beschreibung'))
            form.lbl_beschreibung.grid(column=0, row=40, columnspan=2, sticky=tk.W)
            form.beschreibung.grid(column=0, row=41, columnspan=2, sticky=tk.W)
            
            form.addWidget(
                'bedingungen',
                scrolledtext.ScrolledText(self.frmVAEinzelDaten, width=40, height=6),
                'text',
                label=ttk.Label(self.frmVAEinzelDaten, text='Bedingungen'))
            form.lbl_bedingungen.grid(column=2, row=40, columnspan=4, sticky=tk.W)
            form.bedingungen.grid(column=2, row=41, columnspan=4, sticky=tk.W)
            
            form.addWidget(
                'anmeldepflicht',
                ttk.Checkbutton(self.frmVAEinzelDaten),
                'bool',
                label='Anm.-Pflicht')
            form.lbl_anmeldepflicht.grid(column=0, row=50, sticky=tk.W)
            form.anmeldepflicht.grid(column=0, row=51, sticky=tk.W)
            
            form.addWidget(
                'honorar',
                ttk.Entry(
                    self.frmVAEinzelDaten,
                    width=6,
                    justify='right',
                    validate='key',
                    validatecommand=(self.valInt, '%P')
                    ),
                'int',
                label='Honorar')
            form.lbl_honorar.grid(column=2, row=50, columnspan=2, sticky=tk.W)
            form.honorar.grid(column=2, row=51, columnspan=2, sticky=tk.W)
            
            form.addWidget(
                'sachkosten',
                ttk.Entry(
                    self.frmVAEinzelDaten,
                    width=6,
                    justify='right',
                    validate='key',
                    validatecommand=(self.valInt, '%P')
                    ),
                'int',
                label='Sachkosten')
            form.lbl_sachkosten.grid(column=4, row=50, columnspan=2, sticky=tk.W)
            form.sachkosten.grid(column=4, row=51, columnspan=2, sticky=tk.W)
            
            form.addWidget(
                'bemerkung',
                scrolledtext.ScrolledText(self.frmVAEinzelDaten, width=60, height=6),
                'text',
                label=ttk.Label(self.frmVAEinzelDaten, text='Bemerkung'))
            form.lbl_bemerkung.grid(column=0, row=60, columnspan=6, sticky=tk.W)
            form.bemerkung.grid(column=0, row=61, columnspan=6, sticky=tk.W)
            
            bearbVonAm = BearbVonAm(self.frmVAEinzelDaten)
            bearbVonAm.grid(column=0, row=70, columnspan=6, sticky=tk.W)
            bearbVonAm.connectToForm(form)
            
        #
        # Gruppen
        with Form() as form:
            glb.formGruppen = form
            #
            # Frames für Navi und Formular bauen und in PanedWindow einsetzen
            self.frmGruppenNavi = ttk.Frame(self.frmGruppenEinzelheiten)
            self.frmGruppenDaten = ttk.Frame(self.frmGruppenEinzelheiten)
            self.frmGruppenEinzelheiten.add(self.frmGruppenNavi)
            self.frmGruppenEinzelheiten.add(self.frmGruppenDaten)
            #
            # Navi herstellen und einsetzen
            navi = NaviForm(self.frmGruppenNavi)
            form.setNavi(navi)
            navi.pack(fill=tk.BOTH, expand=True)
            #
            # Navi konfigurieren
            navi.connectToModell(
                Gruppe,
                selects=('farbe',),
                keyFeldNavi='id',
                labelFelder=('kurz_bez', 'bez'),
                filterFelder=('kurz_bez', 'bez'),
                Sort='kurz_bez')
            #
            # Widgets herstellen, zeigen und in Formular aufnehmen
            form.addWidget(
                'id',
                ttk.Entry(self.frmGruppenDaten, state=tk.DISABLED),
                'int',
                label='ID')
            form.lbl_id.grid(column=0, row=0, sticky=tk.E)
            form.id.grid(column=1, row=0, sticky=tk.W)
            
            form.addWidget(
                'kurz_bez',
                ttk.Entry(self.frmGruppenDaten),
                'text',
                label='Kurz.-Bez.')
            form.lbl_kurz_bez.grid(column=0, row=1, sticky=tk.E)
            form.kurz_bez.grid(column=1, row=1, sticky=tk.W)
            
            form.addWidget(
                'bez',
                ttk.Entry(self.frmGruppenDaten),
                'text',
                label='Bezeichnung')
            form.lbl_bez.grid(column=0, row=2, sticky=tk.E)
            form.bez.grid(column=1, row=2, sticky=tk.W)
            
            form.addWidget(
                'farbe',
                ttk.Combobox(self.frmGruppenDaten),
                'text',
                label='Farbe')
            form.lbl_farbe.grid(column=0, row=3, sticky=tk.E)
            form.farbe.grid(column=1, row=3, sticky=tk.W)
            
            form.addWidget(
                'bemerkung',
                scrolledtext.ScrolledText(self.frmGruppenDaten, width=25, height=5),
                'text',
                label=ttk.Label(self.frmGruppenDaten, text='Bemerkung'))
            form.lbl_bemerkung.grid(column=0, row=4, sticky=tk.E+tk.N)
            form.bemerkung.grid(column=1, row=4, sticky=tk.W)
            
            bearbVonAm = BearbVonAm(self.frmGruppenDaten)
            bearbVonAm.grid(column=0, row=5, columnspan=2, sticky=tk.W)
            bearbVonAm.connectToForm(form)
        #
        # Mail Arten
        with Form() as form:
            glb.formMailart = form
            #
            # Frames für Navi und Formular bauen und in PanedWindow einsetzen
            self.frmMailartNavi = ttk.Frame(self.frmMailartEinzelheiten)
            self.frmMailartDaten = ttk.Frame(self.frmMailartEinzelheiten)
            self.frmMailartEinzelheiten.add(self.frmMailartNavi)
            self.frmMailartEinzelheiten.add(self.frmMailartDaten)
            #
            # Navi herstellen und einsetzen
            navi = NaviForm(self.frmMailartNavi)
            form.setNavi(navi)
            navi.pack(fill=tk.BOTH, expand=True)
            #
            # Navi konfigurieren
            navi.connectToModell(
                Mailart,
                keyFeldNavi='id',
                labelFelder=('kurz_bez', 'bez'),
                filterFelder=('kurz_bez', 'bez'),
                Sort='kurz_bez')
            #
            # Widgets herstellen, zeigen und in Formular aufnehmen
            form.addWidget(
                'id',
                ttk.Entry(self.frmMailartDaten, state=tk.DISABLED),
                'int',
                label='ID')
            form.lbl_id.grid(column=0, row=0, sticky=tk.E)
            form.id.grid(column=1, row=0, sticky=tk.W)
            
            form.addWidget(
                'kurz_bez',
                ttk.Entry(self.frmMailartDaten),
                'text',
                label='Kurz.-Bez.')
            form.lbl_kurz_bez.grid(column=0, row=1, sticky=tk.E)
            form.kurz_bez.grid(column=1, row=1, sticky=tk.W)
            
            form.addWidget(
                'bez',
                ttk.Entry(self.frmMailartDaten, width=40),
                'text',
                label='Bezeichnung')
            form.lbl_bez.grid(column=0, row=2, sticky=tk.E)
            form.bez.grid(column=1, row=2, sticky=tk.W)
            
            form.addWidget(
                'bemerkung',
                scrolledtext.ScrolledText(self.frmMailartDaten, width=60, height=5),
                'text',
                label=ttk.Label(self.frmMailartDaten, text='Bemerkung'))
            form.lbl_bemerkung.grid(column=0, row=4, sticky=tk.E+tk.N)
            form.bemerkung.grid(column=1, row=4, sticky=tk.W)
            
            bearbVonAm = BearbVonAm(self.frmMailartDaten)
            bearbVonAm.grid(column=0, row=5, columnspan=2, sticky=tk.W)
            bearbVonAm.connectToForm(form)
        #
        # Raum Arten
        with Form() as form:
            glb.formRaumart = form
            #
            # Frames für Navi und Formular bauen und in PanedWindow einsetzen
            self.frmRaumartNavi = ttk.Frame(self.frmRaumartEinzelheiten)
            self.frmRaumartDaten = ttk.Frame(self.frmRaumartEinzelheiten)
            self.frmRaumartEinzelheiten.add(self.frmRaumartNavi)
            self.frmRaumartEinzelheiten.add(self.frmRaumartDaten)
            #
            # Navi herstellen und einsetzen
            navi = NaviForm(self.frmRaumartNavi)
            form.setNavi(navi)
            navi.pack(fill=tk.BOTH, expand=True)
            #
            # Navi konfigurieren
            navi.connectToModell(
                Raumart,
                keyFeldNavi='id',
                labelFelder= ('kurz_bez', 'beschreibung'),
                filterFelder=('kurz_bez', 'beschreibung'),
                Sort='kurz_bez')
            #
            # Widgets herstellen, zeigen und in Formular aufnehmen
            form.addWidget(
                'id',
                ttk.Entry(self.frmRaumartDaten, state=tk.DISABLED),
                'int',
                label='ID')
            form.lbl_id.grid(column=0, row=0, sticky=tk.E)
            form.id.grid(column=1, row=0, sticky=tk.W)
            
            form.addWidget(
                'kurz_bez',
                ttk.Entry(self.frmRaumartDaten),
                'text',
                label='Kurz.-Bez.')
            form.lbl_kurz_bez.grid(column=0, row=1, sticky=tk.E)
            form.kurz_bez.grid(column=1, row=1, sticky=tk.W)
            
            form.addWidget(
                'beschreibung',
                ttk.Entry(self.frmRaumartDaten, width=40),
                'text',
                label='Bezeichnung')
            form.lbl_beschreibung.grid(column=0, row=2, sticky=tk.E)
            form.beschreibung.grid(column=1, row=2, sticky=tk.W)
            
            form.addWidget(
                'bemerkung',
                scrolledtext.ScrolledText(self.frmRaumartDaten, width=60, height=5),
                'text',
                label=ttk.Label(self.frmRaumartDaten, text='Bemerkung'))
            form.lbl_bemerkung.grid(column=0, row=4, sticky=tk.E+tk.N)
            form.bemerkung.grid(column=1, row=4, sticky=tk.W)
            
            bearbVonAm = BearbVonAm(self.frmRaumartDaten)
            bearbVonAm.grid(column=0, row=5, columnspan=2, sticky=tk.W)
            bearbVonAm.connectToForm(form)
        #
        # Veranstaltung Arten
        with Form() as form:
            glb.formVeranstaltungart = form
            #
            # Frames für Navi und Formular bauen und in PanedWindow einsetzen
            self.frmVeranstaltungartNavi = ttk.Frame(self.frmVeranstaltungartEinzelheiten)
            self.frmVeranstaltungartDaten = ttk.Frame(self.frmVeranstaltungartEinzelheiten)
            self.frmVeranstaltungartEinzelheiten.add(self.frmVeranstaltungartNavi)
            self.frmVeranstaltungartEinzelheiten.add(self.frmVeranstaltungartDaten)
            #
            # Navi herstellen und einsetzen
            navi = NaviForm(self.frmVeranstaltungartNavi)
            form.setNavi(navi)
            navi.pack(fill=tk.BOTH, expand=True)
            #
            # Navi konfigurieren
            navi.connectToModell(
                Veranstaltungart,
                keyFeldNavi='id',
                labelFelder= ('kurz_bez', 'beschreibung'),
                filterFelder=('kurz_bez', 'beschreibung'),
                Sort='kurz_bez')
            #
            # Widgets herstellen, zeigen und in Formular aufnehmen
            form.addWidget(
                'id',
                ttk.Entry(self.frmVeranstaltungartDaten, state=tk.DISABLED),
                'int',
                label='ID')
            form.lbl_id.grid(column=0, row=0, sticky=tk.E)
            form.id.grid(column=1, row=0, sticky=tk.W)
            
            form.addWidget(
                'kurz_bez',
                ttk.Entry(self.frmVeranstaltungartDaten),
                'text',
                label='Kurz.-Bez.')
            form.lbl_kurz_bez.grid(column=0, row=1, sticky=tk.E)
            form.kurz_bez.grid(column=1, row=1, sticky=tk.W)
            
            form.addWidget(
                'beschreibung',
                ttk.Entry(self.frmVeranstaltungartDaten, width=40),
                'text',
                label='Bezeichnung')
            form.lbl_beschreibung.grid(column=0, row=2, sticky=tk.E)
            form.beschreibung.grid(column=1, row=2, sticky=tk.W)
            
            form.addWidget(
                'bemerkung',
                scrolledtext.ScrolledText(self.frmVeranstaltungartDaten, width=60, height=5),
                'text',
                label=ttk.Label(self.frmVeranstaltungartDaten, text='Bemerkung'))
            form.lbl_bemerkung.grid(column=0, row=4, sticky=tk.E+tk.N)
            form.bemerkung.grid(column=1, row=4, sticky=tk.W)
            
            bearbVonAm = BearbVonAm(self.frmVeranstaltungartDaten)
            bearbVonAm.grid(column=0, row=5, columnspan=2, sticky=tk.W)
            bearbVonAm.connectToForm(form)
        #
        # Gruppen als Liste
        def FactoryGruppeListe():
            form = Form()
            #
            # Navi herstellen und einsetzen
            navi = NaviForm(self.frmGruppenListeInhalt.innerFrame, elemente=('save', 'delete'))
            form.setNavi(navi)
            #
            # Navi konfigurieren
            navi.connectToModell(
                GruppeListe,
                selects=('farbe',))
            #
            # Widgets
            form.addWidget(
                'id',
                ttk.Entry(self.frmGruppenListeInhalt.innerFrame, state=tk.DISABLED, width=6),
                'int',
                label='ID')
            form.addWidget(
                'kurz_bez',
                ttk.Entry(self.frmGruppenListeInhalt.innerFrame, width=10),
                'text',
                label='Kurz.-Bez.')
            form.addWidget(
                'bez',
                ttk.Entry(self.frmGruppenListeInhalt.innerFrame, width=20),
                'text',
                label='Bezeichnung')
            form.addWidget(
                'farbe',
                ttk.Combobox(self.frmGruppenListeInhalt.innerFrame, width=10),
                'text',
                label='Farbe')
            #
            # Formular zurückgeben
            return form
                
        with FormListe(self.frmGruppenListeInhalt.innerFrame, FactoryGruppeListe) as form:
            glb.formGruppenListe = form
            #
            # Navi herstellen und einsetzen
            navi = NaviListe(self.frmGruppenListeNavi)
            form.setNavi(navi)
            #
            # Navi konfigurieren
            G = GruppeListe()
            navi.setGetterDicts(G.FactoryGetterDicts(FilterFelder=('kurz_bez', 'bez'), Sort='kurz_bez'))
            #
            # Form Navi packen
            form.getNavi().pack(anchor=tk.W)
        #
        # Farben
        with Form() as form:
            glb.formFarben = form
            #
            # Frames für Navi und Formular bauen und in PanedWindow einsetzen
            self.frmFarbenNavi = ttk.Frame(self.frmFarben)
            self.frmFarbenDaten = ttk.Frame(self.frmFarben)
            self.frmFarben.add(self.frmFarbenNavi)
            self.frmFarben.add(self.frmFarbenDaten)
            #
            # Navi herstellen und einsetzen
            navi = NaviForm(self.frmFarbenNavi)
            form.setNavi(navi)
            navi.pack(fill=tk.BOTH, expand=True)
            #
            # Navi konfigurieren
            navi.connectToModell(
                Farbe,
                keyFeldNavi='id',
                labelFelder=('farbe',),
                filterFelder=('farbe',),
                Sort='farbe')
            #
            # Widgets herstellen, zeigen und in Formular aufnehmen
            form.addWidget(
                'id',
                ttk.Entry(self.frmFarbenDaten, state=tk.DISABLED),
                'int',
                label='ID')
            form.lbl_id.grid(column=0, row=0, sticky=tk.E)
            form.id.grid(column=1, row=0, sticky=tk.W)
            
            form.addWidget(
                'farbe',
                ttk.Entry(self.frmFarbenDaten),
                'text',
                label='Farbe')
            form.lbl_farbe.grid(column=0, row=1, sticky=tk.E)
            form.farbe.grid(column=1, row=1, sticky=tk.W)
            
            bearbVonAm = BearbVonAm(self.frmFarbenDaten)
            bearbVonAm.grid(column=0, row=2, columnspan=2, sticky=tk.W)
            bearbVonAm.connectToForm(form)
            #
            # Info-Widget zu Farben herstellen und zeigen
            infoText = 'Nur Farben aus dem x11names Bereich, s. z.B.\n'
            urlText = 'https://ctan.math.washington.edu/tex-archive/macros/latex/contrib/xcolor/xcolor.pdf'
            wdg = scrolledtext.ScrolledText(
                self.frmFarbenDaten,
                width=70,
                height=4)
            wdg.insert('0.0', urlText)
            wdg.insert('0.0', infoText)
            ttk.Label(self.frmFarbenDaten, text='Info').grid(column=3, row=0, sticky=tk.W)
            wdg.grid(column=3, row=1, rowspan=2, sticky=tk.W)
            wdg.config(state=tk.DISABLED)
            
        #
        # Länder als Liste
        def FactoryLaenderListe():
            form = Form()
            #
            # Navi herstellen und einsetzen
            navi = NaviForm(self.frmLaenderListeInhalt.innerFrame, elemente=('save', 'delete'))
            form.setNavi(navi)
            #
            # Navi konfigurieren
            navi.connectToModell(Laender)
            #
            # Widgets
            form.addWidget(
                'id',
                ttk.Entry(self.frmLaenderListeInhalt.innerFrame, state=tk.DISABLED, width=6),
                'int',
                label='ID')
            form.addWidget(
                'land',
                ttk.Entry(self.frmLaenderListeInhalt.innerFrame, width=40),
                'text',
                label='Land')
            form.addWidget(
                'land_kurz',
                ttk.Entry(self.frmLaenderListeInhalt.innerFrame, width=5),
                'text',
                label='Kurz')
            Tooltip(form.land_kurz, 'Ländercode nach\nhttps://de.wikipedia.org/wiki/ISO-3166-1-Kodierliste')
            form.addWidget(
                'prototyp',
                ttk.Checkbutton(self.frmLaenderListeInhalt.innerFrame),
                'bool',
                label='Prototyp')
            Tooltip(form.prototyp, 'Genau ein Ländereintrag\nmit gleicher Kurz-Bez\nmuss Prototyp sein.')
            #
            # Formular zurückgeben
            return form
                
        with FormListe(self.frmLaenderListeInhalt.innerFrame, FactoryLaenderListe) as form:
            glb.formLaenderListe = form
            #
            # Navi herstellen und einsetzen
            navi = NaviListe(self.frmLaenderListeNavi)
            form.setNavi(navi)
            #
            # Navi konfigurieren
            L = Laender()
            navi.setGetterDicts(L.FactoryGetterDicts(
                      FilterFelder=('land', 'land_kurz'),
                      Sort='land_kurz, land'))
            #
            # Form Navi packen
            form.getNavi().pack(anchor=tk.W)
        #
        # Tagungen
        with Form() as form:
            glb.formTagungen = form
            #
            # Frames für Navi und Formular bauen und in PanedWindow einsetzen
            self.frmTagungenNavi = ttk.Frame(self.frmTagungenEinzelheiten)
            self.frmTagungenDaten = ttk.Frame(self.frmTagungenEinzelheiten)
            self.frmTagungenEinzelheiten.add(self.frmTagungenNavi)
            self.frmTagungenEinzelheiten.add(self.frmTagungenDaten)
            #
            # Navi herstellen und einsetzen
            navi = NaviForm(self.frmTagungenNavi)
            form.setNavi(navi)
            navi.pack(fill=tk.BOTH, expand=True)
            #
            # Navi konfigurieren
            navi.connectToModell(
                Tagung,
                keyFeldNavi='id',
                labelFelder=('kurz_bez',),
                filterFelder=('kurz_bez',),
                Sort='kurz_bez')
            #
            # Widgets herstellen, zeigen und in Formular aufnehmen
            form.addWidget(
                'id',
                ttk.Entry(self.frmTagungenDaten, state=tk.DISABLED, width=6),
                'int',
                label='ID')
            form.lbl_id.grid(column=0, row=0, sticky=tk.W)
            form.id.grid(column=0, row=1, sticky=tk.W)
            
            form.addWidget(
                'aktiv',
                ttk.Checkbutton(self.frmTagungenDaten),
                'bool',
                label='Aktiv')
            form.lbl_aktiv.grid(column=1, row=0, sticky=tk.W)
            form.aktiv.grid(column=1, row=1, sticky=tk.W)
            
            form.addWidget(
                'kurz_bez',
                ttk.Entry(self.frmTagungenDaten, width=40),
                'text',
                label='Kurz-Bez.')
            form.lbl_kurz_bez.grid(column=0, row=2, sticky=tk.W)
            form.kurz_bez.grid(column=0, row=3, sticky=tk.W)
            
            form.addWidget(
                'titel',
                ttk.Entry(self.frmTagungenDaten),
                'text',
                label='Titel'
                )
            form.lbl_titel.grid(column=1, row=2, sticky=tk.W)
            form.titel.grid(column=1, row=3, sticky=tk.W)
            
            form.addWidget(
                'beschreibung',
                ttk.Entry(self.frmTagungenDaten),
                'text',
                label='Beschreibung'
                )
            form.lbl_beschreibung.grid(column=2, row=2, stick=tk.W)
            form.beschreibung.grid(column=2, row=3, sticky=tk.W)
            
            form.addWidget(
                'dat_beginn',
                ttk.Entry(
                    self.frmTagungenDaten,
                    width=15,
                    validate='focusout',
                    validatecommand=(self.valDate, '%P'),
                    invalidcommand=(self.invalidHoldFocus, '%W')
                    ),
                'date',
                label='Beginn'
                )
            form.lbl_dat_beginn.grid(column=0, row=4, sticky=tk.W)
            form.dat_beginn.grid(column=0, row=5, sticky=tk.W)
            
            form.addWidget(
                'dat_ende',
                ttk.Entry(
                    self.frmTagungenDaten,
                    width=15,
                    validate='focusout',
                    validatecommand=(self.valDate, '%P'),
                    invalidcommand=(self.invalidHoldFocus, '%W')
                    ),
                'date',
                label='Ende'
                )
            form.lbl_dat_ende.grid(column=1, row=4, sticky=tk.W)
            form.dat_ende.grid(column=1, row=5, sticky=tk.W)
            
            form.addWidget(
                'ort',
                ttk.Entry(self.frmTagungenDaten),
                'text',
                label='Ort'
                )
            form.lbl_ort.grid(column=2, row=4, sticky=tk.W)
            form.ort.grid(column=2, row=5, sticky=tk.W)
            
            form.addWidget(
                'mail_from',
                ttk.Entry(self.frmTagungenDaten),
                'text',
                label='Mail From')
            form.lbl_mail_from.grid(column=0, row=8, columnspan=2, sticky=tk.W)
            form.mail_from.grid(column=0, row=9, columnspan=2, sticky=tk.W)
            
            form.addWidget(
                'mail_reply',
                ttk.Entry(self.frmTagungenDaten),
                'text',
                label='Mail Reply')
            form.lbl_mail_reply.grid(column=2, row=8, sticky=tk.W)
            form.mail_reply.grid(column=2, row=9, sticky=tk.W)
            
            form.addWidget(
                'rel_verz',
                ttk.Entry(self.frmTagungenDaten),
                'text',
                label='Rel. Verz.')
            form.lbl_rel_verz.grid(column=0, row=10, columnspan=2, sticky=tk.W)
            form.rel_verz.grid(column=0, row=11, columnspan=2, sticky=tk.W)
            
            form.addWidget(
                'schema',
                ttk.Entry(self.frmTagungenDaten),
                'text',
                label='DB Schema')
            form.lbl_schema.grid(column=2, row=10, sticky=tk.W)
            form.schema.grid(column=2, row=11, sticky=tk.W)
            
            bearbVonAm = BearbVonAm(self.frmTagungenDaten)
            bearbVonAm.grid(column=0, row=12, columnspan=3, sticky=tk.W)
            bearbVonAm.connectToForm(form)
        #
        # Mails
        with Form() as form:
            glb.formMails = form
            #
            # Frames für Navi und Formular bauen und in PanedWindow einsetzen
            self.frmMailsNavi = ttk.Frame(self.frmMails)
            self.frmMailsDaten = ttk.Frame(self.frmMails)
            self.frmMails.add(self.frmMailsNavi)
            self.frmMails.add(self.frmMailsDaten)
            #
            # Navi herstellen und einsetzen
            navi = NaviForm(self.frmMailsNavi)
            form.setNavi(navi)
            navi.pack(fill=tk.BOTH, expand=True)
            #
            # Navi konfigurieren
            navi.connectToModell(
                Mail,
                selects=('art',),
                keyFeldNavi='id',
                labelFelder=('art', 'aktuell', 'id',),
                filterFelder=('art', 'betreff',),
                Sort='art, aktuell desc, id')
            #
            # Widgets herstellen, zeigen und in Formular aufnehmen
            form.addWidget(
                'id',
                ttk.Entry(self.frmMailsDaten, state=tk.DISABLED, width=6),
                'int',
                label='ID')
            form.lbl_id.grid(column=0, row=0, sticky=tk.W)
            form.id.grid(column=0, row=1, sticky=tk.W)
            
            form.addWidget(
                'art',
                ComboboxValueLabel(
                      self.frmMailsDaten,
                      width=15),
                'text',
                label='Mail-Art')
            form.lbl_art.grid(column=0, row=2, sticky=tk.W)
            form.art.grid(column=0, row=3, sticky=tk.W)
            
            form.addWidget(
                'aktuell',
                ttk.Checkbutton(self.frmMailsDaten),
                'bool',
                label='Aktuell')
            Tooltip(form.aktuell, 'Nur eine Mail\nder gleichen Art\ndarf und muss als\naktuell markiert sein')
            form.lbl_aktuell.grid(column=1, row=2, sticky=tk.W)
            form.aktuell.grid(column=1, row=3, sticky=tk.W)
            
            mailsWidth = 25
            mailsHeight = 8
            
            form.addWidget(
                'betreff',
                ttk.Entry(self.frmMailsDaten, width=2*mailsWidth),
                'text',
                label='Betreff')
            form.lbl_betreff.grid(column=0, row=4, columnspan=2, sticky=tk.W)
            form.betreff.grid(column=0, row=5, columnspan=2, sticky=tk.W)
            
            form.addWidget(
                'text_vj',
                scrolledtext.ScrolledText(
                    self.frmMailsDaten,
                    width=mailsWidth,
                    height=mailsHeight),
                'text',
                label=ttk.Label(self.frmMailsDaten, text='Text: Volljährige'))
            Tooltip(form.text_vj, 'Text (ohne Anrede)\nfür volljährige TN')
            form.lbl_text_vj.grid(column=0, row=6, sticky=tk.W)
            form.text_vj.grid(column=0, row=7, sticky=tk.W)
            
            form.addWidget(
                'text_mj',
                scrolledtext.ScrolledText(
                    self.frmMailsDaten,
                    width=mailsWidth,
                    height=mailsHeight),
                'text',
                label=ttk.Label(self.frmMailsDaten, text='Text: Minderjährige'))
            Tooltip(form.text_mj, 'Text (ohne Anrede)\nfür minderjährige TN')
            form.lbl_text_mj.grid(column=1, row=6, sticky=tk.W)
            form.text_mj.grid(column=1, row=7, sticky=tk.W)
            
            form.addWidget(
                'text_kf',
                scrolledtext.ScrolledText(
                    self.frmMailsDaten,
                    width=mailsWidth,
                    height=mailsHeight),
                'text',
                label=ttk.Label(self.frmMailsDaten, text='Text: Ki-Tagung'))
            Tooltip(form.text_kf, 'Text (ohne Anrede)\nTN der Kinder-Tagung')
            form.lbl_text_kf.grid(column=2, row=6, sticky=tk.W)
            form.text_kf.grid(column=2, row=7, sticky=tk.W)
            
            form.addWidget(
                'text_kb',
                scrolledtext.ScrolledText(
                    self.frmMailsDaten,
                    width=mailsWidth,
                    height=mailsHeight),
                'text',
                label=ttk.Label(self.frmMailsDaten, text='Text: Ki-Betreuung'))
            Tooltip(form.text_kb, 'Text (ohne Anrede)\nTN der Kinder-Betreuung')
            form.lbl_text_kb.grid(column=3, row=6, sticky=tk.W)
            form.text_kb.grid(column=3, row=7, sticky=tk.W)
            
            form.addWidget(
                'anhang_vj',
                ttk.Entry(self.frmMailsDaten, width=mailsWidth),
                'text',
                label='Anhang: Volljährige')
            Tooltip(form.anhang_vj, 'Anhang für volljährige TN,\ni.d.R. leer')
            form.lbl_anhang_vj.grid(column=0, row=8, sticky=tk.W)
            form.anhang_vj.grid(column=0, row=9, sticky=tk.W)
            
            form.addWidget(
                'anhang_mj',
                ttk.Entry(self.frmMailsDaten, width=mailsWidth),
                'text',
                label='Anhang: Minderjährige')
            Tooltip(form.anhang_mj, 'Anhang für minderjährige TN,\ni.d.R. Einverständniserklärung')
            form.lbl_anhang_mj.grid(column=1, row=8, sticky=tk.W)
            form.anhang_mj.grid(column=1, row=9, sticky=tk.W)
            
            form.addWidget(
                'anhang_kf',
                ttk.Entry(self.frmMailsDaten, width=mailsWidth),
                'text',
                label='Anhang: Ki-Tagung')
            Tooltip(form.anhang_kf, 'Anhang für TN Kinder-Tagung,\ni.d.R. leer')
            form.lbl_anhang_kf.grid(column=2, row=8, sticky=tk.W)
            form.anhang_kf.grid(column=2, row=9, sticky=tk.W)
            
            form.addWidget(
                'anhang_kb',
                ttk.Entry(self.frmMailsDaten, width=mailsWidth),
                'text',
                label='Anhang: Ki-Betreuung')
            Tooltip(form.anhang_kb, 'Anhang für TN Kinder-Betreuung,\ni.d.R. leer')
            form.lbl_anhang_kb.grid(column=3, row=8, sticky=tk.W)
            form.anhang_kb.grid(column=3, row=9, sticky=tk.W)
            
            form.addWidget(
                'bemerkung',
                scrolledtext.ScrolledText(
                    self.frmMailsDaten,
                    width=2*mailsWidth,
                    height=mailsHeight),
                'text',
                label=ttk.Label(self.frmMailsDaten, text='Bemerkung'))
            Tooltip(form.bemerkung, 'Bemerkung des TB,\nwird nicht mit verschickt.')
            form.lbl_bemerkung.grid(column=0, row=10, columnspan=2, sticky=tk.W)
            form.bemerkung.grid(column=0, row=11, columnspan=2, sticky=tk.W)
            
            bearbVonAm = BearbVonAm(self.frmMailsDaten)
            bearbVonAm.grid(column=0, row=12, columnspan=3, sticky=tk.W)
            bearbVonAm.connectToForm(form)
        #
        # Jobs Einzelheiten
        with Form() as form:
            glb.formJobsEinzelheiten = form
            #
            # Frames für Navi und Formular bauen und in PanedWindow einsetzen
            self.frmJobsEinzelheitenNavi = ttk.Frame(self.frmJobsEinzelheiten)
            self.frmJobsEinzelheitenDaten = ttk.Frame(self.frmJobsEinzelheiten)
            
            self.frmJobsEinzelheiten.add(self.frmJobsEinzelheitenNavi)
            self.frmJobsEinzelheiten.add(self.frmJobsEinzelheitenDaten)
            #
            # Navi herstellen und einsetzen
            navi = NaviForm(self.frmJobsEinzelheitenNavi)
            form.setNavi(navi)
            navi.pack(fill=tk.BOTH, expand=True)
            #
            # Navi konfigurieren
            navi.connectToModell(
                Jobs,
                keyFeldNavi='id',
                labelFelder=('titel',),
                filterFelder=('titel', 'kommando'),
                Sort='kommando')
            #
            # Widgets herstellen, zeigen und in Formular aufnehmen
            form.addWidget(
                'id',
                ttk.Entry(self.frmJobsEinzelheitenDaten, state=tk.DISABLED, width=6),
                'int',
                label='ID')
            form.lbl_id.grid(column=0, row=0, sticky=tk.W)
            form.id.grid(column=0, row=1, sticky=tk.W)
            
            form.addWidget(
                'titel',
                ttk.Entry(self.frmJobsEinzelheitenDaten, width=40),
                'text',
                label='Titel')
            form.lbl_titel.grid(column=0, row=2, columnspan=2, sticky=tk.W)
            form.titel.grid(column=0, row=3, columnspan=2, sticky=tk.W)
            
            form.addWidget(
                'kommando',
                ttk.Entry(self.frmJobsEinzelheitenDaten, width=40),
                'text',
                label='Kommando')
            form.lbl_kommando.grid(column=0, row=4, sticky=tk.W)
            form.kommando.grid(column=0, row=5, sticky=tk.W)
            
            form.addWidget(
                'verzeichnis',
                ttk.Entry(self.frmJobsEinzelheitenDaten, width=40),
                'text',
                label='Verzeichnis')
            form.lbl_verzeichnis.grid(column=2, row=4, sticky=tk.W)
            form.verzeichnis.grid(column=2, row=5, sticky=tk.W)
            
            form.addWidget(
                'beschreibung',
                ttk.Entry(self.frmJobsEinzelheitenDaten, width=80),
                'text',
                label='Beschreibung')
            form.lbl_beschreibung.grid(column=0, row=6, columnspan=3, sticky=tk.W)
            form.beschreibung.grid(column=0, row=7, columnspan=3, sticky=tk.W)
            
            form.addWidget(
                'intervall',
                ttk.Entry(
                      self.frmJobsEinzelheitenDaten,
                      width=4,
                      validate='key',
                      validatecommand=(self.valInt, '%P')
                      ),
                'int',
                label='Intervall')
            form.lbl_intervall.grid(column=0, row=8, sticky=tk.E)
            form.intervall.grid(column=0, row=9, sticky=tk.E)
            
            form.addWidget(
                'einheit',
                ComboboxValueLabel(
                      self.frmJobsEinzelheitenDaten,
                      width=12),
                'text',
                label='Einheit')
            form.getWidget('einheit').fill((
                ('mi', 'Minute(n)'),
                ('st', 'Stunde(n)'),
                ('ta', 'Tag(e)'),
                ('mo', 'Monat(e)')
                ))
            form.lbl_einheit.grid(column=1, row=8, sticky=tk.W)
            form.einheit.grid(column=1, row=9, sticky=tk.W)
            
            form.addWidget(
                'aktiv',
                ttk.Checkbutton(self.frmJobsEinzelheitenDaten),
                'bool',
                label='Aktiv')
            form.lbl_aktiv.grid(column=0, row=10, sticky=tk.E)
            form.aktiv.grid(column=1, row=10, sticky=tk.W)
                
            form.addWidget(
                'sofort',
                ttk.Checkbutton(self.frmJobsEinzelheitenDaten),
                'bool',
                label='Sofort')
            form.lbl_sofort.grid(column=0, row=11, sticky=tk.E)
            form.sofort.grid(column=1, row=11, sticky=tk.W)
                
            form.addWidget(
                'gestoppt',
                ttk.Checkbutton(self.frmJobsEinzelheitenDaten),
                'bool',
                label='Gestoppt')
            form.lbl_gestoppt.grid(column=0, row=12, sticky=tk.E)
            form.gestoppt.grid(column=1, row=12, sticky=tk.W)
                
            form.addWidget(
                'selbstzerstoerend',
                ttk.Checkbutton(self.frmJobsEinzelheitenDaten),
                'bool',
                label='Selbstzerstörend')
            form.lbl_selbstzerstoerend.grid(column=0, row=13, sticky=tk.E)
            form.selbstzerstoerend.grid(column=1, row=13, sticky=tk.W)
        #
        # Jobs Liste
        def FactoryJobsListe():
            form = Form()
            #
            # Navi herstellen und einsetzen
            navi = NaviForm(self.frmJobsListeInhalt.innerFrame, elemente=('save', 'delete'))
            form.setNavi(navi)
            #
            # Navi konfigurieren
            navi.connectToModell(JobsListe)
            #
            # Widgets
            form.addWidget(
                'id',
                ttk.Entry(self.frmJobsListeInhalt.innerFrame, state=tk.DISABLED, width=6),
                'int',
                label='ID')
            form.addWidget(
                'titel',
                ttk.Entry(self.frmJobsListeInhalt.innerFrame, width=30),
                'text',
                label='Titel')
            form.addWidget(
                'kommando',
                ttk.Entry(self.frmJobsListeInhalt.innerFrame, width=30),
                'text',
                label='Kommando')
            form.addWidget(
                'intervall',
                ttk.Entry(
                      self.frmJobsListeInhalt.innerFrame,
                      width=8,
                      validate='key',
                      validatecommand=(self.valInt, '%P')
                      ),
                'int',
                label='Interv.')
            form.addWidget(
                'einheit',
                ComboboxValueLabel(
                      self.frmJobsListeInhalt.innerFrame,
                      width=12),
                'text',
                label='Einheit')
            form.getWidget('einheit').fill((
                ('mi', 'Minute(n)'),
                ('st', 'Stunde(n)'),
                ('ta', 'Tag(e)'),
                ('mo', 'Monat(e)')
                ))
            form.addWidget(
                'aktiv',
                ttk.Checkbutton(self.frmJobsListeInhalt.innerFrame),
                'bool',
                label='Aktiv')
            form.addWidget(
                'sofort',
                ttk.Checkbutton(self.frmJobsListeInhalt.innerFrame),
                'bool',
                label='Sofort')
            form.addWidget(
                'gestoppt',
                ttk.Checkbutton(self.frmJobsListeInhalt.innerFrame),
                'bool',
                label='Gestoppt')
            #
            # Formular zurückgeben
            return form
        
        with FormListe(self.frmJobsListeInhalt.innerFrame, FactoryJobsListe) as form:
            glb.formGruppenListe = form
            #
            # Navi herstellen und einsetzen
            navi = NaviListe(self.frmJobsListeNavi)
            form.setNavi(navi)
            #
            # Navi konfigurieren
            J = JobsListe()
            navi.setGetterDicts(J.FactoryGetterDicts(
                    FilterFelder=('titel', 'kommando'),
                    Sort='kommando'))
            #
            # Form Navi packen
            form.getNavi().pack(anchor=tk.W)
        #
        # Status Liste
        def FactoryStatusListe():
            form = Form()
            #
            # Navi herstellen und einsetzen
            navi = NaviForm(self.frmStatusListeInhalt.innerFrame, elemente=('save', 'delete'))
            form.setNavi(navi)
            #
            # Navi konfigurieren
            navi.connectToModell(
                StatusListe,
                selects=('farbe', 'mail_art', 'nachfolge_status'))
            #
            # Widgets
            form.addWidget(
                'id',
                ttk.Entry(self.frmStatusListeInhalt.innerFrame, state=tk.DISABLED, width=6),
                'int',
                label='ID')
            form.addWidget(
                'kurz_bez',
                ttk.Entry(self.frmStatusListeInhalt.innerFrame, width=10),
                'text',
                label='Kurz-Bez.')
            form.addWidget(
                'bez',
                ttk.Entry(self.frmStatusListeInhalt.innerFrame, width=50),
                'text',
                label='Bezeichnung')
            form.addWidget(
                'farbe',
                ttk.Combobox(self.frmStatusListeInhalt.innerFrame, width=8),
                'text',
                label='Farbe')
            form.addWidget(
                'mail_ausloesen',
                ttk.Checkbutton(self.frmStatusListeInhalt.innerFrame),
                'bool',
                label='Mail auslösen')
            form.addWidget(
                'mail_art',
                ttk.Combobox(self.frmStatusListeInhalt.innerFrame, width=8),
                'text',
                label='Art')
            form.addWidget(
                'nachfolge_status',
                ttk.Combobox(self.frmStatusListeInhalt.innerFrame, width=18),
                'text',
                label='Nachfolge-Status')
            #
            # Formular zurückgeben
            return form
        
        with FormListe(self.frmStatusListeInhalt.innerFrame, FactoryStatusListe) as form:
            glb.formStatusListe = form
            #
            # Navi herstellen und einsetzen
            navi = NaviListe(self.frmStatusListeNavi)
            form.setNavi(navi)
            #
            # Navi konfigurieren
            S = StatusListe()
            navi.setGetterDicts(S.FactoryGetterDicts(
                    FilterFelder=('kurz_bez', 'bez'),
                    Sort='kurz_bez'))
            #
            # Form Navi packen
            form.getNavi().pack(anchor=tk.W)
            
    def disableMainNotebook(self):
        """disableMainNotebook - Deaktiviert alle Tabs des Main Notebook
        """
        for index in range(self.nbkMain.index(tk.END)):
            self.nbkMain.tab(index, stat=tk.DISABLED)
                        
    def enableMainNotebook(self):
        """enableMainNotebook - Aktiviert alle Tabs des Main Notebook
        """
        for index in range(self.nbkMain.index(tk.END)):
            self.nbkMain.tab(index, stat=tk.NORMAL)
                        
    def baueLayout(self):
        """baueLayout - Baut das Layout auf, in dem später die Widgets plaziert werden
        
            Notebook-Struktur:
            
                nbkMain
                    nbkPersonen
                        frmJugendEinzelheiten         Personen, relevante Felder für Jugend
                        frmPersonenStatus             Anmelde-Status der Personen
                        frmPersonenFinanzen           Personen: Finanzen
                        frmPersonenFinanzenListe      Personen: Finanzen, als Liste
                        frmAnmWS                      WS-Anm. zuordnen
                    nbkInstitutionen
                        frmInstitutionenJugend        Institutionen, relevante Felder für Jugend
                    nbkQuartier
                        frmQuartiere
                    nbkVeranstaltung
                        frmVeranstaltung
                        frmRaum
                    nbkHelferlein
                        frmGruppen
                        frmGruppenListe
                        frmMailartEinzelheiten
                        frmQuartierartEinzelheiten
                        frmRaumartEinzelheiten
                        frmVeranstaltungsartEinzelheiten
                    nbkVerwaltung
                        frmFarben
                        frmFarbenListe
                        frmTagungenEinzelheiten
                        frmLaenderListe
                        frmJobsListe
                        frmStatus
                        frmStatusListe
                        frmMail
        """
        #
        # Kopfleiste
        self.frmTop = ttk.Frame(self)
        self.frmTop.pack()
        #
        # Paned Window für Haupt und Fuß Frame
        self.pndHauptUndFuss = ttk.PanedWindow(self, orient=tk.VERTICAL)
        self.pndHauptUndFuss.pack(expand=tk.YES, fill=tk.BOTH)
        #
        # Haupt Frame
        self.frmMain = ttk.Frame(self.pndHauptUndFuss)
        self.pndHauptUndFuss.add(self.frmMain)
        #
        # Fuß Frame
        self.frmBottom = ttk.Frame(self.pndHauptUndFuss)
        self.pndHauptUndFuss.add(self.frmBottom)
        #
        # Haupt-Notebook
        self.nbkMain = ttk.Notebook(self.frmMain)
        self.nbkMain.pack(expand=tk.YES, fill=tk.BOTH)
        #
        # Unter-Notebooks
        self.frmNbkPersonen = ttk.Frame(self.frmMain)
        self.nbkMain.add(self.frmNbkPersonen, text='Personen')
        self.nbkPersonen = ttk.Notebook(self.frmNbkPersonen)
        self.nbkPersonen.pack(expand=tk.YES, fill=tk.BOTH)
        
        self.frmNbkInstitutionen = ttk.Frame(self.frmMain)
        self.nbkMain.add(self.frmNbkInstitutionen, text='Institutionen')
        self.nbkInstitutionen = ttk.Notebook(self.frmNbkInstitutionen)
        self.nbkInstitutionen.pack(expand=tk.YES, fill=tk.BOTH)
        
        self.frmNbkQuartiere = ttk.Frame(self.frmMain)
        self.nbkMain.add(self.frmNbkQuartiere, text='Quartiere')
        self.nbkQuartiere = ttk.Notebook(self.frmNbkQuartiere)
        self.nbkQuartiere.pack(expand=tk.YES, fill=tk.BOTH)
        
        self.frmNbkVeranstaltungen = ttk.Frame(self.frmMain)
        self.nbkMain.add(self.frmNbkVeranstaltungen, text='Veranstaltungen')
        self.nbkVeranstaltungen = ttk.Notebook(self.frmNbkVeranstaltungen)
        self.nbkVeranstaltungen.pack(expand=tk.YES, fill=tk.BOTH)
        
        self.frmNbkHelferlein = ttk.Frame(self.frmMain)
        self.nbkMain.add(self.frmNbkHelferlein, text='Helferlein')
        self.nbkHelferlein = ttk.Notebook(self.frmNbkHelferlein)
        self.nbkHelferlein.pack(expand=tk.YES, fill=tk.BOTH)
        
        self.frmNbkVerwaltung = ttk.Frame(self.frmMain)
        self.nbkMain.add(self.frmNbkVerwaltung, text='Verwaltung')
        self.nbkVerwaltung = ttk.Notebook(self.frmNbkVerwaltung)
        self.nbkVerwaltung.pack(expand=tk.YES, fill=tk.BOTH)
        
        self.frmNbkTagung = ttk.Frame(self.frmMain)
        self.nbkMain.add(self.frmNbkTagung, text='Tagungen')
        self.nbkTagung = ttk.Notebook(self.frmNbkTagung)
        self.nbkTagung.pack(expand=tk.YES, fill=tk.BOTH)
        #
        # Frames in Notebooks
        self.frmPersJuEinzel = ttk.Frame(self.frmNbkPersonen)
        self.nbkPersonen.add(self.frmPersJuEinzel, text='Jugend: Einzelheiten')
        
        self.frmPersonenStatusListe = ttk.Frame(self.frmNbkPersonen)
        self.nbkPersonen.add(self.frmPersonenStatusListe, text='Anm.-Status')
        self.frmPersonenStatusListeNavi = ttk.Frame(self.frmPersonenStatusListe)
        self.frmPersonenStatusListeInhalt = yScrolledFrame(self.frmPersonenStatusListe)
        self.frmPersonenStatusListeNavi.pack(
            side=tk.TOP,
            anchor=tk.W
            )
        self.frmPersonenStatusListeInhalt.pack(
            side=tk.TOP,
            expand=tk.YES,
            fill=tk.BOTH
            )
        
        self.frmWSAnmZuordnenListe = ttk.Frame(self.frmNbkPersonen)
        self.nbkPersonen.add(self.frmWSAnmZuordnenListe, text='WS-Anm.')
        ttk.Label(self.frmWSAnmZuordnenListe, text='WS-Anmeldungen').pack(
                    side=tk.TOP,
                    anchor=tk.W
                    )
        self.frmWSAnmZuordnenListeNavi = ttk.Frame(self.frmWSAnmZuordnenListe)
        self.frmWSAnmZuordnenListeInhalt = yScrolledFrame(self.frmWSAnmZuordnenListe)
        self.frmWSAnmZuordnenListeNavi.pack(
            side=tk.TOP,
            anchor=tk.W
            )
        self.frmWSAnmZuordnenListeInhalt.pack(
            side=tk.TOP,
            expand=tk.YES,
            fill=tk.BOTH
            )
        ttk.Label(self.frmWSAnmZuordnenListe, text='Personen').pack(
                    side=tk.TOP,
                    anchor=tk.W
                    )
        self.frmWSAnmZuordnenPersNavi = ttk.Frame(self.frmWSAnmZuordnenListe)
        self.frmWSAnmZuordnenPersInhalt = yScrolledFrame(self.frmWSAnmZuordnenListe)
        self.frmWSAnmZuordnenPersNavi.pack(
            side=tk.TOP,
            anchor=tk.W
            )
        self.frmWSAnmZuordnenPersInhalt.pack(
            side=tk.TOP,
            expand=tk.YES,
            fill=tk.BOTH
            )
        
        self.frmWSFestlegen = ttk.Frame(self.frmNbkPersonen)
        self.nbkPersonen.add(self.frmWSFestlegen, text='WS festlegen')
        self.frmWSFestlegenNavi = ttk.Frame(self.frmWSFestlegen)
        self.frmWSFestlegenInhalt = yScrolledFrame(self.frmWSFestlegen)
        self.frmWSFestlegenNavi.pack(
            side=tk.TOP,
            anchor=tk.W)
        self.frmWSFestlegenInhalt.pack(
            side=tk.TOP,
            expand=tk.YES,
            fill=tk.BOTH)
        
        self.frmPersonenFinanzenEinzel = ttk.Frame(self.frmNbkPersonen)
        self.nbkPersonen.add(self.frmPersonenFinanzenEinzel, text='Finanzen')
        
        self.frmPersonenFinanzenListe = ttk.Frame(self.frmNbkPersonen)
        self.nbkPersonen.add(self.frmPersonenFinanzenListe, text='Finanzen (Liste)')
        self.frmPersonenFinanzenListeNavi = ttk.Frame(self.frmPersonenFinanzenListe)
        self.frmPersonenFinanzenListeInhalt = yScrolledFrame(self.frmPersonenFinanzenListe)
        self.frmPersonenFinanzenListeNavi.pack(
            side=tk.TOP,
            anchor=tk.W
            )
        self.frmPersonenFinanzenListeInhalt.pack(
            side=tk.TOP,
            expand=tk.YES,
            fill=tk.BOTH
            )
        
        self.frmInstitutionenJugend = ttk.Frame(self.frmNbkInstitutionen)
        self.nbkInstitutionen.add(self.frmInstitutionenJugend, text='Jugend: Institutionen')
        
        self.frmVAEinzelheiten = ttk.PanedWindow(
            self.frmNbkVeranstaltungen,
            orient=tk.HORIZONTAL)
        self.nbkVeranstaltungen.add(self.frmVAEinzelheiten, text='VA Einzelheiten')
        
        self.frmGruppenEinzelheiten = ttk.PanedWindow(
            self.frmNbkHelferlein,
            orient=tk.HORIZONTAL)
        self.nbkHelferlein.add(self.frmGruppenEinzelheiten, text='Gruppen')
        
        self.frmGruppenListe = ttk.Frame(self.frmNbkHelferlein)
        self.nbkHelferlein.add(self.frmGruppenListe, text='Gruppen (Liste)')
        self.frmGruppenListeNavi = ttk.Frame(self.frmGruppenListe)
        self.frmGruppenListeInhalt = yScrolledFrame(self.frmGruppenListe)
        self.frmGruppenListeNavi.pack(
            side=tk.TOP,
            anchor=tk.W
            )
        self.frmGruppenListeInhalt.pack(
            side=tk.TOP,
            expand=tk.YES,
            fill=tk.BOTH
            )
        
        self.frmMailartEinzelheiten = ttk.PanedWindow(
            self.frmNbkHelferlein,
            orient=tk.HORIZONTAL)
        self.nbkHelferlein.add(self.frmMailartEinzelheiten, text='Mailarten')
        
        self.frmQuartierartEinzelheiten = ttk.PanedWindow(
            self.frmNbkHelferlein,
            orient=tk.HORIZONTAL)
        self.nbkHelferlein.add(self.frmQuartierartEinzelheiten, text='Quartierarten')
        
        self.frmRaumartEinzelheiten = ttk.PanedWindow(
            self.frmNbkHelferlein,
            orient=tk.HORIZONTAL)
        self.nbkHelferlein.add(self.frmRaumartEinzelheiten, text='Raumarten')
        
        self.frmVeranstaltungartEinzelheiten = ttk.PanedWindow(
            self.frmNbkHelferlein,
            orient=tk.HORIZONTAL)
        self.nbkHelferlein.add(self.frmVeranstaltungartEinzelheiten, text='Veranstaltungsarten')
        
        self.frmTagungenEinzelheiten = ttk.PanedWindow(
            self.frmNbkTagung,
            orient=tk.HORIZONTAL)
        self.nbkTagung.add(self.frmTagungenEinzelheiten, text='Stammdaten')
        
        self.frmMails = ttk.PanedWindow(
            self.frmNbkTagung,
            orient=tk.HORIZONTAL)
        self.nbkTagung.add(self.frmMails, text='Mails')
        
        self.frmFarben = ttk.PanedWindow(
            self.frmNbkVerwaltung,
            orient=tk.HORIZONTAL)
        self.nbkVerwaltung.add(self.frmFarben, text='Farben')
        
        self.frmFarbenListe = ttk.Frame(self.nbkVerwaltung)
        self.nbkVerwaltung.add(self.frmFarbenListe, text='Farben (Liste)')
        self.frmFarbenListeNavi = ttk.Frame(self.frmFarbenListe)
        self.frmFarbenListeInhalt = yScrolledFrame(self.frmFarbenListe)
        self.frmFarbenListeNavi.pack(
            side=tk.TOP,
            anchor=tk.W)
        self.frmFarbenListeInhalt.pack(
            side=tk.TOP,
            expand=tk.YES,
            fill=tk.BOTH)
        
        self.frmLaenderListe = ttk.Frame(self.nbkVerwaltung)
        self.nbkVerwaltung.add(self.frmLaenderListe, text='Länder')
        self.frmLaenderListeNavi = ttk.Frame(self.frmLaenderListe)
        self.frmLaenderListeInhalt = yScrolledFrame(self.frmLaenderListe)
        self.frmLaenderListeNavi.pack(
            side=tk.TOP,
            anchor=tk.W)
        self.frmLaenderListeInhalt.pack(
            side=tk.TOP,
            expand=tk.YES,
            fill=tk.BOTH)
        
        self.frmJobsEinzelheiten = ttk.PanedWindow(
            self.frmNbkVerwaltung,
            orient=tk.HORIZONTAL)
        self.nbkVerwaltung.add(self.frmJobsEinzelheiten, text='Reg. Aufgaben')
        
        self.frmJobsListe = ttk.Frame(self.nbkVerwaltung)
        self.nbkVerwaltung.add(self.frmJobsListe, text='Reg. Aufg. (Liste)')
        self.frmJobsListeNavi = ttk.Frame(self.frmJobsListe)
        self.frmJobsListeInhalt = yScrolledFrame(self.frmJobsListe)
        self.frmJobsListeNavi.pack(
            side=tk.TOP,
            anchor=tk.W)
        self.frmJobsListeInhalt.pack(
            side=tk.TOP,
            expand=tk.YES,
            fill=tk.BOTH)
        
        self.frmStatusListe = ttk.Frame(self.nbkVerwaltung)
        self.nbkVerwaltung.add(self.frmStatusListe, text='Status (Liste)')
        self.frmStatusListeNavi = ttk.Frame(self.frmStatusListe)
        self.frmStatusListeInhalt = yScrolledFrame(self.frmStatusListe)
        self.frmStatusListeNavi.pack(
            side=tk.TOP,
            anchor=tk.W)
        self.frmStatusListeInhalt.pack(
            side=tk.TOP,
            expand=tk.YES,
            fill=tk.BOTH)

def main():
    configuration()
    
    hauptprogramm = Hauptprogramm()
    hauptprogramm.mainloop()

if __name__ == '__main__':
    main()
