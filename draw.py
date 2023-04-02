import random
import pandas as pd
import streamlit as st
import time 


def filter_dataframe(df: pd.DataFrame, ticket_price: int):
    # Get only rows where the invoice is paid (Accounted = True) and the email is not empty
    df = df[(df['Accounted'] == True) & (df['BuyerEmail'].notnull())]
    # Add a column with the number of tickets bought
    df['N_Tickets'] = df['InvoicePrice'] / ticket_price
    # Keep only the columns we need ['PaymentId', 'N_Tickets', 'BuyerEmail']
    df = df[['PaymentId', 'N_Tickets', 'BuyerEmail']].copy()
    return df

def draw(df: pd.DataFrame, number_of_winners: int):
    # Draw the N different emails from the dataframe, based on the number of tickets bought
    winners = random.choices(df['BuyerEmail'], weights=df['N_Tickets'], k=number_of_winners)
    if len(set(winners)) != len(winners):
        # If there are duplicates, draw again
        winners = draw(df, number_of_winners)
    return winners

    
st.title('Lotteria Pasquale SatoshiSpritz Torino 2023') 

ticket_price = st.number_input('Inserire il prezzo di un biglietto', min_value=1, value=7650)
number_of_winners = st.number_input('Inserire il numero di vincitori', min_value=1, value=3)

st.write(f'Il prezzo di un singolo biglietto è di {ticket_price} sats')
st.write(f'Il numero di vincitori sarà di {number_of_winners}')

# Load file of  BTC Pay Server Invoces CSV 
st.subheader('Caricare CSV BTC PayServer')
invoices_file = st.file_uploader('Caricare file invoices BTCPayServer in formato CSV', type='csv')

if invoices_file is not None:
    df = pd.read_csv(invoices_file)
    st.success('File caricato correttamente!')
    
    # Filter the dataframe
    filterd_df = filter_dataframe(df, ticket_price)
    
    with st.expander('Show filtered dataframe'):
        st.write(filterd_df[['BuyerEmail', 'N_Tickets']])
        

    # Draw the winning 
    if st.button('Estrazione vincitori'):
        
        with st.spinner(text='Estrazione in corso...'):
            # Draw the winners
            winners = draw(filterd_df, number_of_winners)
            st.success(f'Vincitori estratti con successo!')
            st.write(f"Un po' di suspense...")
            for i, winner in enumerate(winners):
                time.sleep(10)
                st.success(f'Il vincitore numero {i+1} è: {winner}')
                st.balloons()

            # Dump the winners to a CSV file (with the timestamp)
            timestamp = pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')
            filename = f'./estrazioni/winners_{timestamp}.csv'

            # Create a dataframe with the winners emails and payment Ids to be able to check the payments
            winners_df = df[df['BuyerEmail'].isin(winners)][['PaymentId', 'BuyerEmail']]
            winners_df.to_csv(filename, index=False)
            
            st.write(f'File {filename} creato con successo!')