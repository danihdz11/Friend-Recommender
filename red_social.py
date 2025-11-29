from typing import Set, List, Dict, Tuple
import networkx as nx
from collections import Counter


class Usuario:    
    def __init__(self, nombre: str, gustos: Set[str]):
        self.nombre = nombre
        self.gustos = gustos
    
    def __repr__(self):
        return f"Usuario(nombre='{self.nombre}', gustos={self.gustos})"


class RedSocial:
    def __init__(self):
        self.grafo = nx.Graph()  # Grafo no dirigido para representar amistades
        self.usuarios: Dict[str, Usuario] = {}  # Diccionario de usuarios por nombre
    
    def agregar_usuario(self, usuario: Usuario):
        if usuario.nombre in self.usuarios:
            raise ValueError(f"El usuario '{usuario.nombre}' ya existe en la red")
        
        self.usuarios[usuario.nombre] = usuario
        self.grafo.add_node(usuario.nombre, usuario=usuario)


    def agregar_amistad(self, usuario1: str, usuario2: str):
        if usuario1 not in self.usuarios:
            raise ValueError(f"El usuario '{usuario1}' no existe en la red")
        if usuario2 not in self.usuarios:
            raise ValueError(f"El usuario '{usuario2}' no existe en la red")
        if usuario1 == usuario2:
            raise ValueError("Un usuario no puede ser amigo de sí mismo")
        
        self.grafo.add_edge(usuario1, usuario2)
    

    def obtener_amigos(self, nombre_usuario: str) -> List[str]:

        if nombre_usuario not in self.usuarios:
            raise ValueError(f"El usuario '{nombre_usuario}' no existe en la red")
        
        return list(self.grafo.neighbors(nombre_usuario))
    

    def calcular_similitud(self, usuario1: str, usuario2: str) -> float:

        if usuario1 not in self.usuarios:
            raise ValueError(f"El usuario '{usuario1}' no existe en la red")
        if usuario2 not in self.usuarios:
            raise ValueError(f"El usuario '{usuario2}' no existe en la red")
        
        gustos1 = self.usuarios[usuario1].gustos
        gustos2 = self.usuarios[usuario2].gustos
        
        if not gustos1 and not gustos2:
            return 1.0  # Ambos sin gustos = idénticos
        if not gustos1 or not gustos2:
            return 0.0  # Uno sin gustos = sin similitud
        
        gustos_compartidos = gustos1.intersection(gustos2)
        gustos_totales = gustos1.union(gustos2)
        
        return len(gustos_compartidos) / len(gustos_totales) if gustos_totales else 0.0
    
    def obtener_amigos_ordenados_por_similitud(self, nombre_usuario: str, 
                                               limite: int = None) -> List[Tuple[str, float]]:

        amigos = self.obtener_amigos(nombre_usuario)
        similitudes = [
            (amigo, self.calcular_similitud(nombre_usuario, amigo))
            for amigo in amigos
        ]
        similitudes.sort(key=lambda x: x[1], reverse=True)
        
        if limite:
            return similitudes[:limite]
        return similitudes
    
    def recomendar_intereses(self, nombre_usuario: str, 
                            num_recomendaciones: int = 5,
                            num_amigos_considerar: int = None) -> List[Tuple[str, float]]:

        if nombre_usuario not in self.usuarios:
            raise ValueError(f"El usuario '{nombre_usuario}' no existe en la red")
        
        usuario = self.usuarios[nombre_usuario]
        gustos_usuario = usuario.gustos
        
        # Obtener amigos ordenados por similitud
        amigos_similares = self.obtener_amigos_ordenados_por_similitud(
            nombre_usuario, 
            limite=num_amigos_considerar
        )
        
        if not amigos_similares:
            return []  # Sin amigos = sin recomendaciones
        
        # Contar gustos de amigos ponderados por similitud
        scores_gustos: Dict[str, float] = {}
        
        for amigo_nombre, similitud in amigos_similares:
            amigo = self.usuarios[amigo_nombre]
            for gusto in amigo.gustos:
                # Solo considerar gustos que el usuario no tiene
                if gusto not in gustos_usuario:
                    # Ponderar por similitud: amigos más similares tienen más peso
                    scores_gustos[gusto] = scores_gustos.get(gusto, 0.0) + similitud
        
        # Ordenar por score descendente
        recomendaciones = sorted(
            scores_gustos.items(), 
            key=lambda x: x[1], 
            reverse=True
        )
        
        return recomendaciones[:num_recomendaciones]
    
    def obtener_estadisticas(self) -> Dict:

        return {
            'num_usuarios': len(self.usuarios),
            'num_amistades': self.grafo.number_of_edges(),
            'densidad': nx.density(self.grafo),
            'componentes_conexas': nx.number_connected_components(self.grafo),
            'grado_promedio': sum(dict(self.grafo.degree()).values()) / len(self.usuarios) if self.usuarios else 0
        }
    
    def __repr__(self):
        return f"RedSocial(usuarios={len(self.usuarios)}, amistades={self.grafo.number_of_edges()})"

