# Lotteria Pasquale 2023

Repository Lotteria Pasquale organizzata dal Satoshi Spritz Torino per il 2023


## Regolamento 

Per partecipare alla Lotteria Pasquale indetta sul canale telegram SatoshiSpritz Torino è necessario seguire attentamente le seguenti disposizioni.

### Periodo di Svolgimento: 

Da Domenica 02.04.2023 (CEST) alle ore 22 fino alle ore 21 del giorno 06.04.2023 (CEST)

Numero dei biglietti messi in vendita e il loro prezzo: **90 biglietti per un costo di 7650 sats a singolo biglietto**

Destinazione dei fondi raccolti: 459.000 sats verranno usati per l’acquisto delle uova premio.
Tutto il ricavato superiore alla cifra precedente verrà donato all’ente scelto dal gruppo [SatoshiSpritzTorino](https://t.me/satoshispritztorino)

### Premi
Quantità e natura dei premi: 3 uova di Pasqua dal valore di euro 40 cad messi a disposizione della gelateria Modo di Torino


### Partecipazione

Per partecipare alla Lotteria Pasquale sarà necessario collegarsi al link sottostante per poter procedere all’acquisto dei ticket.

Link per l’acquisto dei ticket per la Lotteria Pasquale: https://btcpay.gianlock.xyz/apps/4DXSHppzLHDZPeGeAovr4Q6L1kBJ/pos

Si ringrazia l'utente gianlock per aver messo a disposizione il proprio BTCPayServer per l'acquisto dei ticket.

**Una volta effettuato l’acquisto dovrete inserire una email (è possibile inserirne una inventata oppure una creata per l'occasione). Servirà al fine di risalire al vincitore della Lotteria Pasquale.**

**Necessario salvarsi la ricevuta del pagamento di BTCPayServer per poter verificare la vincita. Utilizzeremo il transaction ID per verificare la vincita della lotteria Pasquale.**

Si accettano esclusivamente pagamenti in Bitcoin tramite Lightning Network.


## Premiazione 

Luogo e data in cui vengono esposti i premi: Durante il SatoshiSpritz Torino del giorno 06.04.2023

Luogo e tempo fissato per l’estrazione e consegna dei premi: Durante il SatoshiSprits del giorno 06.04.2023 alle ore 21:00


## Estrazione dei premi

Durante il SatoshiSpritz del 06.04.2023 verranno estratti i 3  vincitori della Lotteria Pasquale attraverso uno script creato ad hoc per l’occasione, presente in questo repository, chiamato draw.py.

Useremo per l’estrazione dei vincitori un file CSV estratto direttamente dal BTCPayServer, che contiene tutte le informazioni che riguardano le singole transazioni effettuate per l’acquisto dei ticket. Verrà inserito in questo script per procedere alla estrazione dei tre vincitori.

Modalità della comunicazione della vincita e della consegna dei premi: Durante il SatoshiSpritz verrà comunicato nel canale ufficiale.

I mezzi usati per la pubblicazione del regolamento: [Canale Telegram Ufficiale SatoshiSpritsTorino](https://t.me/satoshispritztorino)


# Utilizzo script estrazione vincitori

Richiesto un environment python3 con le seguenti librerie installate: 
- pandas
- streamlit 
  
Per installare le librerie necessarie eseguire il seguente comando:
```
pip3 install -r requirements.txt
```

Lanciare lo script con il seguente comando:
```
streamlit run draw.py
```
