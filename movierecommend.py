from dotenv import load_dotenv
load_dotenv()
import os
API_KEY = os.environ.get("OPENAI_API_KEY")
def get_recommendations(genres, favorite_movies):
    prompt = f"""
    Kullanıcının tercih ettiği film türleri: {', '.join(genres)}
    Kullanıcının en sevdiği 3 film: {', '.join(favorite_movies)}
    
    Lütfen bu bilgilere dayanarak 5 film önerisi yapın. Önerdiğiniz filmler, kullanıcının belirttiği favori filmlerden farklı olmalıdır. 
    Önerileri aşağıdaki formatta bir tablo olarak sunun:
    
    | Film Adı | Tür | Kısa Özet |
    |----------|-----|-----------|
    | ... | ... | ... |
    
    Lütfen sadece tabloyu döndürün, başka açıklama eklemeyin.
    """
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"API Hatası: {response.status_code} - {response.text}"

def main():
    st.title("Film Öneri Sistemi")
    
    genre_options = ["Aksiyon", "Komedi", "Drama", "Bilim Kurgu", "Korku"]
    genres = st.multiselect("Film türlerini seçin:", genre_options)
    
    favorite_movies = []
    for i in range(3):
        movie = st.text_input(f"En sevdiğiniz {i+1}. film:")
        favorite_movies.append(movie)
    
    if st.button("Öneriler Al"):
        if genres and all(favorite_movies):
            with st.spinner("Film önerileri alınıyor..."):
                recommendations = get_recommendations(genres, favorite_movies)
            st.markdown(recommendations)
        else:
            st.warning("Lütfen en az bir tür seçin ve üç favori film girin.")

if __name__ == "__main__":
    main()
