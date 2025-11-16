class Perfil():
    def __init__(self, nome: str, profissão: str, areas_interesse: list, soft_skills: list, hard_skills: list):
        self.nome = nome
        self.profissao = profissão
        self.areas_interesse = areas_interesse
        self.soft_skills = soft_skills
        self.hard_skills = hard_skills

    def exibir_perfil(self):
        return f"\nNome: {self.nome}\nProfissão: {self.profissao}\nÁreas de interesse: {self.areas_interesse}\nSoft Skills: {self.soft_skills}\nHard Skills: {self.hard_skills}"