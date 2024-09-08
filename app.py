import streamlit as st
import csv
from operator import itemgetter

def extract_reactions(reactions):
    if reactions.startswith("⭐"):
        try:
            return int(reactions.split("(")[1].split(")")[0])
        except ValueError:
            return 0
    return 0

def process_csv(filename):
    rows = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            reactions = extract_reactions(row['Reactions'])
            row['ReactionsCount'] = reactions
            rows.append(row)
    
    sorted_rows = sorted(rows, key=itemgetter('ReactionsCount'), reverse=True)
    
    top_30 = sorted_rows[:30]
    return top_30

def generate_ranking(top_30):
    ranking_data = [(i + 1, row['ReactionsCount']) for i, row in enumerate(top_30)]
    return ranking_data

def main():
    st.set_page_config(page_title="Ranking Alura", layout="wide", initial_sidebar_state="auto", menu_items=None)

    input_filename = 'ranking.csv'
    top_30 = process_csv(input_filename)
    data = generate_ranking(top_30)

    st.title("🏆 :gray[Ranking Alura Não Oficial] - Última Atualização (11:00) ")

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    for i, col in enumerate([col1, col2, col3, col4, col5, col6]):
        start_index = i * 5
        end_index = start_index + 5
        with col:
            st.markdown("\n".join([f"{pos}. Lugar = :orange[{stars}] estrelas"
                                   for pos, stars in data[start_index:end_index]]))
    
    st.markdown("## Próxima atualização às 00:00.")
    st.markdown("Repositório do ranking [aqui](https://github.com/matheusaudibert/ranking_alura).")

if __name__ == "__main__":
    main()
