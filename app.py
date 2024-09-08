import streamlit as st

def parse_txt(filename):
    projects = []
    
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    
    blocks = content.split('Novo projeto recebido!\n')
    
    for block in blocks[1:]: 
        
        name_start = block.find('Nome\n') + len('Nome\n')
        name_end = block.find('\n', name_start)
        name = block[name_start:name_end].strip()
        
        link_start = block.find('Link do github com o projeto\n') + len('Link do github com o projeto\n')
        link_end = block.find('\n', link_start)
        github_link = block[link_start:link_end].strip()
        
        description_start = block.find('Descrição do projeto\n') + len('Descrição do projeto\n')
        description_end = block.find('\n', description_start)
        description = block[description_start:description_end].strip()
        
        reactions = 0
      
        reactions_start = block.find('{Reactions}\n⭐ (') + len('{Reactions}\n⭐ (')
        if reactions_start > len('{Reactions}\n⭐ ('):
            reactions_end = block.find(')', reactions_start)
            try:
                reactions = int(block[reactions_start:reactions_end].strip())
            except ValueError:
                reactions = 0
        
        projects.append((name, github_link, reactions))
    
    sorted_projects = sorted(projects, key=lambda x: x[2], reverse=True)
    
    return sorted_projects

def display_projects(st, projects):
    if not projects:
        st.markdown("Nenhum projeto encontrado.")
    for i, (name, github_link, reactions) in enumerate(projects, start=1):
        st.markdown(f"{i}. **Nome**: {name}")
        st.markdown(f"   **Link do GitHub**: [Link]({github_link})")
        st.markdown(f"   **Reações**: :orange[{reactions}]")

def main():
    st.set_page_config(page_title="Ranking Alura", layout="wide", initial_sidebar_state="auto", menu_items=None)

    st.title("🏆 Ranking Alura :gray[Não Oficial] - Última Atualização (02:30)")

    input_filename = 'ranking.txt'
    projects = parse_txt(input_filename)
    top_30_projects = projects[:30]

    col1, col2, col3 = st.columns(3)
   
    top_10 = top_30_projects[:10]
    top_20 = top_30_projects[10:20]
    top_30 = top_30_projects[20:30]

    with col1:
        display_projects(st, top_10)
    
    with col2:
        display_projects(st, top_20)
    
    with col3:
        display_projects(st, top_30)

    st.markdown("## ⏰ Próxima atualização às 10:00. Total de projetos: 1677")

    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown(":orange[⭐ Deixe o seu like no meu projeto [aqui](https://discord.com/channels/1277631721822748742/1277631722716008535/1281647648096518155)]")

    with col5:
        st.markdown(":blue[🌐 Acesse o meu projeto [aqui](https://devspaceee.vercel.app/index.html)]")

    with col6:
        st.markdown("Repositório do ranking [aqui](https://github.com/matheusaudibert/ranking_alura)")

    # Barra de pesquisa para encontrar projetos
    st.sidebar.header("🔍 Pesquisar Projetos")
    search_name = st.sidebar.text_input("Digite o nome seu nome:")

    if search_name:
        # Filtra projetos que contêm o nome pesquisado e obtém suas posições
        results = [(index + 1, project) for index, project in enumerate(projects) if search_name.lower() in project[0].lower()]
        
        if results:
            st.sidebar.markdown(f"Resultados para '{search_name}':")
            for position, (name, github_link, reactions) in results:
                st.sidebar.markdown(f"{position}. **Nome**: {name}")
                st.sidebar.markdown(f"   **Link do GitHub**: [Link]({github_link})")
                st.sidebar.markdown(f"   **Reações**: :orange[{reactions}]")
        else:
            st.sidebar.markdown("Não te encotrei 😕.")

if __name__ == "__main__":
    main()
