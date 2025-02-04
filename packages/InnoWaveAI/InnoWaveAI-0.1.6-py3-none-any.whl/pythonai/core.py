import json
import http.client
import re  # Для очистки ответа

class InnoWaveAI:
    _API_KEY = "2165ec5065898c6227d7f541961c1f1071a59fb437f7994baa7310153fa17c0b"
    _API_HOST = "api.together.xyz"
    _API_PATH = "/v1/chat/completions"

    @classmethod
    def generate_code(cls, prompt: str) -> str:
        try:
            headers = {
                "Authorization": f"Bearer {cls._API_KEY}",
                "Content-Type": "application/json"
            }

            # Уточняем запрос для генерации кода только с нужными конструкциями
            content = f"Напиши только базовый код на Python, использующий только конструкции: if, elif, else, while, for i in range(), print, input. Без классов, функций или других конструкций, также чтобы были переменные английского алфавита по примеру, a, b, c, d и так далее . Реши задачу:\n{prompt}"

            data = json.dumps({
                "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
                "messages": [{"role": "user", "content": content}],
                "temperature": 0.7
            })

            conn = http.client.HTTPSConnection(cls._API_HOST)
            conn.request("POST", cls._API_PATH, body=data, headers=headers)

            response = conn.getresponse()
            result = response.read().decode()
            conn.close()

            result_json = json.loads(result)

            if "choices" in result_json and result_json["choices"]:
                content = result_json["choices"][0]["message"]["content"]
                # Убираем тройные кавычки и пометки ```python
                content = re.sub(r"```[^\n]*\n", "", content)  # Убираем начало ```python
                content = content.replace("```", "").strip()  # Убираем конец ```
                return content

            return "Ошибка: пустой или некорректный ответ от модели."
        except Exception as e:
            return f"Ошибка запроса: {e}"

    @classmethod
    def print(cls, prompt: str):
        result = cls.generate_code(prompt)
        print(result)