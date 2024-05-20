# Eserciziario di Statistica

Benvenuti all'eserciziario di statistica! Questo progetto contiene esercizi di statistica che l'utente deve implementare e verificare mediante test automatici.

## Struttura del Progetto

- `src/`: Contiene le classi che modellano gli esercizi di statistica.
- `tests/`: Contiene i test unitari per verificare le implementazioni degli esercizi.

## Come Funziona

1. Ogni classe in `src/` rappresenta un esercizio di statistica. 
2. Queste classi hanno un metodo principale, `execute()` che deve essere implementato dall'utente.
3. I test corrispondenti agli esercizi si trovano nella directory `tests/` e contengono le soluzioni corrette.
4. L'utente implementa il metodo della classe relativa all'esercizio d'interesse in `src/`.
5. L'utente esegue i test per validare la propria implementazione.

## Requisiti

- Python 3.x
- `pip`

## Installazione

1. Clonare il repository:
   ```sh
   git clone https://github.com/gozus19p/esercizi-statistica.git
   cd esercizi-statistica
   ```

2. Installare i requisiti:
   ```sh
   pip install -r requirements.txt
   ```

## Esecuzione dei Test

1. Implementare la classe dell'esercizio d'interesse in `src/`.
2. Eseguire i test utilizzando `pytest`:
   ```sh
   pytest
   ```

## Esempio di Utilizzo

1. Implementare il metodo mancante nella classe di un esercizio in `src/`.
2. Eseguire i test per verificare la correttezza dell'implementazione:
   ```sh
   pytest tests/test_nome_esercizio.py
   ```

## Contributi

I contributi sono benvenuti! Sentitevi liberi di aprire issue e pull request.
