from red_social import RedSocial, Usuario


def crear_red_ejemplo():
    
    red = RedSocial()
    
    # Crear usuarios con diferentes gustos
    usuarios = [
        Usuario("Ana", {"música", "fitness", "tecnología", "viajes"}),
        Usuario("Carlos", {"música", "fitness", "deportes", "cocina"}),
        Usuario("María", {"tecnología", "programación", "videojuegos", "música"}),
        Usuario("Pedro", {"fitness", "deportes", "viajes", "fotografía"}),
        Usuario("Laura", {"música", "tecnología", "fotografía", "arte"}),
        Usuario("Juan", {"programación", "tecnología", "videojuegos", "música"}),
        Usuario("Sofía", {"fitness", "cocina", "viajes", "fotografía"}),
        Usuario("Diego", {"deportes", "fitness", "música", "cocina"}),
    ]
    
    # Agregar usuarios a la red
    for usuario in usuarios:
        red.agregar_usuario(usuario)
    
    # Establecer relaciones de amistad
    amistades = [
        ("Ana", "Carlos"),
        ("Ana", "María"),
        ("Ana", "Pedro"),
        ("Carlos", "María"),
        ("Carlos", "Diego"),
        ("María", "Juan"),
        ("María", "Laura"),
        ("Pedro", "Sofía"),
        ("Pedro", "Diego"),
        ("Laura", "Sofía"),
        ("Laura", "Juan"),
        ("Sofía", "Diego"),
    ]
    
    for usuario1, usuario2 in amistades:
        red.agregar_amistad(usuario1, usuario2)
    
    return red


def mostrar_recomendaciones(red: RedSocial):
    """Muestra recomendaciones para todos los usuarios."""
    
    print("=" * 80)
    print("SISTEMA DE RECOMENDACIONES BASADO EN AMIGOS")
    print("=" * 80)
    print()
    
    # Mostrar estadísticas de la red
    stats = red.obtener_estadisticas()
    print("ESTADÍSTICAS DE LA RED SOCIAL")
    print(f"   • Número de usuarios: {stats['num_usuarios']}")
    print(f"   • Número de amistades: {stats['num_amistades']}")
    print(f"   • Densidad de la red: {stats['densidad']:.3f}")
    print(f"   • Componentes conexas: {stats['componentes_conexas']}")
    print(f"   • Grado promedio: {stats['grado_promedio']:.2f}")
    print()
    
    # Mostrar recomendaciones para cada usuario
    for nombre_usuario in red.usuarios.keys():
        usuario = red.usuarios[nombre_usuario]
        amigos = red.obtener_amigos(nombre_usuario)
        
        print("-" * 80)
        print(f"USUARIO: {nombre_usuario}")
        print(f"Gustos actuales: {', '.join(sorted(usuario.gustos))}")
        print(f"Amigos ({len(amigos)}): {', '.join(amigos)}")
        print()
        
        # Mostrar similitud con amigos
        if amigos:
            print("Similitud con amigos:")
            amigos_similares = red.obtener_amigos_ordenados_por_similitud(nombre_usuario)
            for amigo, similitud in amigos_similares:
                print(f"      • {amigo}: {similitud:.2%}")
            print()
        
        # Mostrar recomendaciones
        recomendaciones = red.recomendar_intereses(nombre_usuario, num_recomendaciones=5)
        
        if recomendaciones:
            print("RECOMENDACIONES:")
            for i, (interes, score) in enumerate(recomendaciones, 1):
                print(f"      {i}. {interes} (score: {score:.3f})")
        else:
            print("No hay recomendaciones disponibles (sin amigos o ya tiene todos los gustos)")
        
        print()


def ejemplo_detallado(red: RedSocial):
    """Muestra un ejemplo detallado para un usuario específico."""
    
    print("\n" + "=" * 80)
    print("EJEMPLO DETALLADO: Ana")
    print("=" * 80)
    print()
    
    usuario = "Ana"
    usuario_obj = red.usuarios[usuario]
    
    print(f"Usuario: {usuario}")
    print(f"Gustos: {usuario_obj.gustos}")
    print()
    
    amigos = red.obtener_amigos(usuario)
    print(f"Amigos: {amigos}")
    print()
    
    print("Análisis de similitud con amigos:")
    for amigo in amigos:
        similitud = red.calcular_similitud(usuario, amigo)
        amigo_obj = red.usuarios[amigo]
        gustos_compartidos = usuario_obj.gustos.intersection(amigo_obj.gustos)
        print(f"  • {amigo}:")
        print(f"    - Similitud: {similitud:.2%}")
        print(f"    - Gustos compartidos: {gustos_compartidos}")
        print(f"    - Gustos únicos del amigo: {amigo_obj.gustos - usuario_obj.gustos}")
    print()
    
    recomendaciones = red.recomendar_intereses(usuario, num_recomendaciones=5)
    print("Recomendaciones generadas:")
    for interes, score in recomendaciones:
        print(f"  • {interes}: score {score:.3f}")
        # Mostrar de qué amigos viene esta recomendación
        amigos_contribuyentes = []
        for amigo in amigos:
            amigo_obj = red.usuarios[amigo]
            if interes in amigo_obj.gustos:
                similitud = red.calcular_similitud(usuario, amigo)
                amigos_contribuyentes.append((amigo, similitud))
        
        if amigos_contribuyentes:
            contribuidores = ", ".join([f"{a} (sim: {s:.2%})" for a, s in amigos_contribuyentes])
            print(f"    ← Recomendado por: {contribuidores}")


if __name__ == "__main__":
    # Crear red de ejemplo
    red = crear_red_ejemplo()
    
    # Mostrar recomendaciones para todos
    mostrar_recomendaciones(red)
    
    # Mostrar ejemplo detallado
    ejemplo_detallado(red)

