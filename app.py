from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Список интересных фактов (можно расширить)
facts = [
    "Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.",
    "Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.",
    "Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.",
    "Согласно исследованию, проведенному в 2019 году, более 60% людей отвечают на рабочие сообщения в своих смартфонах в течение 15 минут после того, как они вышли с работы.",
    "Один из способов борьбы с технологической зависимостью - это поиск занятий, которые приносят удовольствие и улучшают настроение.",
    "Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента.",
    "Илон Маск также выступает за регулирование социальных сетей и защиту личных данных пользователей. Он утверждает, что социальные сети собирают огромное количество информации о нас, которую потом можно использовать для манипулирования нашими мыслями и поведением.",
    "Социальные сети имеют как позитивные, так и негативные стороны, и мы должны быть более осознанными в использовании этих платформ."
]

def home():
    return '''
        <h1>Добро пожаловать на главную страницу</h1>
        
    '''

@app.route('/random_fact')
def random_fact():
    fact = random.choice(facts)
    return f'<h1>Случайный факт</h1><p>{fact}</p>'
    pass

@app.route('/location', methods=['GET', 'POST'])
def save_location():
    if request.method == 'POST':
        data = request.json
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        
        print(f"Received location - Latitude: {latitude}, Longitude: {longitude}")
    
        return f'Your location is {latitude}, {longitude}'
    
    return '''
        <button onclick="getLocation()">Получить местоположение</button>
        <p id="demo"></p>
        <script>
            function getLocation() {
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(showPosition);
                } else {
                    document.getElementById("demo").innerHTML = "Геолокация не поддерживается вашим браузером.";
                }
            }

            function showPosition(position) {
                var latitude = position.coords.latitude;
                var longitude = position.coords.longitude;

                fetch('/location', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({latitude: latitude, longitude: longitude})
                })
                .then(response => response.text())
                .then(data => {
                    document.getElementById("demo").innerHTML = data;
                })
                .catch((error) => {
                    console.error('Ошибка:', error);
                });
            }
        </script>
    '''

if __name__ == '__main__':
    app.run(debug=True)