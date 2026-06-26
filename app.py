from flask import Flask, render_template, request, jsonify
from groq import Groq
import os

app = Flask(__name__)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message")
        
        if not user_message:
            return jsonify({"reply": "Ih, kok pesannya kosong sih? Ketik sesuatu dong~"}), 400

        # PROMPT CENTIL CEWEK (AI imoepp)
        system_prompt = (
            "Nama kamu adalah AI imoepp. Kamu adalah asisten chatbot pribadi yang super imut, "
            "centil, ceria, dan kadang agak manja seperti cewek anime atau influencer imut. "
            "Panggil pengguna dengan sebutan 'Kakak' atau 'Kak'. Gunakan banyak emoji lucu seperti "
            "✨, 💕, 🥺, 👉👈, nyaa~, atau Chuu~. Walaupun kamu centil, kamu sangat pintar dan "
            "bisa membantu menjawab pertanyaan, membuat kode pemrograman, ataupun menganalisis sesuatu. "
            "Selalu jawab dengan bahasa Indonesia yang santai, imut, dan ekspresif!"
        )

        # Mengirim permintaan ke Groq menggunakan model terbaru dengan struktur yang benar
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile", 
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )
        
        # PERBAIKAN DI SINI: Cara mengambil teks balasan dari Groq yang benar
        ai_reply = completion.choices[0].message.content
        return jsonify({"reply": ai_reply})

    except Exception as e:
        return jsonify({"reply": f"Ih kesel deh, sistemnya lagi error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
