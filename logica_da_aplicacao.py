from models.Perfil import Perfil
from models.Carreira import Carreira
from models.Recomendador import Recomendador


def cadastrar_perfil():
    print("\n--- Cadastro de Perfil ---")

    nome = input("Nome: ")
    profissao = input("Profissão atual: ")

    areas_interesse = input("Áreas de interesse (separe por vírgulas): ").split(",")
    soft_skills = input("Soft Skills (separe por vírgulas): ").split(",")
    hard_skills = input("Hard Skills (separe por vírgulas): ").split(",")

    areas_interesse = [a.strip() for a in areas_interesse]
    soft_skills = [s.strip() for s in soft_skills]
    hard_skills = [h.strip() for h in hard_skills]

    return Perfil(nome, profissao, areas_interesse, soft_skills, hard_skills)


def criar_carreiras_padrao():
    return [
        Carreira(
            "Desenvolvedor Backend",
            ["Python", "APIs", "Banco de Dados", "Lógica"],
            ["Resolução de problemas", "Pensamento analítico"]
        ),
        Carreira(
            "Engenheiro de Dados",
            ["Python", "SQL", "ETL", "Cloud"],
            ["Organização", "Raciocínio lógico"]
        ),
        Carreira(
            "UX Designer",
            ["Figma", "Design"],
            ["Criatividade", "Empatia", "Comunicação"]
        ),
        Carreira(
            "Cientista de Dados",
            ["Python", "Machine Learning", "Estatística"],
            ["Pensamento crítico", "Curiosidade"]
        ),
        Carreira(
            "DevOps Engineer",
            ["Linux", "Docker", "Cloud", "CI/CD"],
            ["Proatividade", "Adaptabilidade"]
        ),
        Carreira(
            "Engenheiro de Machine Learning",
            ["Python", "Machine Learning", "Deep Learning", "Data Pipelines"],
            ["Pensamento analítico", "Curiosidade", "Resolução de problemas"]
        ),
        Carreira(
            "Analista de Segurança da Informação",
            ["Linux", "Redes", "Segurança da Informação", "Pentest", "SIEM"],
            ["Atenção a detalhes", "Pensamento crítico", "Persistência"]
        ),
        Carreira(
            "Product Owner",
            ["Scrum", "Gestão de backlog", "Análise de requisitos"],
            ["Liderança", "Comunicação", "Tomada de decisão"]
        ),
        Carreira(
            "Desenvolvedor Mobile",
            ["Kotlin", "Swift", "APIs", "Git"],
            ["Criatividade", "Organização", "Proatividade"]
        ),
        Carreira(
            "Analista de Cloud",
            ["Cloud", "Linux", "Redes", "IaC"],
            ["Adaptabilidade", "Pensamento lógico", "Colaboração"]
        )
    ]


def criar_recomendador():
    carreiras = criar_carreiras_padrao()
    return Recomendador(carreiras)
