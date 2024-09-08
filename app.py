import streamlit as st

def parse_txt(filename):
    projects = []
    
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Divida o conteúdo em blocos baseados em "Novo projeto recebido!"
    blocks = content.split('Novo projeto recebido!\n')
    
    for block in blocks[1:]:  # Ignora o primeiro bloco vazio
        # Extraia o nome
        name_start = block.find('Nome\n') + len('Nome\n')
        name_end = block.find('\n', name_start)
        name = block[name_start:name_end].strip()
        
        # Extraia o link do GitHub
        link_start = block.find('Link do github com o projeto\n') + len('Link do github com o projeto\n')
        link_end = block.find('\n', link_start)
        github_link = block[link_start:link_end].strip()
        
        # Extraia a descrição
        description_start = block.find('Descrição do projeto\n') + len('Descrição do projeto\n')
        description_end = block.find('\n', description_start)
        description = block[description_start:description_end].strip()
        
        # Inicialize as reações como 0
        reactions = 0
        
        # Extraia o número de reações se a seção {Reactions} estiver presente
        reactions_start = block.find('{Reactions}\n⭐ (') + len('{Reactions}\n⭐ (')
        if reactions_start > len('{Reactions}\n⭐ ('):
            reactions_end = block.find(')', reactions_start)
            try:
                reactions = int(block[reactions_start:reactions_end].strip())
            except ValueError:
                reactions = 0
        
        projects.append((name, github_link, reactions))
    
    # Ordena os projetos com base no número de reações em ordem decrescente
    sorted_projects = sorted(projects, key=lambda x: x[2], reverse=True)
    
    # Retorna apenas os top 30
    return sorted_projects[:30]

def display_projects(st, title, projects, start_index):
    st.markdown(title)
    for i, (name, github_link, reactions) in enumerate(projects, start=start_index):
        st.markdown(f"{i}. **Nome**: {name}")
        st.markdown(f"   **Link do GitHub**: [Link]({github_link})")
        st.markdown(f"   **Reações**: :orange[{reactions}]")

def main():
    st.set_page_config(page_title="Ranking Alura", layout="wide", initial_sidebar_state="auto", menu_items=None)

    st.title("🏆 Ranking Alura :gray[Não Oficial] - Última Atualização (12:30)")

    input_filename = 'ranking.txt'
    top_30_projects = parse_txt(input_filename)

    col1, col2, col3 = st.columns(3)
    
    # Divida os projetos em top 10, top 11-20 e top 21-30
    top_10 = top_30_projects[:10]
    top_20 = top_30_projects[10:20]  # Mostra projetos do 11º ao 20º
    top_30 = top_30_projects[20:30]  # Mostra projetos do 21º ao 30º

    with col1:
        display_projects(st, "#", top_10, start_index=1)
    
    with col2:
        display_projects(st, "#", top_20, start_index=11)
    
    with col3:
        display_projects(st, "#", top_30, start_index=21)

    st.markdown("## Próxima atualização às 00:00.")
    st.markdown("Repositório do ranking [aqui](https://github.com/matheusaudibert/ranking_alura).")

if __name__ == "__main__":
    main()
