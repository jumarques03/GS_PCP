import os
import json
from dotenv import load_dotenv
import google.generativeai as genai


class Recomendador:
    def __init__(self, carreiras: list):
        self.carreiras = carreiras
        load_dotenv()
        GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
        genai.configure(api_key=GOOGLE_API_KEY)

    def recomendar(self, perfil):
        melhor_carreira = ""
        melhor_score = 0

        for carreira in self.carreiras:
            score = carreira.calcular_match(perfil)

            if score > melhor_score:
                melhor_score = score
                melhor_carreira = carreira
        
        if melhor_carreira == "":
            return "Não foi possível recomendar uma carreira."
            
        return melhor_carreira
    
    def explicar_recomendacao(self, perfil, carreira_recomendada):
        perfil_info = {
            "nome": perfil.nome,
            "profissao_atual": perfil.profissao,
            "areas_interesse": perfil.areas_interesse,
            "soft_skills": perfil.soft_skills,
            "hard_skills": perfil.hard_skills
        }
        
        carreira_info = {
            "nome": carreira_recomendada.nome,
            "hard_skills_requeridas": carreira_recomendada.hard_requeridas,
            "soft_skills_requeridas": carreira_recomendada.soft_requeridas
        }
        
        perfil_formatado = json.dumps(perfil_info, indent=2, ensure_ascii=False)
        carreira_formatada = json.dumps(carreira_info, indent=2, ensure_ascii=False)
        
        system_prompt = """
        Você é um assistente de recomendação de carreiras.
        Explique de forma simples e direta por que aquela carreira foi recomendada para o usuário.
        Use apenas 2 a 3 frases objetivas.
        Foque nas habilidades que o usuário possui que combinam com a carreira.
        Em seguida, recomende uma trilha de aprendizado de acordo com a carreira recomendada. Seja breve nessa recomendação.
        Responda em português brasileiro, sem usar markdown ou formatação especial.
        """
        
        user_prompt = f"""
        ### PERFIL DO USUÁRIO ###
        {perfil_formatado}
        
        ### CARREIRA RECOMENDADA ###
        {carreira_formatada}
        
        Explique por que essa carreira foi recomendada para esse usuário.
        """
        
        generation_config = {
            "temperature": 0.7,
            "max_output_tokens": 200,
        }
        
        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash-lite-001",
            system_instruction=system_prompt,
            generation_config=generation_config
        )
        
        resposta = model.generate_content(user_prompt)
        
        return resposta.text.strip()