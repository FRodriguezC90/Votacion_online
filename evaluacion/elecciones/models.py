from django.db import models


class Candidato:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.votos = 0

    def identificador(self):
        return f"{self.nombre} {self.apellido}"


class Elecciones:
    def __init__(self):
        self.candidatos = {}

    def inscribir(self, candidato):
        identificador_candidato = candidato.identificador()
        if identificador_candidato in self.candidatos:
            return "Error: El candidato ya existe."

        self.candidatos[identificador_candidato] = candidato
        return "Éxito: Candidato inscrito correctamente."

    def obtener_ganador(self):
        if not self.candidatos:
            return None

        return max(self.candidatos.values(), key=lambda candidato: candidato.votos)

    def hay_empate(self):
        if not self.candidatos:
            return False
        max_votos = max(c.votos for c in self.candidatos.values())
        candidatos_con_max_votos = [
            c for c in self.candidatos.values() if c.votos == max_votos
        ]
        return len(candidatos_con_max_votos) > 1

    def votar_por(self, nombre, apellido):
        identificador_candidato = f"{nombre} {apellido}"
        if identificador_candidato in self.candidatos:
            self.candidatos[identificador_candidato].votos += 1
            return "Voto registrado exitosamente."
        return "Error: No se encontró el candidato."

    def obtener_candidatos(self):
        return list(self.candidatos.values())
