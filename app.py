from pypresence import Presence
import time

# Remplace par l'ID de ton application Discord
client_id = '1406228219123994735'

# Initialise la connexion RPC
RPC = Presence(client_id)
print("Tentative de connexion à Discord...")
try:
    RPC.connect()
    print("Connecté à Discord RPC.")
except Exception as e:
    print(f"Erreur de connexion à Discord RPC : {e}")
    print("Assure-toi que Discord est lancé et que tu as un client Discord actif.")
    exit()

while True:
    try:
        RPC.update(
            state="release date : unknow",
            details="Adding visual interface"
            # L'argument start= est complètement absent
        )
        print("Rich Presence mise à jour. En attente de la prochaine mise à jour...")
    except Exception as e:
        print(f"Erreur lors de la mise à jour de la Rich Presence : {e}")
        # Gère la reconnexion si nécessaire
        try:
            RPC.connect()
            print("Reconnexion réussie.")
        except Exception as reconnect_e:
            print(f"Échec de la reconnexion : {reconnect_e}. Assurez-vous que Discord est en cours d'exécution.")
            break

    time.sleep(15)
