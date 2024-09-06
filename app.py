import streamlit as st

def main():

  st.set_page_config(page_title="Ranking Alura ", layout="wide", initial_sidebar_state="auto", menu_items=None)

  st.title("🏆 :gray[Ranking Alura Não Oficial] - Ultima Atualização (20:00) ")

  st.markdown("### Número de estrelas para estar entre os top 30: :orange[31]")

  # Criar as colunas para exibir o ranking
  col1, col2, col3, col4, col5, col6 = st.columns(6)

  # Dados de ranking
  ranking_data = [
    (1, 86), (2, 86), (3, 84), (4, 79), (5, 76),
    (6, 74), (7, 69), (8, 67), (9, 53), (10, 53),
    (11, 51), (12, 51), (13, 50), (14, 43), (15, 43),
    (16, 42), (17, 39), (18, 39), (19, 38), (20, 38),
    (21, 38), (22, 37), (23, 36), (24, 35), (25, 34),
    (26, 34), (27, 33), (28, 32), (29, 32), (30, 31)
  ]

  # Exibir os dados nas colunas
  for i, col in enumerate([col1, col2, col3, col4, col5, col6]):
    start_index = i * 5
    with col:
        st.markdown("\n".join([f"{pos}. Lugar = :orange[{stars}] estrelas"
                               for pos, stars in ranking_data[start_index:start_index+5]]))
   
  
  st.markdown("## Próxima atualização às 21:00.")

if __name__ == "__main__":
    main()
