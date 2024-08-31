from dotenv import load_dotenv
load_dotenv()
import os
API_KEY = os.environ.get("OPENAI_API_KEY")

def get_user_preferences():
    print("Film türlerini seçin (virgülle ayırarak):")
    print("Aksiyon, Komedi, Drama, Bilim Kurgu, Korku")
    genres = input("Seçilen türler: ").split(',')
    
    favorite_movies = []
    for i in range(3):
        movie = input(f"En sevdiğiniz {i+1}. film: ")
        favorite_movies.append(movie)
    
    return genres, favorite_movies

def get_recommendations(genres, favorite_movies):
    prompt = f"""
    Kullanıcının tercih ettiği film türleri: {', '.join(genres)}
    Kullanıcının en sevdiği 3 film: {', '.join(favorite_movies)}
    
    Lütfen bu bilgilere dayanarak 5 film önerisi yapın. Önerileri aşağıdaki formatta bir tablo olarak sunun:
    
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
        return "Üzgünüm, bir hata oluştu. Lütfen daha sonra tekrar deneyin."

def main():
    print("Film Öneri Sistemine Hoş Geldiniz!")
    genres, favorite_movies = get_user_preferences()
    recommendations = get_recommendations(genres, favorite_movies)
    print("\nİşte size özel film önerileri:\n")
    print(recommendations)

if __name__ == "__main__":
    main()
