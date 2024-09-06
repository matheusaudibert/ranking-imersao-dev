import streamlit as st

def main():

  st.set_page_config(page_title="Ranking Alura ", layout="wide", initial_sidebar_state="auto", menu_items=None)

  st.title("🏆 :gray[Ranking Alura Não Oficial] - Ultima Atualização (19:00) ")

  st.markdown(" ### Número de estrelas para estar entre os top 30: :orange[29]")

  col1, col2, col3= st.columns(3);

  with col1:
    st.markdown(""" 1. Lugar = :orange[85] estrelas

2. Lugar = :orange[84] estrelas

3. Lugar = :orange[81] estrelas

4. Lugar = :orange[75] estrelas

5. Lugar = :orange[74] estrelas

6. Lugar = :orange[74] estrelas

7. Lugar = :orange[69] estrelas

8. Lugar = :orange[64] estrelas

9. Lugar = :orange[52] estrelas

10. Lugar = :orange[51] estrelas


""")

  with col2:
    st.markdown("""11. Lugar = :orange[50] estrelas

12. Lugar = :orange[48] estrelas

13. Lugar = :orange[44] estrelas

14. Lugar = :orange[43] estrelas

15. Lugar = :orange[39] estrelas
                
16. Lugar = :orange[38] estrelas

17. Lugar = :orange[38] estrelas

18. Lugar = :orange[38] estrelas

19. Lugar = :orange[38] estrelas

20. Lugar = :orange[37] estrelas
""")
    
  with col3:
   st.markdown("""
21. Lugar = :orange[37] estrelas

22. Lugar = :orange[36] estrelas

23. Lugar = :orange[33] estrelas

24. Lugar = :orange[33] estrelas

25. Lugar = :orange[32] estrelas

26. Lugar = :orange[31] estrelas

27. Lugar = :orange[30] estrelas

28. Lugar = :orange[30] estrelas

29. Lugar = :orange[29] estrelas

30. Lugar = :orange[29] estrelas""")
   
  with col2:
    st.markdown("O ranking é a atualizado a cada 1h. Próxima atualização às 20:00")
      
if __name__ == "__main__":
    main()
