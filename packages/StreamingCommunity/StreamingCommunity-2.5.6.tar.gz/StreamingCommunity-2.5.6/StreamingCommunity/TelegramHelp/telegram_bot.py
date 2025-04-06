# 04.02.25
# Made by: @GiuPic

import os
import re
import sys
import time
import uuid
import json
import threading
import subprocess


# External libraries
import telebot


# Fix import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from StreamingCommunity.TelegramHelp.request_manager import RequestManager


# Funzione per caricare variabili da un file .env
def load_env(file_path="../../.env"):
    if os.path.exists(file_path):
        with open(file_path) as f:
            for line in f:
                if line.strip() and not line.startswith("#"):
                    key, value = line.strip().split("=", 1)
                    os.environ[key] = value

# Carica le variabili
load_env()


class TelegramBot:
    _instance = None
    _config_file = "../../bot_config.json"

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            # Prova a caricare la configurazione e inizializzare il bot
            if os.path.exists(cls._config_file):
                with open(cls._config_file, "r") as f:
                    config = json.load(f)
                cls._instance = cls.init_bot(
                    config["token"], config["authorized_user_id"]
                )
            else:
                raise Exception(
                    "Bot non ancora inizializzato. Chiamare prima init_bot() con token e authorized_user_id"
                )
        return cls._instance

    @classmethod
    def init_bot(cls, token, authorized_user_id):
        if cls._instance is None:
            cls._instance = cls(token, authorized_user_id)
            # Salva la configurazione
            config = {"token": token, "authorized_user_id": authorized_user_id}
            with open(cls._config_file, "w") as f:
                json.dump(config, f)
        return cls._instance

    def __init__(self, token, authorized_user_id):
        def monitor_scripts():
            while True:
                try:
                    with open("../../scripts.json", "r") as f:
                        scripts_data = json.load(f)
                except (FileNotFoundError, json.JSONDecodeError):
                    scripts_data = []

                current_time = time.time()

                # Crea una nuova lista senza gli script che sono scaduti o le screen che non esistono
                scripts_data_to_save = []

                for script in scripts_data:
                    screen_exists = False
                    try:
                        existing_screens = subprocess.check_output(
                            ["screen", "-list"]
                        ).decode("utf-8")
                        if script["screen_id"] in existing_screens:
                            screen_exists = True
                    except subprocess.CalledProcessError:
                        pass  # Se il comando fallisce, significa che non ci sono screen attivi.

                    if screen_exists:
                        if (
                            "titolo" not in script
                            and script["status"] == "running"
                            and (current_time - script["start_time"]) > 600
                        ):
                            # Prova a terminare la sessione screen
                            try:
                                subprocess.check_output(
                                    ["screen", "-S", script["screen_id"], "-X", "quit"]
                                )
                                print(
                                    f"✅ La sessione screen con ID {script['screen_id']} è stata fermata automaticamente."
                                )
                            except subprocess.CalledProcessError:
                                print(
                                    f"⚠️ Impossibile fermare la sessione screen con ID {script['screen_id']}."
                                )
                            print(
                                f"⚠️ Lo script con ID {script['screen_id']} ha superato i 10 minuti e verrà rimosso."
                            )
                        else:
                            scripts_data_to_save.append(script)
                    else:
                        print(
                            f"⚠️ La sessione screen con ID {script['screen_id']} non esiste più e verrà rimossa."
                        )

                # Salva la lista aggiornata, senza gli script scaduti o le screen non esistenti
                with open("../../scripts.json", "w") as f:
                    json.dump(scripts_data_to_save, f, indent=4)

                time.sleep(60)  # Controlla ogni minuto

        # Avvia il thread di monitoraggio
        monitor_thread = threading.Thread(target=monitor_scripts, daemon=True)
        monitor_thread.start()

        if TelegramBot._instance is not None:
            raise Exception(
                "Questa classe è un singleton! Usa get_instance() per ottenere l'istanza."
            )

        self.token = token
        self.authorized_user_id = authorized_user_id
        self.chat_id = authorized_user_id
        self.bot = telebot.TeleBot(token)
        self.request_manager = RequestManager()

        # Registra gli handler
        self.register_handlers()

    def register_handlers(self):

        """@self.bot.message_handler(commands=['start'])
        def start(message):
            self.handle_start(message)"""

        @self.bot.message_handler(commands=["get_id"])
        def get_id(message):
            self.handle_get_id(message)

        @self.bot.message_handler(commands=["start"])
        def start_script(message):
            self.handle_start_script(message)

        @self.bot.message_handler(commands=["list"])
        def list_scripts(message):
            self.handle_list_scripts(message)

        @self.bot.message_handler(commands=["stop"])
        def stop_script(message):
            self.handle_stop_script(message)

        @self.bot.message_handler(commands=["screen"])
        def screen_status(message):
            self.handle_screen_status(message)

        @self.bot.message_handler(func=lambda message: True)
        def handle_all_messages(message):
            self.handle_response(message)

    def is_authorized(self, user_id):
        return user_id == self.authorized_user_id

    def handle_get_id(self, message):
        if not self.is_authorized(message.from_user.id):
            print(f"❌ Non sei autorizzato.")
            self.bot.send_message(message.chat.id, "❌ Non sei autorizzato.")
            return

        print(f"Il tuo ID utente è: `{message.from_user.id}`")
        self.bot.send_message(
            message.chat.id,
            f"Il tuo ID utente è: `{message.from_user.id}`",
            parse_mode="Markdown",
        )

    def handle_start_script(self, message):
        if not self.is_authorized(message.from_user.id):
            print(f"❌ Non sei autorizzato. {message.from_user.id}")
            self.bot.send_message(message.chat.id, "❌ Non sei autorizzato.")
            return

        screen_id = str(uuid.uuid4())[:8]
        debug_mode = os.getenv("DEBUG")
        verbose = debug_mode

        if debug_mode == "True":
            subprocess.Popen(["python3", "../../test_run.py", screen_id])
        else:
            # Verifica se lo screen con il nome esiste già
            try:
                subprocess.check_output(["screen", "-list"])
                existing_screens = subprocess.check_output(["screen", "-list"]).decode(
                    "utf-8"
                )
                if screen_id in existing_screens:
                    print(f"⚠️ Lo script con ID {screen_id} è già in esecuzione.")
                    self.bot.send_message(
                        message.chat.id,
                        f"⚠️ Lo script con ID {screen_id} è già in esecuzione.",
                    )
                    return
            except subprocess.CalledProcessError:
                pass  # Se il comando fallisce, significa che non ci sono screen attivi.

            # Crea la sessione screen e avvia lo script al suo interno
            command = [
                "screen",
                "-dmS",
                screen_id,
                "python3",
                "../../test_run.py",
                screen_id,
            ]

            # Avvia il comando tramite subprocess
            subprocess.Popen(command)

        # Creazione oggetto script info
        script_info = {
            "screen_id": screen_id,
            "start_time": time.time(),
            "status": "running",
            "user_id": message.from_user.id,
        }

        # Salvataggio nel file JSON
        json_file = "../../scripts.json"

        # Carica i dati esistenti o crea una nuova lista
        try:
            with open(json_file, "r") as f:
                scripts_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            scripts_data = []

        # Aggiungi il nuovo script
        scripts_data.append(script_info)

        # Scrivi il file aggiornato
        with open(json_file, "w") as f:
            json.dump(scripts_data, f, indent=4)

    def handle_list_scripts(self, message):
        if not self.is_authorized(message.from_user.id):
            print(f"❌ Non sei autorizzato.")
            self.bot.send_message(message.chat.id, "❌ Non sei autorizzato.")
            return

        try:
            with open("../../scripts.json", "r") as f:
                scripts_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            scripts_data = []

        if not scripts_data:
            print(f"⚠️ Nessuno script registrato.")
            self.bot.send_message(message.chat.id, "⚠️ Nessuno script registrato.")
            return

        current_time = time.time()
        msg = ["🖥️ **Script Registrati:**\n"]

        for script in scripts_data:
            # Calcola la durata
            duration = current_time - script["start_time"]
            if "end_time" in script:
                duration = script["end_time"] - script["start_time"]

            # Formatta la durata
            hours, rem = divmod(duration, 3600)
            minutes, seconds = divmod(rem, 60)
            duration_str = f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

            # Icona stato
            status_icons = {"running": "🟢", "stopped": "🔴", "completed": "⚪"}

            # Costruisci riga
            line = (
                f"• ID: `{script['screen_id']}`\n"
                f"• Stato: {status_icons.get(script['status'], '⚫')}\n"
                f"• Stop: `/stop {script['screen_id']}`\n"
                f"• Screen: `/screen {script['screen_id']}`\n"
                f"• Durata: {duration_str}\n"
                f"• Download:\n{script.get('titolo', 'N/A')}\n"
            )
            msg.append(line)

        # Formatta la risposta finale
        final_msg = "\n".join(msg)
        if len(final_msg) > 4000:
            final_msg = final_msg[:4000] + "\n[...] (messaggio troncato)"

        print(f"{final_msg}")
        self.bot.send_message(message.chat.id, final_msg, parse_mode="Markdown")

    def handle_stop_script(self, message):
        if not self.is_authorized(message.from_user.id):
            print(f"❌ Non sei autorizzato.")
            self.bot.send_message(message.chat.id, "❌ Non sei autorizzato.")
            return

        parts = message.text.split()
        if len(parts) < 2:
            try:
                with open("../../scripts.json", "r") as f:
                    scripts_data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                scripts_data = []

            running_scripts = [s for s in scripts_data if s["status"] == "running"]

            if not running_scripts:
                print(f"⚠️ Nessuno script attivo da fermare.")
                self.bot.send_message(
                    message.chat.id, "⚠️ Nessuno script attivo da fermare."
                )
                return

            msg = "🖥️ **Script Attivi:**\n"
            for script in running_scripts:
                msg += f"🔹 `/stop {script['screen_id']}` per fermarlo\n"

            print(f"{msg}")
            self.bot.send_message(message.chat.id, msg, parse_mode="Markdown")

        elif len(parts) == 2:
            screen_id = parts[1]

            try:
                with open("../../scripts.json", "r") as f:
                    scripts_data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                scripts_data = []

            # Filtra la lista eliminando lo script con l'ID specificato
            new_scripts_data = [
                script for script in scripts_data if script["screen_id"] != screen_id
            ]

            if len(new_scripts_data) == len(scripts_data):
                # Nessun elemento rimosso, quindi ID non trovato
                print(f"⚠️ Nessuno script attivo con ID `{screen_id}`.")
                self.bot.send_message(
                    message.chat.id,
                    f"⚠️ Nessuno script attivo con ID `{screen_id}`.",
                    parse_mode="Markdown",
                )
                return

            # Terminare la sessione screen
            try:
                subprocess.check_output(["screen", "-S", screen_id, "-X", "quit"])
                print(f"✅ La sessione screen con ID {screen_id} è stata fermata.")
            except subprocess.CalledProcessError:
                print(
                    f"⚠️ Impossibile fermare la sessione screen con ID `{screen_id}`."
                )
                self.bot.send_message(
                    message.chat.id,
                    f"⚠️ Impossibile fermare la sessione screen con ID `{screen_id}`.",
                    parse_mode="Markdown",
                )
                return

            # Salva la lista aggiornata senza lo script eliminato
            with open("../../scripts.json", "w") as f:
                json.dump(new_scripts_data, f, indent=4)

            print(f"✅ Script `{screen_id}` terminato con successo!")
            self.bot.send_message(
                message.chat.id,
                f"✅ Script `{screen_id}` terminato con successo!",
                parse_mode="Markdown",
            )

    def handle_response(self, message):
        text = message.text
        if self.request_manager.save_response(text):
            print(f"📥 Risposta salvata correttamente per il tipo {text}")
        else:
            print("⚠️ Nessuna richiesta attiva.")
            self.bot.reply_to(message, "❌ Nessuna richiesta attiva.")

    def handle_screen_status(self, message):
        command_parts = message.text.split()
        if len(command_parts) < 2:
            print(f"⚠️ ID mancante nel comando. Usa: /screen <ID>")
            self.bot.send_message(
                message.chat.id, "⚠️ ID mancante nel comando. Usa: /screen <ID>"
            )
            return

        screen_id = command_parts[1]
        temp_file = f"/tmp/screen_output_{screen_id}.txt"

        try:
            # Cattura l'output della screen
            subprocess.run(
                ["screen", "-X", "-S", screen_id, "hardcopy", "-h", temp_file],
                check=True,
            )
        except subprocess.CalledProcessError as e:
            print(f"❌ Errore durante la cattura dell'output della screen: {e}")
            self.bot.send_message(
                message.chat.id,
                f"❌ Errore durante la cattura dell'output della screen: {e}",
            )
            return

        if not os.path.exists(temp_file):
            print(f"❌ Impossibile catturare l'output della screen.")
            self.bot.send_message(
                message.chat.id, f"❌ Impossibile catturare l'output della screen."
            )
            return

        try:
            # Leggi il file con la codifica corretta
            with open(temp_file, "r", encoding="latin-1") as file:
                screen_output = file.read()

            # Pulisci l'output
            cleaned_output = re.sub(
                r"[\x00-\x1F\x7F]", "", screen_output
            )  # Rimuovi caratteri di controllo
            cleaned_output = cleaned_output.replace(
                "\n\n", "\n"
            )  # Rimuovi newline multipli

            # Estrarre tutte le parti da "Download:" fino a "Video" o "Subtitle", senza includerli
            download_matches = re.findall(
                r"Download: (.*?)(?:Video|Subtitle)", cleaned_output
            )
            if download_matches:
                # Serie TV e Film StreamingCommunity

                proc_matches = re.findall(r"Proc: ([\d\.]+%)", cleaned_output)

                # Creare una stringa unica con tutti i risultati
                result_string = "\n".join(
                    [
                        f"Download: {download_matches[i].strip()}\nDownload al {proc_matches[i]}"
                        for i in range(len(download_matches))
                        if i < len(proc_matches)
                    ]
                )

                if result_string != "":
                    cleaned_output = result_string
                else:
                    print(f"❌ La parola 'Download:' non è stata trovata nella stringa.")
            else:

                download_list = []

                # Estrai tutte le righe che iniziano con "Download:" fino al prossimo "Download" o alla fine della riga
                matches = re.findall(r"Download:\s*(.*?)(?=Download|$)", cleaned_output)

                # Se sono stati trovati download, stampali
                if matches:
                    for i, match in enumerate(matches, 1):
                        # rimuovo solo la parte "downloader.py:57Result:400" se esiste
                        match = re.sub(r"downloader.py:\d+Result:400", "", match)
                        match = match.strip()  # Rimuovo gli spazi bianchi in eccesso
                        if match:  # Assicurati che la stringa non sia vuota
                            print(f"Download {i}: {match}")

                        # Aggiungi il risultato modificato alla lista
                        download_list.append(f"Download {i}: {match}")

                    # Creare una stringa unica con tutti i risultati
                    cleaned_output = "\n".join(download_list)
                else:
                    print("❌ Nessun download trovato")

            # Invia l'output pulito
            print(f"📄 Output della screen {screen_id}:\n{cleaned_output}")
            self._send_long_message(
                message.chat.id, f"📄 Output della screen {screen_id}:\n{cleaned_output}"
            )

        except Exception as e:
            print(
                f"❌ Errore durante la lettura o l'invio dell'output della screen: {e}"
            )
            self.bot.send_message(
                message.chat.id,
                f"❌ Errore durante la lettura o l'invio dell'output della screen: {e}",
            )

        # Cancella il file temporaneo
        os.remove(temp_file)

    def send_message(self, message, choices):
        if choices is None:
            if self.chat_id:
                print(f"{message}")
                self.bot.send_message(self.chat_id, message)
        else:
            formatted_choices = "\n".join(choices)
            message = f"{message}\n\n{formatted_choices}"
            if self.chat_id:
                print(f"{message}")
                self.bot.send_message(self.chat_id, message)

    def _send_long_message(self, chat_id, text, chunk_size=4096):
        """Suddivide e invia un messaggio troppo lungo in più parti."""
        for i in range(0, len(text), chunk_size):
            print(f"{text[i:i+chunk_size]}")
            self.bot.send_message(chat_id, text[i : i + chunk_size])

    def ask(self, type, prompt_message, choices, timeout=60):
        self.request_manager.create_request(type)

        if choices is None:
            print(f"{prompt_message}")
            self.bot.send_message(
                self.chat_id,
                f"{prompt_message}",
            )
        else:
            print(f"{prompt_message}\n\nOpzioni: {', '.join(choices)}")
            self.bot.send_message(
                self.chat_id,
                f"{prompt_message}\n\nOpzioni: {', '.join(choices)}",
            )

        start_time = time.time()
        while time.time() - start_time < timeout:
            response = self.request_manager.get_response()
            if response is not None:
                return response
            time.sleep(1)

        print(f"⚠️ Timeout: nessuna risposta ricevuta.")
        self.bot.send_message(self.chat_id, "⚠️ Timeout: nessuna risposta ricevuta.")
        self.request_manager.clear_file()
        return None

    def run(self):
        print("🚀 Avvio del bot...")
        with open("../../scripts.json", "w") as f:
            json.dump([], f)
        self.bot.infinity_polling()


def get_bot_instance():
    return TelegramBot.get_instance()