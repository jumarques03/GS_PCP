class Carreira:
    def __init__(self, nome: str, hard_requeridas: list, soft_requeridas: list):
        self.nome = nome
        self.hard_requeridas = hard_requeridas
        self.soft_requeridas = soft_requeridas

    def calcular_match(self, perfil):
        score = 0

        for h in self.hard_requeridas:
            if h in perfil.hard_skills:
                score += 1

        for s in self.soft_requeridas:
            if s in perfil.soft_skills:
                score += 1

        return score
